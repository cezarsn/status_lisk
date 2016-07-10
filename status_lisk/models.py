import controllerts



class Server(object):
    def __init__(self, protocol, host, port, name, net):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.name = name
        self.url = '{}://{}:{}/'.format(self.protocol, self.host, self.port)
	self.net = net
        self.status = self.get_block_heigh()


    def get_block_heigh(self):
        block_heigh = controllerts.make_request(self.url, 'api/loader/status/sync', "")
        return block_heigh

    def __str__(self):
        return '{} - {}://{}:{}'.format(self.name, self.protocol, self.host, self.port)


class Delegate(object):
    def __init__(self, lisk_address):
        self.lisk_address = lisk_address
        self.name = "wannabe_rotebaron"
        self.rank = 160

    def __str__(self):
        return 'Lisk Address:{} -Name:{} -Rank:{}'.format(self.lisk_address, self.name, self.rank)

lisk_servers = [Server(protocol='http', host='192.168.178.31', port='7000', name='C Local', net='testnet'),  
		Server(protocol='http', host='45.63.117.29', port='7000', name='S Vultr', net='testnet'), 
		Server(protocol='http', host='185.92.221.6', port='8000', name='C Vutlr', net='mainnet')]

ref_servers = [Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet'), 
		Server(protocol='https', host='login.lisk.io', port='443', name='login.lisk.io', net='mainnet')]
