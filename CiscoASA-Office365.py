#!/usr/bin/python
#########################################################################
#                   *** Office365 Cisco Config ***                      #
# Author:  Nick Stebbens                                                #
# Date:    21/06/2017                                                   #
# Version: 1.1                                                          #
# Dependancies: Python 3.6                                              #
# Description:                                                          #
# Assembles new Cisco ASA network objects containing Microsoft          #
# office365 IP addresses populated using the latest XML list            #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright 2017 Nicholas Stebbens                                      # 
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#########################################################################

import xml.etree.ElementTree as etree
import urllib.request
import ipaddress
import os

# opening url and loading it into the parser.
xmlurl = 'https://support.content.office.net/en-us/static/O365IPAddresses.xml'
dl = urllib.request.urlopen(xmlurl)
tree = etree.parse(dl)
dl.close()

outputfile = "office365_cisco_config.txt"

if os.path.isfile(outputfile): # Remove existing file
    os.remove(outputfile)

def output(text): #function to output to a file and the screen
    with open(outputfile,'a') as file:
        file.write(text+"\n")
        print(text)
        file.close()

prodlist = [] #Initalise empty array for productlist

for product in tree.getroot(): # find the root of the tree and iterate of products (children)
    for addresslist in product: #iterate over addresslists (grand children)
        if addresslist.attrib['type'] == "IPv4": # Match only IPv4 addresslists
            if not addresslist: # check for empty addresslists (currently ex-fed is empty) and move to next iteration
                break
            output("object-group MS_SUBNET-"+product.attrib['name'])
            output("description updated: "+tree.getroot().attrib['updated'])#Add a description including the date it was last updated
            prodlist.append("MS_SUBNET-"+product.attrib['name'])
            for address in addresslist: #iterate over addresses (great grand children)
                ipnet = ipaddress.ip_network(address.text)# pass the address text to ipaddress module
                output("network-object host "+str(ipnet.network_address)+" "+str(ipnet.netmask))# print IP and netmask in appropriate format

output("object-group MS_SUBNETS")
for prod in prodlist:
    output("group-object "+prod)
