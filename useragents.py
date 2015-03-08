#!/usr/bin/env python
"""
Script takes the input file of a WSA access-logs and outputs all of the unique user agents seen in the log.
"""
__author__ = 'jbollinger'
import csv
import getopt
import sys

#initilize global variables
inputfile = ""
outputfile = ""
useragent = []

#Process command line arguments for input/output files
try:
     opts, args = getopt.getopt(sys.argv[1:],"hio:",["inputfile=","outputfile="])
except getopt.GetoptError:
    print 'useragents.py -i <inputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'useragents.py -i <inputfile>'
        sys.exit()
    elif opt in ("-i", "--inputfile"):
        inputfile = arg
    elif opt in ("-o", "--outputfile"):
        outputfile = arg

#If cli arguments are not given prompt to enter file names
if inputfile == "":
    inputfile = raw_input("Enter logfile name: ")

if outputfile == "":
    outputfile = raw_input("Enter output file name: ")

print 'Input file is ', inputfile
print 'Output file is ', outputfile
#Helper functions

#function removes duplicates from a list
def dedupe(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

#Attempt to open file if it exists.  If file does not exists quit and print error to screen.
try:
    with open(inputfile, 'rb') as csvfile:
        """Parse inputfile as a CSV using 'space' as a delimiter.  Each line of the file is read one line at a time.
         Each element in the row can be referenced independently
        """
        infile = csv.reader(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # skip the first five lines because they are headers
        for x in range(4):
            next(infile, None)
        for row in infile:
            if len(row) > 13:
                useragent.append(row[13])
except:
    print "Error. Input file name not valid"
    quit()

#removes duplicate useragents from the list
uniqueua = dedupe(useragent)

#prints the output to a file
try:
    with open(outputfile, 'wb') as output:
        for item in uniqueua:
            output.write(item)
except:
    print "Error. Output filename is not valid"
    quit()








