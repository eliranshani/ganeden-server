import json

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import requests
from models import User


@csrf_exempt
def login(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.save()
        return HttpResponse(user)


def get_singles(request):
    result = {'result': []}
    for i in range(6):
        user = requests.get('https://randomuser.me/api/').json().get('results', [])[0]
        user_name = user.get('name', {})
        try:
            result['result'].append({'name':
                               '{} {}'.format(user_name.get('first', ''), user_name.get('last', '')),
                           'photoUrl':
                               user.get('picture', {}).get('large', '')
                           })
        except UnicodeEncodeError:
            i = i - 1
            continue
    return HttpResponse(json.dumps(result), content_type="application/json")
