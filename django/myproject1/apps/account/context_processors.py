# coding: utf-8
def auth_user(request):
    return {'auth_user': request.auth_user}
