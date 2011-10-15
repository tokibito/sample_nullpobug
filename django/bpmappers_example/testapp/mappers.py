from bpmappers import ListDelegateField
from bpmappers.djangomodel import ModelMapper

from testapp.models import User, Group


class GroupMapper(ModelMapper):
    class Meta:
        model = Group


class UserMapper(ModelMapper):
    groups = ListDelegateField(GroupMapper, key='groups.private_groups')

    class Meta:
        model = User
        exclude = ['groups']  # bpmappers bug...