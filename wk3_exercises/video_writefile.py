# VIDEO NOTES
from adodbapi.examples.xls_read import filename
from setuptools.command.egg_info import egg_info

#open 'w' if exists clears file data
#open 'w'  if doesn't exist, python creates file.
# 'a' append, to add to file. eg log file

# use print to write to filename
# eg.
# name = input("Name: ")
#out_file = open("name.txt", "w")
#print(name, file=out_file)
#out_file.close()
# OR  ^ .
# out_file.write(s)             write 's' to  file
# out_file.writelines(lines)    write list of strings one at a time to file

# use seek to move around file to read/write  not normally used
# shortcut instead of open/close, use WITH
# with open("     dfvdg", "w") as out_file:    opens and closes. indent below with
#       line = in_file.readline()
# OPEN/CLOSE in function
# use other functions to open/close

#CSV comma seperated variables ","








