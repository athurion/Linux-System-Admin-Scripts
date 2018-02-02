#!/usr/bin/env python
##################################################################
#Created by: Alvin Aguila Sosangyo
##################################################################
import subprocess

serverName = raw_input("Input Server: ");


#objects containing


#This part executes the command
df = subprocess.Popen([
    "ssh", "-q", serverName,
    "df",
    "-h",
    "/files0"
    ], stdout = subprocess.PIPE)
dfout = df.stdout.read()

print """
Hi,

Kindly check and perform cleanup on.

%s

""" % (dfout)

fileAppend = open("diskSpaceNotify.txt", "wb")
fileAppend.write(dfout);


subprocess.call(["cat", "diskSpaceNotify.txt", " | mailx", "sus.oc.onshift.unix@accenture.com"])


fileAppend.close()

