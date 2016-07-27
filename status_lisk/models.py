import controllers


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
        self.last_forged = 0
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

            self.last_forged =  last_forged['blocks'][0]["height"], last_forged['blocks'][0]["timestamp"]
        except TypeError:
            self.last_forged = -1

    def get_status(self, ref_server):
        """
        Return if the server is in sync with an ref_server
        """
        if (self.block_height % ref_server.block_height) < 10 or (self.block_height % self.last_forged) < 100:
             self.is_sync = True
        else:
            self.is_sync = False

    def is_forging(self, delegate):
        return False

    def update(self):
        self.get_block_height()



    def __str__(self):
        return '{} - {}://{}:{}'.format(self.name, self.protocol, self.host, self.port)


"""
http://openmindsro.ddns.net:7000/api/delegates/get?username=wannabe_rotebaron
{"success":true,"delegate":{"username":"wannabe_rotebaron","address":"16379340065696424247L","publicKey":"0348a623c41ed7742a7f35a5812476750e2ba41208e16a29b110e6fe11e514d4","vote":"85039088874255","producedblocks":2445,"missedblocks":902,"rate":78,"approval":0.84,"productivity":73.05}}

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
        username = self.username
        response = controllers.make_request(server.url, 'api/delegates/get', {"username": username})
        if response:
            self.address = response["delegate"]["address"]
            self.public_key = response["delegate"]["publicKey"]
            self.rate = response["delegate"]['rate']
            self.produced_blocks = response["delegate"]['producedblocks']
            self.missed_blocks = response["delegate"]['missedblocks']
            self.productivity = response["delegate"]['productivity']

    def __str__(self):
        return 'Lisk Address:\t{} - Name:\t{} - Rank:\t{}'.format(self.address, self.username, self.rate)
