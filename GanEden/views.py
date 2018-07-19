import json

from django.http import HttpResponse

import requests


def get_singles(request):
    result = {'result': []}
    for i in range(6):
        success = False
        while not success:
            try:
                user = requests.get('https://randomuser.me/api/').json().get('results', [])[0]
                user_name = user.get('name', {})
                result['result'].append({'name':
                                         '{} {}'.format(user_name.get('first', ''),
                                                        user_name.get('last', '')),
                                         'photoUrl':
                                         user.get('picture', {}).get('large', '')
                                         })
                success = True
            except UnicodeEncodeError:
                pass
    return HttpResponse(json.dumps(result), content_type="application/json")
