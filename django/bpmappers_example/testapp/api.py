from django.utils import simplejson as json

from testapp.models import User
from testapp.mappers import UserMapper


def get_user_json(pk):
    user = User.objects.get(pk=pk)
    user_dict = UserMapper(user).as_dict()
    result = json.dumps(user_dict, indent=2)
    return result