def loc2zip( w ) :
  # n[ 1 ] is the column of towns in the zip_codes.csv file. n[ 0 ] is the column of zip codes
    for n in bL :
        if n[ 1 ] == w :
            return n[ 0 ]
