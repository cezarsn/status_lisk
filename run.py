#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

from status_lisk import app
app.secret_key = '\x02\x07A\xec\xd6\xe0\xbe\xcb\xcf\x001\xab+g\x1a\xef^\xef\xeb\x91,\xe4!\r'


import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/status_lis/status_lisk/")

app.run(debug = True)
