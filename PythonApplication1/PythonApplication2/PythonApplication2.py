

import os

from athletelist import AthleteList
from athletemodel import *


def get_data(file_name):
    try:
        with open (file_name) as f_open:
            data = f_open.readline()

        data = data.strip().split(',')

        #new_data = []
        #for each_t in data:
            # new_data.append(sanitize(each_t))

        new_data = sorted( set( [sanitize(each_t) for each_t in data]) )
        
        return new_data

    except IOError as ioerr:
        print("IO Error: ", str(ioerr)  )

        return None

r_james = get_coach_data("james2.txt")
print (r_james.name, r_james.dob, r_james.get_top3())

the_files =["james2.txt", "mikey2.txt", "julie2.txt", "sarah2.txt"]
data = put_to_store(the_files)

for each_ath in data:
    print(data[each_ath].name   + " " + data[each_ath].dob)


#print (julie)
#print (sarah)
#print (mikey)


