a = open( "DOITT_THEATER_01_13SEPT2010.csv" , "r" )
aRL = a.readlines()
a.close()

b = open( "zip_codes.csv" , "r" )
bRL = b.readlines()
b.close()

def listify( L ) :
    for i in L :
        p = L.index( i )
        L[ p ] = L[ p ].strip()
        L[ p ] = L[ p ].split( "," )
    return L

aL = listify( aRL )
bL = listify( bRL )

def loc2zip( w ) :
    for n in bL :
        if n[ 1 ] == w :
            return n[ 0 ]

"""
Theater: zip codes-col7, names-col1, addresses-col4
"""

def getN( loc , zipCode , name , address ) :
    zipcode = loc2zip( loc )
    for n in aL :
        if n[ zipCode ] == zipcode :
            print "The " + n[ name ] + " is located at " + n[ address ] + "."

# getN( "Lower East Side" , 7 , 1 , 4 ) prints 3 diff theaters 
