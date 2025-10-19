
from django.http import HttpResponse

def index(request):
    return HttpResponse("Successfully deployed to AWS EB with Travis CI")
