""" this is set of functions
"""


""" print_list : list print recursively"""

def print_list(list_data, level=0):
    for item in list_data:
        if isinstance(item, list) :
            print_list(item, level+1)
        else:
            for tabs in range(level):
                print("\t", end='')
            print(item)
