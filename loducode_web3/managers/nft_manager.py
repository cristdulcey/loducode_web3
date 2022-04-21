from typing import Union
from uuid import UUID

from django.db import connection
from django.db.models import Manager


class NftManager(Manager):

    def truncate(self):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(self.model._meta.db_table))

    def load_by_id(self, id: Union[UUID, str]):  # pylint: disable=no-self-use,redefined-builtin
        return super().filter(id=id).first()
