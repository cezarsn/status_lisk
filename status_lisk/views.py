from flask import Flask, render_template
from status_lisk import app
import models
import controllers


def status():
    lisk_servers = models.lisk_servers
    for elem in lisk_servers:
        elem.update()
    return lisk_servers


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

    delegate = Delegate("wannabe_rotebaron")
    last_forged = controllers.get_last_forged()
    return render_template('index.html', lisk_servers=lisk_servers, ref_servers=ref_servers, delegate=delegate,
                           poloniex=poloniex, last_forged=last_forged)


@app.route('/demo')
def demo():
    return render_template('demo.html', lisk_servers=status())


@app.errorhandler(500)
def internalServerError(error):
    return "Internal Server Error"
