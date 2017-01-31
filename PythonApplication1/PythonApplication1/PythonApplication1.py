


#from module1 import print_list
import module1

print("this is start.")

movies = ["the holy grail", "the life of brian", "the meaning  of life", ["nested item", ["again item"]]]


import os
print(os.getcwd())

#print_list(movies)
#module1.print_list (movies)


data = open("sketch.txt")
data.seek(0)

man = []
other = []

for each_line in data:
    try:
        (l_value, r_value) = each_line.split(":", 1)
        #print( l_value, end='')
        #print( " said: ", end="")
        #print( r_value, end='')

        r_value.strip()

        if( l_value == 'Man'):
            man.append(r_value)
        elif (l_value == "Other Man"):
            other.append(r_value)


    except:
        print(" exception:", each_line)
       
data.close()

try:
    out = open("data.out", "w")
    
    print("gogogo", file=out)
    print(man, file=out)
    print(other, file=out)

    

except IOError:
    pass

finally:
    out.close()


















