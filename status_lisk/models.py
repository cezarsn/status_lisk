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
        block_heigh = controllers.make_request(self.url, 'api/loader/status/sync', "")['height']
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

