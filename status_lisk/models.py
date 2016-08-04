import controllers
from status_lisk import app


class Server(object):
    def __init__(self, protocol, host, port, name, net):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.name = name
        self.url = '{}://{}:{}/'.format(self.protocol, self.host, self.port)
        self.net = net
        self.is_sync = False
        self.block_height = 0
        self.last_forged = (-1, -1)
        self.is_forging_delegate = False

    def get_block_height(self):
        try:
            block_height = controllers.make_request(self.url, 'api/loader/status/sync', "")['height']
            self.block_height = block_height
        except TypeError:
            self.block_height = -1

    def get_last_forged(self, delegate):
        """
        /api/blocks?generatorPublicKey=0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4&limit=1&orderBy=height:desc

       {"success":true,"blocks":[{"id":"9970641156066037716","version":0,"timestamp":4861570,"height":240604,"previousBlock":"28091283506320323","numberOfTransactions":0,"totalAmount":0,"totalFee":0,"reward":500000000,"payloadLength":0,"payloadHash":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","generatorPublicKey":"0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4","generatorId":"16379340065696424247L","blockSignature":"5e2edfcf73f76d9b57386e87bcef0a18efc5e5fe96ee1aa38ca3f9e4c51f4268d930663b830b885d1712e16a45e76c7bd41cc950c409b0373dfe6b25ff245e00","confirmations":31,"totalForged":"500000000"}],"count":1934}


        :return:
        """

        try:
            last_forged = controllers.make_request(self.url, 'api/blocks',
                                                   {"generatorPublicKey": delegate.public_key, "orderBy": "height:desc",
                                                    "limit": 1,})
            self.last_forged = last_forged['blocks'][0]["height"], last_forged['blocks'][0]["timestamp"]
        except TypeError:
            self.last_forged = -1, -1

    def get_status(self, ref_server):
        """
        Return if the server is in sync with an ref_server
        """
        if (self.block_height % ref_server.block_height) < 10:
            self.is_sync = True
        else:
            self.is_sync = False

    def update(self):
        self.get_block_height()

    def __str__(self):
        return '{} - {}://{}:{}'.format(self.name, self.protocol, self.host, self.port)


"""
http://openmindsro.ddns.net:7000/api/delegates/get?username=wannabe_rotebaron
{"success":true,"delegate":{"username":"wannabe_rotebaron","address":"16379340065696424247L",
"publicKey":"0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4","vote":"85039088874255",
"producedblocks":2445,"missedblocks":902,"rate":78,"approval":0.84,"productivity":73.05}}

"""
"""
Delegate Should be the one and I should implement the check on diffrence between last forging and the block height

"""



class Delegate(object):
    def __init__(self, username):
        self.username = username
        self.address = ""
        self.rate = 0
        self.vote = ""
        self.public_key = ""
        self.produced_blocks = 0
        self.missed_blocks = 0
        self.productivity = 0
        self.approval = 0

    def get_delegate_info(self, server):
        """
        Return the information about a a delegate base on his lisk address
        :param server:
        :return:
        """
        username = self.username
        response = controllers.make_request(server.url, 'api/delegates/get', {"username": username})
        if response:
            self.address = response["delegate"]["address"]
            self.public_key = response["delegate"]["publicKey"]
            self.rate = response["delegate"]['rate']
            self.produced_blocks = response["delegate"]['producedblocks']
            self.missed_blocks = response["delegate"]['missedblocks']
            self.productivity = response["delegate"]['productivity']


    def is_forging(self, server):
        """
        Return is the delegate if forging on a server
        :param server:
        :return:
        """
        if self.public_key != 0:
            response = controllers.make_request(server.url, 'api/delegates/forging/status', {"publicKey": self.public_key})
            if response:
                return response['enabled']
            return None


    def __str__(self):
        return 'Lisk Address:\t{} - Name:\t{} - Rank:\t{}'.format(self.address, self.username, self.rate)


lisk_servers = [Server(protocol='http', host='192.168.178.31', port='7000', name='C Local', net='testnet'),
                Server(protocol='http', host='45.63.117.29', port='7000', name='S Vultr', net='testnet'),
                Server(protocol='http', host='92.222.74.236', port='7000', name='C OVH', net='testnet'),
                Server(protocol='http', host='185.92.221.6', port='8000', name='C Vultr', net='mainnet'),
                Server(protocol='http', host='104.207.130.189', port='8000', name='S Vultr', net='mainnet')]

ref_servers = [Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet'),
               Server(protocol='https', host='login.lisk.io', port='443', name='login.lisk.io', net='mainnet')]

delegate_cezar = Delegate("wannabe_rotebaron")
delegate_stef = Delegate('atreides')

servers_testnet_cezar = [
    Server(protocol='http', host='openmindsro.ddns.net', port='7000', name='C Local', net='testnet'),
    Server(protocol='http', host='92.222.74.236', port='7000', name='C OVH', net='testnet')]

servers_testnet_stef = [Server(protocol='http', host='45.63.117.29', port='7000', name='S Vultr', net='testnet')]

ref_testnet = Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet')
ref_mainnet = Server(protocol='https', host='login.lisk.io', port='443', name='login.lisk.io', net='mainnet')
