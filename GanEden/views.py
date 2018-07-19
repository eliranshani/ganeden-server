import json
from random import sample
from django.http import HttpResponse

import requests


def get_singles(request):
    result = {'result': []}
    # user = requests.get('https://randomuser.me/api/').json().get('results', [])[0]
    users = requests.get('http://www.designskilz.com/random-users/fakeusers.json').json()
    male_picture_indexes = sample(range(1, 52), 3)
    female_picture_indexes = sample(range(1, 52), 3)
    pictures_url = 'http://www.designskilz.com/random-users/images/image{}{}.jpg'
    males_pictures_urls = [pictures_url.format('M', i) for i in male_picture_indexes]
    females_pictures_urls = [pictures_url.format('F', i) for i in female_picture_indexes]

    male_first_name_indexes = sample(range(0, 60), 3)
    female_first_name_indexes = sample(range(0, 60), 3)
    males_first_names = [users.get('firstNamesM', {})[i] for i in male_first_name_indexes]
    females_first_names = [users.get('firstNamesF', {})[i] for i in female_first_name_indexes]

    last_name_indexes = sample(range(0, 112), 6)
    last_names = [users.get('lastNames', {})[i] for i in last_name_indexes]

    for i in range(6):
        if i < 3:
            user = {'name': '{} {}'.format(males_first_names[i], last_names[i]),
                    'photoUrl': males_pictures_urls[i]}
        else:
            user = {'name': '{} {}'.format(females_first_names[5-i], last_names[5-i]),
                    'photoUrl': females_pictures_urls[5-i]}

        result['result'].append(user)

    return HttpResponse(json.dumps(result), content_type="application/json")
