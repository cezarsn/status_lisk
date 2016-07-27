import unittest
import models
import controllers

server_cezar = models.Server(protocol='http', host='openmindsro.ddns.net', port='7000', name='C Local', net='testnet')
ref_server = models.Server(protocol='https', host='testnet.lisk.io', port='443', name='testnet.lisk.io', net='testnet')

delegate_cezar = models.Delegate("wannabe_rotebaron")

delegate_cezar.get_delegate_info(server_cezar)

ref_server.get_block_height()
server_cezar.get_block_height()

server_cezar.get_last_forged(delegate_cezar)

server_cezar.get_status(ref_server)

"""56"""
block_difference = server_cezar.block_height % server_cezar.last_forged[0]

print("Delegate Status: {}".format(delegate_cezar))
print("Server status: status sync {}\n\t\t block height {} last forged {} with block difference {}".format(server_cezar.is_sync , server_cezar.block_height, server_cezar.last_forged[0], block_difference))

print("TestNet status: block height {}".format(ref_server.block_height))

