from flask import Flask, render_template
from status_lisk import app
from models import Server, Delegate


@app.route('/')
@app.route('/index')
def index():
    lisk_local = Server(protocol='http', host='192.168.178.31', port='7000', name='LiskLocal TestNet')
    ref_servers = [Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io')]
    delegate = Delegate(lisk_address=123456789092L)
    return render_template('index.html', lisk_servers=lisk_local, ref_servers=ref_servers, delegate= delegate)

