from flask import Flask, render_template
from status_lisk import app
from models import Server, Delegate
import models
import controllers


def status_delegate():
    models.delegate_cezar.get_delegate_info(models.servers_testnet_cezar[0])


def status_server():
    #app.logger.debug(models.lisk_servers)
    models.delegate_cezar.get_delegate_info(models.servers_testnet_cezar[0])
    models.ref_testnet.get_block_height()
    models.servers_testnet_cezar[0].get_last_forged(models.delegate_cezar)

    for server in models.servers_testnet_cezar:
        server.get_block_height()
        server.get_status(models.ref_testnet)




@app.route('/')
@app.route('/index')
def index():
    lisk_servers = [Server(protocol='http', host='192.168.178.31', port='7000', name='C Local', net='testnet'),
<<<<<<< HEAD
                    Server(protocol='http', host='45.32.158.11', port='7000', name='S Vultr', net='testnet'),
		    Server(protocol='http', host='92.222.74.236', port='7000', name='C OVH', net='testnet'),
=======
                    Server(protocol='http', host='45.63.117.29', port='7000', name='S Vultr', net='testnet'),
                    Server(protocol='http', host='92.222.74.236', port='7000', name='C OVH', net='testnet'),
>>>>>>> 3d14a95bd9383ecd95ef8f8de797c4fe26267468
                    Server(protocol='http', host='185.92.221.6', port='8000', name='C Vultr', net='mainnet'),
                    Server(protocol='http', host='104.207.130.189', port='8000', name='S Vultr', net='mainnet'),
                    Server(protocol='http', host='31.187.70.167', port='7000', name='Sa', net='testnet')]

    ref_servers = [Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet'),
                   Server(protocol='https', host='login.lisk.io', port='443', name='login.lisk.io', net='mainnet')]

    # poloniex = controllers.make_requests('https://poloniex.com/public?command=returnTicker')

    poloniex = controllers.make_poloniex_req('returnTicker')['BTC_LSK']

    delegate = Delegate("wannabe_rotebaron")
    last_forged = controllers.get_last_forged()
    return render_template('index.html', lisk_servers=lisk_servers, ref_servers=ref_servers, delegate=delegate,
                           poloniex=poloniex, last_forged=last_forged)


<<<<<<< HEAD


@app.route('/refa_nodul')
def refa_nodul():
    return controllers.rebuild_node()
     



@app.route('/demo')
def demo():
    return render_template('demo.html')
=======
@app.route('/dashboard')
def dashboard():
    status_server()
    return render_template('dashboard.html', lisk_testnet_servers=models.servers_testnet_cezar, ref_testnet = models.ref_testnet)


@app.route('/deaia')
def deaia():
    return status_delegate()
>>>>>>> 3d14a95bd9383ecd95ef8f8de797c4fe26267468


@app.errorhandler(500)
def internalServerError(error):
    return "Internal Server Error"
