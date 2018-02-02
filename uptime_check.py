#!/usr/bin/env python
##################################################################
#Created by: Alvin Aguila Sosangyo
#
#Script quickly checks uptime of single server in the network
##################################################################
import subprocess

def main():
	server_name = raw_input("Input server or x to exit: ");
	if server_name == "x":
		exit
	else:
		subprocess.call([
			"ssh", server_name,
			"uname -a",
			"; ",
			"uname -n",
			"; ",
			"uptime"
		])
		main();
main();
