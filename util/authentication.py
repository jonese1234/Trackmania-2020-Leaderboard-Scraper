from ..settings import *
import requests
from requests.auth import HTTPBasicAuth


def GetAuthentication():
    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/basic"
    body = '{"audience":"NadeoLiveServices"}'
    result = requests.post(url, data=body, auth=HTTPBasicAuth(login, password))
    return result.json()


def GetTokenRefresh(refreshToken):
    url = "https://prod.trackmania.core.nadeo.online/v2/authentication/token/refresh"
    headers = {'Authorization': 'nadeo_v1 t=' + refreshToken}
    result = requests.post(url, headers=headers)
    return result.json()
