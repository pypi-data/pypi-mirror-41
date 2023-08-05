import requests

from weasl.exceptions import WeaslAPIException

_BASE_URL = 'https://api.weasl.in'


def make_weasl_headers(client_id=None, client_secret=None, auth_token=None):
    headers = {'Content-Type': 'application/json'}
    if client_id is not None:
        headers['X-Weasl-Client-Id'] = client_id
    if client_secret is not None:
        headers['X-Weasl-Client-Secret'] = client_secret
    if auth_token is not None:
        headers['Authorization'] = 'Bearer {}'.format(auth_token)
    return headers


def find_user(uuid, client_id):
    res = requests.get(_BASE_URL + '/end_users/{}'.format(uuid), headers=make_weasl_headers(client_id=client_id))
    if res.status_code == 404:
        return None
    elif res.status_code == 200:
        return res.json()
    else:
        raise WeaslAPIException(res.status_code, 'Internal Error')


def find_logged_in_user(client_id, auth_token):
    res = requests.get(_BASE_URL + '/end_users/me', headers=make_weasl_headers(client_id=client_id, auth_token=auth_token))
    if res.status_code == 401:
        return None
    elif res.status_code == 200:
        return res.json()
    else:
        raise WeaslAPIException(res.status_code, 'Internal Error')
