Hacking an Amazon Dash
===
There are a few references on the internet to the method of sniffing ARP packets on your network to detect if a Dash button has been pressed.
 For some unknown reason, I wasn't able to see ARP requests from the Dash, however I was able to capture the Dash doing DHCP requests using BOOTP over UDP.

The Dash stays asleep (and off of your Wifi network) until its button is pressed.
When the Dash buton is pressed, it wakes up, connects to your WiFi network (including doing a DHCP request), and attempts to communicate with Amazon to order the product.

The Dash makes two UDP requests as part of the DHCP/BOOTP process, the second of which is after the Dash is assigned an IP address.
 Both UDP requests include the Dash's ethernet MAC ID, however because multiple UDP requests are issued, queueing off of any UDP packet with a specific MAC address would result in triggering twice for each Dash button press.
 Detecting this second UDP packet and extracting the IP address is validation that the Dash button has been pressed once and once only.

The Dash does not issue additional requests if the button is pressed while the Dash is still awake from a prior button press.
You need to wait until the white LED stops blinking, then the red LED (indicating that the intended product purchase failed) goes away until you can press the button again.

Note: my setup was all on Mac OSX 10.11.3 (El Capitan), using virtualenv with python 2.7.11.
 Setting up scapy in this environment was a PITA (pain in the ass), just google `scapy osx` and follow the most recent instructions.

Setting Up Your Dash
---
Follow the instructions from Amazon on how to pair the Dash **but when it asks you to choose a product, do NOT choose a product to order.**

(On iOS) I was getting spammed by Amazon that my Dash wasn't completely set up whenever I pushed the Dash button, so an onfortunate side effect of this hack is that I had to turn off iOS notifications for the Amazon app to prevent getting spammed _every single time the button was pressed_.  Amazon - it'd be great if you allowed hackers to turn that off in some preference...

