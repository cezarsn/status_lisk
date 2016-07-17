import requests
from status_lisk import app


def make_request(url, api_path, params):
    url_full = url + api_path + params
    app.logger.debug(url_full)
    try:
        response = requests.get(url_full, params=params, timeout=0.5,)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError, requests.ConnectTimeout:
        return False


    #poloniex = controllers.make_requests('https://poloniex.com/public?command=returnTicker')   

def make_poloniex_req(params):
    url_full = 'https://poloniex.com/public'
    params = {'command' : params } 
    try:
        response = requests.get(url_full, params=params, timeout=0.5,)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError, requests.ConnectTimeout:
        return False


