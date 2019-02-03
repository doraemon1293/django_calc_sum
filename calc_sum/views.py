# Create your views here.
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        arr = json.loads(request.POST["list"])
        response = json.dumps({"total": sum(arr)})
        return HttpResponse(response, content_type="application/json")
    if request.method == 'GET':
        return HttpResponse('Use POST method to send list in JSON format and retrieve the calculate the summation.')
