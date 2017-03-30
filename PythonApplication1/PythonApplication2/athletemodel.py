
import os
import pickle

from athletelist import AthleteList

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)



def get_coach_data(file_name):
        try:
            with open(file_name) as f_read:
                data = f_read.readline()

            data = data.strip().split(',')

            a = AthleteList(data.pop(0), data.pop(0), sorted(set([sanitize(each_t) for each_t in data])))

            return a

        except IOError as ioerr:
            print("IO Error: ", str(ioerr))
            return None


def put_to_store(files_list):
    all_atheletes = {}

    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_atheletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_atheletes, athf)

    except IOError as ioerr:
        print("File error (put_and_store):" + str(ioerr))

    return (all_atheletes)

def get_from_store():
    all_atheletes = {}

    try:
        with open('atheletes.pickle', 'rb') as athf:
            all_atheletes = pickle.load(athf)
    except IOError as ioerr:
        print("File error (get from store)" + str(ioerr))


    return (all_atheletes)


