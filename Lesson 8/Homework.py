"""

Write  a  function  that  can  read  contents  of  a file  and
can  handle  cases  when  provided  file name does not exist:
- Handle  Error  cases  gracefully  displaying  an informative
message to the user.
- What  Error  type  can  we  use  here?
(check Python documentation)

"""
from os import path

def read_from_file(filename):
    try:
        if str(path.isfile(filename)):
            txt = open(filename, "r")
        else:
            raise IOError
    except IOError as err:
        print(filename + " is not a valid file! Please try again.")

read_from_file("hello.txt") # prints hello.txt is not a valid file! Please try again.

