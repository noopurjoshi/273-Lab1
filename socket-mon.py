from __future__ import print_function
import psutil
import re, sys
from itertools import groupby
import csv

listOfSortedConnections = sorted(psutil.net_connections(), key=lambda pid: pid[6])

print ("\"pid\",\"laddr\",\"raddr\",\"status\"", end="\n")
for pid, connections in groupby(listOfSortedConnections, lambda pid: pid[6]):
    for connection in connections:
        if connection[5] != 'NONE' and connection[3] and connection[4] :
		print ("\"%s" % (connection[6]), end="\",")
		print ("\"%s@%d" % (connection[3]), end="\",")
		print ("\"%s@%d" % (connection[4]), end="\",")
		print ("\"%s" % (connection[5]), end="\"\n")