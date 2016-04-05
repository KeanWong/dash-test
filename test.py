import datetime

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def button_pressed_dash1():
  current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
  print 'Dash button pressed at ' + current_time

def udp_filter(pkt):
  options = pkt[DHCP].options
  for option in options:
    if isinstance(option, tuple):
      if 'requested_addr' in option:
        # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
        mac_to_action[pkt.src]()
        break


mac_to_action = {'74:c2:46:4a:52:af' : button_pressed_dash1}
mac_id_list = list(mac_to_action.keys())

print "Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)

if __name__ == "__main__":
  main()