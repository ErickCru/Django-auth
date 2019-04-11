def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'google-oauth2':
        url = response['picture']
        print("lo de la url: " + str(url))
