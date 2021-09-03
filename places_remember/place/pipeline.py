import requests

def get_user_avatar(strategy, backend, request, details, response=None, social=None, uid=None,
                    user=None, *args, **kwargs):
    if backend.name == 'facebook':
        url = 'https://graph.facebook.com/v11.0/%s/picture' % response['id']
        parameters = {
            'access_token': response['access_token'],
            'type' : 'large',
            'redirect' : False
        }
        avatar = requests.get(url, params=parameters)
        avatar_url = avatar.json()['data']['url']
        extra_data = social.extra_data
        extra_data['avatar_url'] = avatar_url
        social.set_extra_data(extra_data)
        social.save()
