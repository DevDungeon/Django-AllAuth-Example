import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def test(request):
    return HttpResponse("It is working. User:" + str(request.user))
