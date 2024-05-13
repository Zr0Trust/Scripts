#!/bin/python3

import subprocess 
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an Interface, refer to --help for more info.")
	elif not options.new_mac:
		parser.error("[-] Please specify a new MAC Address, refer to --help for more info.")
	return options
	
def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_mac(interface):	
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

	if mac_search_result:
		return mac_search_result.group(0)
	else:
		print("[-] Could not read MAC Address")

options = get_arguments()

current_mac = get_mac(options.interface)
print(f"Current MAC = {current_mac}")

change_mac(options.interface, options.new_mac)

current_mac = get_mac(options.interface)
if current_mac == options.new_mac:
 	print(f"[+] MAC Address was succesfully changed to {current_mac}")
else:
 	print("[-] MAC Address did not get changed")

