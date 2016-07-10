from flask import Flask, render_template
from status_lisk import app
from models import Server, Delegate


#TO DO 
# chainge the name variable so is going to do dns name resolition
lisk_servers = [Server(protocol='http', host='192.168.178.31', port='7000', name='C Local', net='testnet'),  
		Server(protocol='http', host='45.63.117.29', port='7000', name='S Vultr', net='testnet'), 
		Server(protocol='http', host='185.92.221.6', port='8000', name='C Vultr', net='mainnet')]

ref_servers = [Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet'), 
		Server(protocol='https', host='login.lisk.io', port='443', name='login.lisk.io', net='mainnet')]


@app.route('/')
@app.route('/index')
def index():
    
    delegate = Delegate(lisk_address = 16379340065696424247L)
    return render_template('index.html', lisk_servers=lisk_servers, ref_servers=ref_servers, delegate= delegate)

