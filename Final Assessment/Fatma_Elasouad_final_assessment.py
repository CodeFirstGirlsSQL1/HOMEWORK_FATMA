"""
TASK 1

# Design a parent class called CFGStudent.

# It should have general attributes like name, surname, age, email, student id
# and methods to fetch student’s full name and student’s id.

# Design a child class called NanoStudent, which  inherits from CFGStudent class.
# This class should have exactly the same attributes as its parent class,
# as well as an additional one called ‘specialization’ and course grades.

# The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
# in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
from random import randrange


class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        """ 
            initializer method for CFGStudent class
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id() if student_id == None else student_id

    @staticmethod
    def generate_id():
        """ 
            creates a random new id, which is any number between 1,000 and 10,000 and 
            returns id as a string
        """
        return str(randrange(1000, 10000))

    def get_id(self):
        """ 
            return the student objects id 
        """
        return self.student_id

    def get_fullname(self):
        """
            returns the full name of the student i.e. first name + surname
        """
        return self.name + " " + self.surname

class NanoStudent(CFGStudent):

    def __init__(self, specialization, **kwargs):
        """ 
            initializer method for NanoStudent class
            inherits from CFGStudent with keyword arguments 
        """
        super().__init__(**kwargs)
        self.specialization = specialization
        self.course_grades = dict()

    @staticmethod
    def generate_id():
        """ 
            creates a random new id, which is a word NANO followed by any number between 1,000 and 10,000 and 
            returns id as a string
        """
        return "NANO" + str(randrange(1000, 10000))

    def add_new_grade(self, course, grade):
        """ 
            adds/updates the course and the grade to the student's course_grades dictionary
        """
        self.course_grades[course] = grade

    def get_course_grades(self):
        """ 
            returns the current courses and grades taken by the student held in the course_grades attribute
        """
        return self.course_grades

#### TESTS ####

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}

"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

def fib(n):
    """
        method to find the fibonnaci sequence of n numbers
    """
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)

def even_fibonacci_sum(limit):
    total = 0
    for i in range(0, limit):
        # as a recursive function it will have multiple return statements as the method
        # recursively returns values;
        # so we check every returned value of the sequence to see if it a even and if so
        # then add it to our total
        if fib(i) % 2 == 0:
            total += fib(i)
    return total

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""
"""
    Fatma's Note: I have attempted this questions in two ways, the first way is the 
    most natural way to me, where i just check if the sequence number is in the array, but 
    this method seemed not to be the approach i should be taking upon reading the question properly.
    so attempted it another way using a while loop with a position flag to compare each 
    number in the sequence arr to the numbers in main array, only breaking when i've found it 
    or ending the whole function if one value of the sequence has not been found in any value 
    of the main array
"""

# 1st attempt at the question:
# def is_valid_subsequence(arr, seq):
#     for num in seq:
#         if num not in arr:
#             return False
#     return True


# 2nd attempt at the question:
def is_valid_subsequence(arr, seq):
    """
        method to find if the second array is a subsqeuence of the first array

    """
    pos = 0
    # while we loop through the main array, we only stay in the while loop for the duration
    # of the seq array length
    while pos < len(seq):
        # check if the value im evaluating in the seq array is in the main array
        found = False
        for num in arr:
            if seq[pos] == num:
                # if the seq value is equal to a value in the main array then break
                # and start checking the enxt seq value
                found = True
                break
        if found == False:
            # if after checking the whole array and one of the values haven't been found
            # then there is no point in moving the position flag and starting the loop again
            # and so we return False here
            return False
        # we move the position flag on the basis that the value in the seq is also found in
        # the main array and repeat the process on the next value
        pos += 1
    return True


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""


"""
REVIEW:
    SOLID - i dont remember exactly what the letters all stand for, but i remember the gist of the principles 
    - single responsibility: This class should be used to represent an employee, and classes are made up 
    out of attributes that describe the object and methods that represent the actions and behaviours or responsibilties 
    they can exhibit. that being said, upon reviewing the Employee class, it is confusing that we are passing through 
    a database engine into the class and setting it as part of the attributes, as OOP dictatecs, objects should represent 
    the object as they are and how they interact with each other, and so it is with that understanding that i would recommend 
    that the database should be its own class, and the employee is a class within its own right, and they interact with each other 
    to be able to save the employee information into the database, or to remove the employee from the databaase 
        - i.e. the saving and removing the employee data from the database is a behaviour expected of a database class not an 
        employee class, and the data or information is asociated with the employee class itself and so it should 
        remain there with some access methods to allow the database method to access the employee information 
    - behaviour:
        a print employee report function does not correctly represent what an employee is like in terms of the 
        behaviours expected of an employee. as it is a method that prints a report about that employee I would again expect 
        to see a report generator class or some admin class that will work to produce reports based on the emplyee objects that 
        is passed into it, i.e. the two objects interact with each other but the generation of the report is not a behaviour 
        i would associate with the employee  (SINGLE RESPONSIBILITY & INTEGRATION SEPERATION) 
    - writing to file:
        in the case of writing to the file, you can have not taken the necessary stepts to close 
        the file after finishing to write to file 
    - id and underscore:
        it looks like the incoming id is a number that should not be modified by a developer utilising this class, that
        should be denoted by an underscore '_id' and the self object attribute should showcase that too self._id = _id 
    - attribute access:
        ideally we would like some form of getter methods to allow for the outside world to access the attributes of the objects created
        to stop unintentional changing or modifying of the attributes directly, i.e. needs better encaspualation
    - comments:
        there aren't any comments in the code to explain what the methods do as docstrings so if i were to check the 
        documentation of the class, i would find little to no information, also some documentation for what the input 
        data types should be is needed to ensure no errors later on e.g. when saving to the database
    - error handling:
         in the print employee report function, the path to file is an open letter for all sorts of errors, such as a file not found or if the path points to a 
         file that isn't writable to etc. This method should have a try and except for these cases as it could occur. 
            - there are also no checks to see if the values that are to be written into the employee report are valid, i.e 
            there is no validation from the moment the class is constructed to when this method is called - so i could 
            create an employee class and pass in only 000000 as each argument and could still write to the file    
    - validation:
        on the mention of validation in the previous point, there isn't much data validation at all, however data types
        are important in saving to a database, as certain columns expect specific values of specific lengths sometimes. 
        therefore, there needs to be validations on the data passed in, but also try and except or some form of error
        handling in not only the print employee report but also the save employee, and the remove employee methods.  
"""







