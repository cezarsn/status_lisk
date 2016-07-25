from flask import Flask, render_template
from status_lisk import app
from models import Server, Delegate
import controllers


# TO DO
# chainge the name variable so is going to do dns name resolition
# https://poloniex.com/public?command=returnTicker
# ,"BTC_LSK":{"id":163,"last":"0.00052102","lowestAsk":"0.00052157","highestBid":"0.00052102","percentChange":"0.16374438","baseVolume":"2418.09014754","quoteVolume":"4801192.36555423","isFrozen":"0","high24hr":"0.00054450","low24hr":"0.00044504"},



@app.route('/')
@app.route('/index')
def index():
    lisk_servers = [Server(protocol='http', host='192.168.178.31', port='7000', name='C Local', net='testnet'),
                    Server(protocol='http', host='45.63.117.29', port='7000', name='S Vultr', net='testnet'),
		    Server(protocol='http', host='92.222.74.236', port='7000', name='C OVH', net='testnet'),
                    Server(protocol='http', host='185.92.221.6', port='8000', name='C Vultr', net='mainnet'),
                    Server(protocol='http', host='104.207.130.189', port='8000', name='S Vultr', net='mainnet')]

    ref_servers = [Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet'),
                   Server(protocol='https', host='login.lisk.io', port='443', name='login.lisk.io', net='mainnet')]

    # poloniex = controllers.make_requests('https://poloniex.com/public?command=returnTicker')

    poloniex = controllers.make_poloniex_req('returnTicker')['BTC_LSK']

    delegate = Delegate(lisk_address="16379340065696424247L")
    last_forged = controllers.get_last_forged()
    return render_template('index.html', lisk_servers=lisk_servers, ref_servers=ref_servers, delegate=delegate,
                           poloniex=poloniex, last_forged=last_forged)


@app.route('/demo')
def demo():
    return render_template('demo.html')


@app.errorhandler(500)
def internalServerError(error):
    return "Internal Server Error"
