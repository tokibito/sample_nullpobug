from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse


@method_decorator(csrf_exempt, name="dispatch")
class Endpoint(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"method": request.method, "headers": dict(request.headers)})

    def put(self, request, *args, **kwargs):
        return JsonResponse({"method": request.method, "headers": dict(request.headers)})
