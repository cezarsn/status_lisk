import requests
import subprocess
import json
import datetime
from status_lisk import app


def make_request(url, api_path, params):
    url_full = url + api_path + params
    app.logger.debug(url_full)
    try:
        response = requests.get(url_full, params=params, timeout=1,)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.Timeout:
        return False


    #poloniex = controllers.make_requests('https://poloniex.com/public?command=returnTicker')   

def make_poloniex_req(params):
    url_full = 'https://poloniex.com/public'
    params = {'command' : params } 
    try:
        response = requests.get(url_full, params=params, timeout=1,)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.Timeout:
        return {"BTC_LSK":{"last":"-1","lowestAsk":"-1","highestBid":"-1"}}


def get_last_forged():
    tac = subprocess.Popen(['tac','/opt/install/lisk-test/logs.log'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    grep = subprocess.Popen(['grep','-m1', 'Forged'], stdin=tac.stdout, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in grep.stdout.readlines():
        jline = json.loads(line)
        message, timestamp =  jline['message'], jline['timestamp']
    message=message.split(":")[2]
    
    last_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')    
    now = datetime.datetime.now()
    timediff = now -last_time
    timediff_min = timediff.total_seconds()/60 - 120

    retval = grep.wait()
    return (message, timediff_min)
