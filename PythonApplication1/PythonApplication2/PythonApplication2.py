

import os


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)


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


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times= []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend ( a_times)

    def get_top3(self):
        return self[0:3]

        

def get_data2(file_name):
    try:
        with open(file_name) as f_read:
            data = f_read.readline()

        data = data.strip().split(',')

        a = AthleteList(data.pop(0), data.pop(0), sorted ( set ( [sanitize(each_t) for each_t in data])) )
                        
        return a
        
    except IOError as ioerr:
        print("IO Error: ", str(ioerr)  )
        return None
                


r_james = get_data2("james2.txt")
#julie = get_data("julie2.txt")
#sarah = get_data("sarah2.txt")
#mikey = get_data("mikey2.txt")
#s = get_data("s.txt")


print (r_james.name, r_james.dob, r_james.get_top3())

#print (julie)
#print (sarah)
#print (mikey)


