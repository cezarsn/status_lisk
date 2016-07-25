import controllers


class Server(object):
    def __init__(self, protocol, host, port, name, net):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.name = name
        self.url = '{}://{}:{}/'.format(self.protocol, self.host, self.port)
        self.net = net
        self.status = self.get_block_height()
        self.last_forged = controllers.get_last_forged()
	#self.last_forged = self.get_last_forged("")

    def get_block_height(self):
        try:
            block_height = controllers.make_request(self.url, 'api/loader/status/sync', "")['height']
            return block_height
        except TypeError:
            return False

    def get_last_forged(self, public_key):
        """
        /api/blocks?generatorPublicKey=0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4&limit=1&orderBy=height:desc

       {"success":true,"blocks":[{"id":"9970641156066037716","version":0,"timestamp":4861570,"height":240604,"previousBlock":"28091283506320323","numberOfTransactions":0,"totalAmount":0,"totalFee":0,"reward":500000000,"payloadLength":0,"payloadHash":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","generatorPublicKey":"0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4","generatorId":"16379340065696424247L","blockSignature":"5e2edfcf73f76d9b57386e87bcef0a18efc5e5fe96ee1aa38ca3f9e4c51f4268d930663b830b885d1712e16a45e76c7bd41cc950c409b0373dfe6b25ff245e00","confirmations":31,"totalForged":"500000000"}],"count":1934}


        :return:
        """
        public_key = "0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4"
        try:
            last_forged = controllers.make_request(self.url, '/api/blocks', {"generatorPublicKey": public_key, "orderBy": "height:desc", "limit": 1, })
            return last_forged
        except TypeError:
            return False

    def __str__(self):
        return '{} - {}://{}:{}'.format(self.name, self.protocol, self.host, self.port)


class Delegate(object):
    def __init__(self, lisk_address):
        self.lisk_address = lisk_address
        self.name = "wannabe_rotebaron"
        self.rank = 160
        self.public_key = "0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4"

    def __str__(self):
        return 'Lisk Address:{} -Name:{} -Rank:{}'.format(self.lisk_address, self.name, self.rank)
