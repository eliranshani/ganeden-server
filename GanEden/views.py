import json
from random import sample
from django.http import HttpResponse

import requests


def get_singles(request):
    users = requests.get('http://www.designskilz.com/random-users/fakeusers.json').json()
    male_picture_indexes = sample(range(1, 52), 6)
    female_picture_indexes = sample(range(1, 52), 6)
    pictures_url = 'http://www.designskilz.com/random-users/images/image{}{}.jpg'
    males_pictures_urls = [pictures_url.format('M', i) for i in male_picture_indexes]
    females_pictures_urls = [pictures_url.format('F', i) for i in female_picture_indexes]

    male_first_name_indexes = sample(range(0, 60), 6)
    female_first_name_indexes = sample(range(0, 60), 6)
    males_first_names = [users.get('firstNamesM', {})[i] for i in male_first_name_indexes]
    females_first_names = [users.get('firstNamesF', {})[i] for i in female_first_name_indexes]

    last_name_indexes = sample(range(0, 112), 12)
    last_names = [users.get('lastNames', {})[i] for i in last_name_indexes]

    address_indexes = sample(range(0, 100), 12)
    addresses = [users.get('addresses', {})[i] for i in address_indexes]

    ages = sample(range(20, 38), 12)

    male_index = 0
    female_index = 0
    age_index = 0
    users_list = []
    for i in range(12):
        if i % 2 == 0:
            user = {'name': '{} {}'.format(males_first_names[male_index], last_names[male_index]),
                    'photoUrl': males_pictures_urls[male_index],
                    'location': addresses[male_index],
                    'age': ages[age_index]}
            male_index += 1
        else:
            user = {'name': '{} {}'.format(females_first_names[female_index], last_names[female_index]),
                    'photoUrl': females_pictures_urls[female_index],
                    'location': addresses[female_index],
                    'age': ages[age_index]}
            female_index += 1
        age_index += 1
        users_list.append(user)

    return HttpResponse(json.dumps({'result': users_list}), content_type="application/json")
