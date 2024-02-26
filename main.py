import requests # ! Dont touch
import time # ! Dont touch

interval_minutes = 10 # ! [1: minutes is default]
# channel_id = '1204410642195284000' # ! Channel ID TESTING
channel_id = '1168221495147892816' # ! Channel ID Cps Promote World

def send_message():
  payload = {
    'content': '''
=========================
# FREE BFG POG - ALWAYS PTHT
#   >> BFGLLN <<
> - CHEAP LRAY, RAYMAN, AND LSS
> - CHEAP UWS, ARROZ, AND CLOVER
> - TONS STOCK DAILY PTHT
# FREE BFG POG - ALWAYS PTHT
#   >> BFGLLN <<
=========================

---------------------
  Auto Post By @Toy
---------------------
    '''
  }

  header = {
    'Authorization': 'ODk4NDA2MTA1NzYyMzk4MjM5.GOZ4Bh.Ys_COMmQus6EovL_B9qstCbWJm99XjxT5pLR2U'
  }

  r = requests.post("https://discord.com/api/v9/channels/" + channel_id + "/messages", data=payload, headers=header)
  print("Message successfully sent to Discord")

while True:
  send_message()
  time.sleep(interval_minutes * 60)
