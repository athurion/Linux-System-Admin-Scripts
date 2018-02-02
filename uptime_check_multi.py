#!/usr/bin/env python
##################################################################
#Created by: Alvin Aguila Sosangyo
#
#Script will check uptime of multiple servers in the network
#How to use?
# 1. Input list of servers at list_servers.txt
# 2. Run the script
##################################################################
import subprocess

fo = open("list_servers.txt", "r")
str = fo.read().split();
for i in str:
	subprocess.call([
		"ssh", "-q", i,
		"uname -a",
		"; ",
		"uname -n",
		"; ",
		"uptime"
	])
fo.close()
