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

c = open( "subway.csv" , "r" )
cRL = c.readlines()
c.close()

d = open( "OEM_HurricaneEvacuationCenters_2015.csv" , "r" )
dRL = d.readlines()
d.close()

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
cL = listify( cRL )
dL = listify( dRL )

def loc2zip( w ) :
    for n in bL :
        if n[ 1 ] == w :
            return n[ 0 ]

def theatre( loc ) :
    zipcode = loc2zip( loc )
    found = False
    for n in aL :
        if n[ 7 ] == zipcode :
            print n[ 1 ] + " is located at " + n[ 4 ] + ". <br>"
            found = True
    if found == False:
        print("Sorry, there are no theatres nearby your current location.")

def subway( loc ) :
    zipcode = loc2zip( loc )
    found = False
    for n in cL :
        if n[ 8 ] == zipcode :
            print "The " + n[ 3 ] + " station is in your zip code. The " + n[ 4 ]$
            found = True
    if found == False:
        print "Sorry, there are no subway stations near your current location."

def hurricane( loc ) :
    zipcode = loc2zip( loc )
    found = False
    for n in dL :
        if n[ 5 ] == zipcode :
            print n[ 1 ] + " is a hurricane center in your area. It is located at$
            found = True
    if found == False:
        print "Sorry, there are no hurricane centers near your current location."

#calls and returns the appropriate function based on given parameters
def chooseFunction():
    if params['function']=='Transportation':
        print subway( params[ "input" ] )
    elif params['function']=='Entertainment':
        return theatre( params[ "input" ] )
    elif params[ 'function' ] == 'Safety Zones' :
        return hurricane( params[ "input" ] )
    elif params['function']=='Educational Opportunities':
        print("Under Construction")
    elif params['function']=='Food':
        print("Under Construction")
    else: #just in case.
        return 'Unknown function.'

def printInfo():
    print '<h1>Function: ' + params['function'].capitalize() + '</h1>'
    print 'Input: ' + params['input'] + '<br>'

HTML_HEADER = 'Content-type: text/html\n\n'
Top_HTML= '''
<html>
<head>
<title> Key to Success </title>
</head>
<body style="background: MediumSpringGreen;">
<center>
<p><font size="5" color="gray">
'''
Bottom_HTML='''
</p>
</center>
</body>
</html>
'''

params=parseQuery()
chooseFunction()
print HTML_HEADER + Top_HTML + "</p>" + str(chooseFunction()) + Bottom_HTML

