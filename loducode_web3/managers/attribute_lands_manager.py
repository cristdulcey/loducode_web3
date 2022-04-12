from typing import Union
from uuid import UUID

from django.db.models import Manager


class AttributeLandManager(Manager):
    def load_by_id(self, id: Union[UUID, str]):  # pylint: disable=no-self-use,redefined-builtin
        return super().filter(id=id).first()
