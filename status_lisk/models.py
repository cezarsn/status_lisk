import controllers



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
	try:
            block_heigh = controllers.make_request(self.url, 'api/loader/status/sync', "")['height']
            return block_heigh
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

