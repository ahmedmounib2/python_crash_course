# exc 10-3


exc10_file = 'exct10_file.txt'
name = input('whats your name?:  ')
with open(exc10_file,'w') as file_object:
    file_object.write(name)



# solving 10-3 with importing Path from pathlib

from pathlib import Path

path = Path('exc10-3Guest.txt')

path_name = input('whats your name again? ')
path.write_text(path_name)


