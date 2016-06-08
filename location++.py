#!/usr/bin/python
print "Content-Type: text/html\n\n"

import cgi
import cgitb
cgitb.enable()

a = open( "DOITT_THEATER_01_13SEPT2010.csv" , "r" )
aRL = a.readlines()
a.close()

b = open( "zipcodeconverter.csv" , "r" )
bRL = b.readlines()
b.close()

def parseQuery():
    q=cgi.FieldStorage()
    d={}
    for key in q:
##        print str(key) + ": "
##        print q[key].value
##        print "<br>"
        d[key]=q[key].value
    return d

def listify( L ) :
    for i in L :
        p = L.index( i )
        L[ p ] = L[ p ].strip()
        L[ p ] = L[ p ].split( "," )
    return L

aL = listify( aRL )
bL = listify( bRL )

def theatre( loc , zipCode , name , address ) :
    zipcode = loc2zip( loc )
    found = False
    for n in aL :
        if n[ zipCode ] == zipcode :
            print n[ name ] + " is located at " + n[ address ] + "."
            found = True
    if found == False:
        print("Sorry, there are no theatres nearby your current location.")
            
"""
Theater: zip codes-col7, names-col1, addresses-col4
"""

def getN( loc , zipCode , name , address ) :
    zipcode = loc2zip( loc )
    for n in aL :
        if n[ zipCode ] == zipcode :
            print "The " + n[ name ] + " is located at " + n[ address ] + "."

# getN( "Lower East Side" , 7 , 1 , 4 ) prints 3 diff theaters
# for Lower East Side entertainment
    # params returns -> {'function': 'Entertainment', 'input': 'Lower East Side'}

#calls and returns the appropriate function based on given parameters
def chooseFunction():
    if params['function']=='Transportation':
        print("Under Construction")
    elif params['function']=='Entertainment':
        return getN(( params[ "input" ] ) , 7 , 1 , 4 )
    elif params['function']=='Educational Opportunities':
        print("Under Construction")
    elif params['function']=='Food':
        print("Under Construction")
    else: #just in case.
        return 'Unknown function.'

def printInfo():
    print '<h1>Function: ' + params['function'].capitalize() + '</h1>'
    print 'Input: ' + params['input'] + '<br>'

"""
def checkEnoughData():
    if 'function' not in params:
        print '<h1>Please select a function.</h1>'
    if 'input' not in params:
        print 'Please give an input.'
    if ('function' in params) and ('input' in params):
        printInfo()
        print 'Output: '+formatify(chooseFunction())
"""
print "<!DOCTYPE html><html>\n"

params=parseQuery()
print params , "<br>"
#checkEnoughData()
chooseFunction()
print "</html>"
