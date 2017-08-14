# CiscoASA-Office365
A python script to which pulls the latest Office365 IP list from Microsoft's website and creates Cisco ASA object groups containing the IP addresses.

The script downloads the XML list from https://support.office.com/en-gb/article/Office-365-URLs-and-IP-address-ranges-8548a211-3fe7-47cb-abb1-355ea5aa88a2?ui=en-US&rs=en-GB&ad=GB.

I am by no means a python expert so the script may seem inelegant or kludgy but it gets the job done.

The script could easily be edited to work on other firewalls or routers such as Cisco ISR, Juniper SRXs or Vyatta/vyos routers. Just edit line 58 into the appropriate format.
If you don’t want it to print to screen, comment out line 43.
