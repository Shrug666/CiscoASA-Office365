# CiscoASA-Office365
A python script which pulls the latest Office365 IP list from Microsoft's website and creates a text file with Cisco ASA object groups containing the IP addresses and subnets.

The script downloads the XML list from https://support.office.com/en-gb/article/Office-365-URLs-and-IP-address-ranges-8548a211-3fe7-47cb-abb1-355ea5aa88a2?ui=en-US&rs=en-GB&ad=GB.
Each Product is put into an object group and the object groups are collected in a group object called "MS_SUBNETS" Just reference "MS_SUBNETS" in your outbound ACL and it should allow all subnets. You can delete products groups from the resultant text file or edit the python script to put logic around "product.attrib['name']" and automatically filter the products you need.

I am by no means a python expert so the script may seem inelegant or kludgy but it gets the job done.

The script could easily be edited to work on other firewalls or routers such as Cisco ISR, Juniper SRXs or Vyatta/vyos routers. Just edit line 58 into the appropriate format for your device.
If you don’t want it to print to screen, comment out line 43.
