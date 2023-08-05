# Copyright 2017 Oursky Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from .asset import get_signer
from .encoding import deserialize_record, serialize_record
from .error import RecordQueryInvalid, SkygearException
from .models import Record


class Database(object):
    """The Skygear database CRUD class.

    Example:

    >>> database = container.public_database
    >>> database.save(record)

    """

    def __init__(self, container, database_id):
        self.container = container
        self.database_id = database_id

    def save(self, arg, atomic=False):
        """Save Function.

        Args:
            arg1 (list): A list of records
            atomic (bool): Atomic save if true. Defaults to False

        Returns:
            dict: Skygear server response

        Raises:
            SkygearException: If skygear server returns an error.
        """

        if not isinstance(arg, list):
            arg = [arg]
        records = [serialize_record(item)
                   if isinstance(item, Record) else item
                   for item in arg]
        return self.container.send_action('record:save', {
            'database_id': self.database_id,
            'records': records,
            'atomic': atomic
        })

    @staticmethod
    def _encode_id(record_id):
        return record_id.type + "/" + record_id.key

    def delete(self, arg):
        """
        Delete records.


        Args:
            arg (list): List of records or ID

        Returns:
            dict: Skygear server response

        Raises:
            SkygearException: If skygear server returns an error.
        """
        if not isinstance(arg, list):
            arg = [arg]
        ids = [Database._encode_id(item.id)
               if isinstance(item, Record)
               else item
               for item in arg]
        return self.container.send_action('record:delete', {
            'database_id': self.database_id,
            'ids': ids
        })

    def query(self, query):
        """Query records.

        Args:
            query (Query): Query object

        Returns:
            list: List of Record

        Raises:
            SkygearException: If skygear server returns an error.
        """

        include = {v: {"$type": "keypath", "$val": v}
                   for v in list(set(query.include))}

        payload = {'database_id': self.database_id,
                   'record_type': query.record_type,
                   'predicate': query.predicate.to_dict(),
                   'count': query.count,
                   'sort': query.sort,
                   'include': include}

        if query.offset is not None:
            payload['offset'] = query.offset
        if query.limit is not None:
            payload['limit'] = query.limit
        result = self.container.send_action('record:query', payload)
        if 'error' in result:
            raise SkygearException(result['error']['message'],
                                   code=RecordQueryInvalid)
        result = result['result']
        output = []
        signer = None
        for r in result:
            record = deserialize_record(r)
            if '_transient' in r:
                t = r['_transient']
                record['_transient'] = {k: deserialize_record(t[k])
                                        for k in t.keys()}
            if 'attachment' in r:
                if signer is None:
                    signer = get_signer()
                record['attachment'] = r['attachment'].copy()
                record['attachment']['$url'] =\
                    signer.sign(r['attachment']['$name'])
            output.append(record)
        return output
