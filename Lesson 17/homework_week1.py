"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

- Fatma:
    applying a discount: I've understood it as a discount that is stored in
        the cash register, like the ones I use at work at KFC, which is applied upon
        seeing the correct identification for it, e.g. Blue Light Card for NHS discount

"""


class CashRegister:

    def __init__(self):
        self.total_items = dict()  # {'item': 'price'}
        self.total_price = 0
        self.discount = {'NHS': 0.25, 'Employee_Discount': 0.10, 'Customer_Survey': 0.15}
        self.discount_applied = {"applied?": False, "type": None}  # key info regarding checking for discounts applied

    def add_item(self, item, price):
        # this will add the item to the total items, add the price to the total running price and print confirmation
        # that its added the item
        self.total_price += price
        self.total_items[item] = price
        print("Added {} .......... {}".format(item, price))

    def remove_item(self, item):
        # check if the item is within our total items, then remove, else warn the user
        if self.total_items[item]:
            self.total_price -= self.total_items[item]
            self.total_items.pop(item)
            print("Removed " + item + " from total items\n")
        else:
            print("This item hasn't been added yet!\n")

    # check if this discount is valid on this till
    def is_valid_discount(self, discount):
        return True if discount in self.discount.keys() else False

    # check if any discount is already applied
    def any_discount_applied(self):
        return self.discount_applied["applied?"]

    # update the state of the order to a discounted order, and what discount type
    def apply_discount_to_order(self, discount):
        self.discount_applied["applied?"] = True
        self.discount_applied["type"] = discount

    def apply_discount(self, discount):
        # check if we accept this discount and if they haven't already applied a discount
        if self.is_valid_discount(discount) and self.any_discount_applied() == False:
            for item, price in self.total_items.items():
                self.total_items[item] = price - (price * self.discount[discount])
            # set the system that the user has now applied a discount to their order and which one they used
            self.apply_discount_to_order(discount)
            print("Discount applied successfully")
        # in the case that they have already applied a discount
        elif self.any_discount_applied():
            print("Error discount already applied: Only one discount per transaction!")
        # in the case that we don't recognise this discount
        else:
            print("Sorry you can't use this discount")

    def get_total(self):
        # print the total price as well as the discount used if it's been applied
        if self.any_discount_applied():
            print('{:s}'.format('\u0332'.join('Total Price:')) + '{0:.2f}'.format(self.total_price) + '\n\033[1m' +
                  str(self.discount_applied["type"]) + " \x1B[3mDiscount Applied\x1B[0m\033[0m\n")
        # print total price in the case that no discount has been applied
        else:
            print('{:s}'.format('\u0332'.join('Total Price:')) + '{0:.2f}'.format(self.total_price) + "\n")

    def show_items(self):
        # prints the item and price formatted to be similar to a receipt
        print('{:s}'.format('\u0332'.join('Total items:')))
        for item, price in self.total_items.items():
            print(item + " .......... {0:.2f}".format(price))

    def reset_register(self):
        # reset all the key variables of the cash register to take the next customer order
        self.total_items.clear()
        self.total_price = 0
        self.discount_applied["applied?"] = False
        self.discount_applied["type"] = None
        print("Cash register reset successfully")


""" 

EXAMPLES AND OUTPUT

"""


# EXAMPLE code run:

# 1. create the cash register till
KFC_cash_register = CashRegister()

# 2. scan and add the items to the total items
KFC_cash_register.add_item('Zinger Meal', 4.99)
KFC_cash_register.add_item('Boneless Banquet', 6.49)
KFC_cash_register.add_item('Flaming Wrap', 1.49)
"""
output: 

Added Zinger Meal .......... 4.99
Added Boneless Banquet .......... 6.49
Added Flaming Wrap .......... 1.49

"""

# 3. check the total items and total price so far 
KFC_cash_register.show_items()
KFC_cash_register.get_total()

""" 
output:

T̲o̲t̲a̲l̲ ̲i̲t̲e̲m̲s̲:
Zinger Meal .......... 4.99
Boneless Banquet .......... 6.49
Flaming Wrap .......... 1.49
T̲o̲t̲a̲l̲ ̲P̲r̲i̲c̲e̲:12.97

"""

# 4. trying a different discount that we don't accept
KFC_cash_register.apply_discount("Armed Forces")

""" 
output:

Sorry you can't use this discount

"""

# 5. Add NHS discount to the order, then check the new price, and updated discounted item prices
KFC_cash_register.apply_discount('NHS')
KFC_cash_register.get_total()
KFC_cash_register.show_items()

""" 
output:

Discount applied successfully
T̲o̲t̲a̲l̲ ̲P̲r̲i̲c̲e̲:12.97
NHS Discount Applied

T̲o̲t̲a̲l̲ ̲P̲r̲i̲c̲e̲:12.97

T̲o̲t̲a̲l̲ ̲i̲t̲e̲m̲s̲:
Zinger Meal .......... 3.74
Boneless Banquet .......... 4.87
Flaming Wrap .......... 1.12

"""

# 6. trying a different discount that we don't accept
KFC_cash_register.apply_discount("Employee_Discount")

"""
output:

Error discount already applied: Only one discount per transaction!

"""

# 7. customer decides to remove one item
KFC_cash_register.remove_item('Zinger Meal')
KFC_cash_register.show_items()
KFC_cash_register.get_total()

"""
output:

Removed Zinger Meal from total items

T̲o̲t̲a̲l̲ ̲i̲t̲e̲m̲s̲:
Boneless Banquet .......... 4.87
Flaming Wrap .......... 1.12
T̲o̲t̲a̲l̲ ̲P̲r̲i̲c̲e̲:9.23
NHS Discount Applied

"""

# 8. Once the order is completed, reset the cash register till
KFC_cash_register.reset_register()

""" 
output:

Cash register reset successfully

"""

###############
# Second task #
###############

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def underline(self, string):
        # just a helper method to help format some printed output
        return "\u0332".join(string)

    def add_subject(self, subject):
        # add subject to the dictionary and set the grade to None
        self.subjects[subject] = None

    def remove_subject(self, subject):
        # remove the subject form subject list and the correlating grade
        if subject in self.subjects.keys():
            self.subjects.pop(subject)
            print("{} subject removed successfully from {}'s subjects".format(subject, self.name))

    def view_subjects(self):
        # number and list all registered subjects for this student if they are registered to any subjects
        if len(self.subjects) == 0:
            print("No subjects to display")
        else:
            print(self.underline("{}, ID: {} - Subjects: ".format(self.name, self.id)))
            for idx, subject in enumerate(self.subjects):
                print("{}. {}".format(idx + 1, subject))

    def view_grades(self):
        # number and view any subject they are registered to and the grade they have
        if len(self.subjects) == 0:
            print("No subjects to display")
        else:
            print(self.underline("{}, ID: {} - Grades Transcript: ".format(self.name, self.id)))
            for idx, subject in enumerate(self.subjects):
                # mark any None grades as ungraded
                grade = "Ungraded" if self.subjects[subject] is None else self.subjects[subject]
                print("{}. {} .......... {}".format(idx + 1, subject, grade))

    def add_grade(self, subject, grade):
        self.subjects[subject] = grade

    def update_grade(self, subject, grade):
        # does the same as add grade, specified method for usability and readability
        self.add_grade(subject, grade)


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#           - Fatma: I thought it made more sense that any student object should be able to add/remove subjects or
#                    add/update grades, so i moved this functionality to the student base object class

#     create a method to view all subjects taken by a student
#           - Fatma: I again felt that all student objects should be able to view any subjects they're registered in
#                    so i again moved this functionality to the student base class

#     create a method (and a new variable) to get student's overall mark (use average)


class CFGStudent(Student):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        self.overall_mark = None
        self.nanodegree_stream = None
        self.classmates = []

    def set_nanodegree_stream(self, stream):
        # only accept 'Software' or 'Data' as the stream input
        if stream.lower() == 'software' or stream.lower() == 'data':
            self.nanodegree_stream = stream
        else:
            print("Invalid input, please input 'Software' or 'Data' streams!")

    def get_stream(self):
        # displays the student's stream if it has been set
        if self.nanodegree_stream is None:
            print("Nanodegree stream not set, please set it first!")
        else:
            print(self.underline("{}, ID: {} - {} Stream".format(self.name, self.id, self.nanodegree_stream)))

    def get_overall_mark(self):
        # prints the average overall grade if any subjects have been taken with grades
        if len(self.subjects) == 0:
            print("This student has not taken any subjects yet!")
        else:
            total = 0
            no_of_subjects = len(self.subjects)
            no_of_graded_subjects = 0
            # only counts and averages the graded subjects out of all registered subjects
            for subject, grade in self.subjects.items():
                if grade is not None:
                    total += grade
                    no_of_graded_subjects += 1
            self.overall_mark = total / no_of_graded_subjects
            print("{}, ID: {} - Overall average mark for {} graded subjects out of {} total subjects: {}".format(
                self.name, self.id, no_of_graded_subjects, no_of_subjects, self.overall_mark))

    def add_classmate(self, classmate):
        # link students together and add to each others classmate list
        if self.nanodegree_stream == classmate.nanodegree_stream:
            self.classmates.append(classmate.name)
            classmate.classmates.append(self.name)
        else:
            print("Sorry, classmates must be in the same stream! Please add classmate from the {} stream.".format(self.nanodegree_stream))

    def view_classmates(self):
        # print and view all linked classmates of the same stream
        if len(self.classmates) > 0:
            print(self.underline("{}'s classmates:".format(self.name)) + " {}".format(self.classmates))
        else:
            print("No classmates added yet!")


""" 

EXAMPLES AND OUTPUT

"""

# 1. create a new student object
Fatma = CFGStudent("Fatma Elasouad", 26, 156172)

# 2. set the nanodegree_stream and add some subjects, and view them all
Fatma.set_nanodegree_stream("Software")
Fatma.add_subject("SQL foundation")
Fatma.add_subject("Python foundation")
Fatma.view_subjects()

""" 
output:

F̲a̲t̲m̲a̲ ̲E̲l̲a̲s̲o̲u̲a̲d̲,̲ ̲I̲D̲:̲ ̲1̲5̲6̲1̲7̲2̲ ̲-̲ ̲S̲u̲b̲j̲e̲c̲t̲s̲:̲ 
1. SQL foundation
2. Python foundation

"""

# 3. set the grades for the subjects
Fatma.add_grade("SQL foundation", 78)
Fatma.add_grade("Python foundation", 88)
Fatma.add_grade("Intro to programming", 90)

# 4. view the subjects and grades, and try removing a subject
Fatma.view_grades()
Fatma.remove_subject("Intro to programming")
Fatma.add_subject("Coding fundamentals")
Fatma.view_grades()

""" 
output:

F̲a̲t̲m̲a̲ ̲E̲l̲a̲s̲o̲u̲a̲d̲,̲ ̲I̲D̲:̲ ̲1̲5̲6̲1̲7̲2̲ ̲-̲ ̲G̲r̲a̲d̲e̲s̲ ̲T̲r̲a̲n̲s̲c̲r̲i̲p̲t̲:̲ 
1. SQL foundation .......... 78
2. Python foundation .......... 88
3. Intro to programming .......... 90
Intro to programming subject removed successfully from Fatma Elasouad's subjects
F̲a̲t̲m̲a̲ ̲E̲l̲a̲s̲o̲u̲a̲d̲,̲ ̲I̲D̲:̲ ̲1̲5̲6̲1̲7̲2̲ ̲-̲ ̲G̲r̲a̲d̲e̲s̲ ̲T̲r̲a̲n̲s̲c̲r̲i̲p̲t̲:̲ 
1. SQL foundation .......... 78
2. Python foundation .......... 88
3. Coding fundamentals .......... Ungraded

"""

# 5. see average overall mark
Fatma.get_overall_mark()

""" 
output:

Fatma Elasouad, ID: 156172 - Overall average mark for 2 graded subjects out of 3 total subjects: 83.0

"""

# 6. Create new Student
Aisha = CFGStudent("Aisha Saad", 24, 182359)

# 7. set the stream and add subjects
Aisha.set_nanodegree_stream("Software")
Aisha.add_subject("SQL foundation")
Aisha.add_subject("Python foundation")

# 8. set the grades for the subjects and view the grades
Aisha.add_grade("SQL foundation", 98)
Aisha.add_grade("Python foundation", 62)
Aisha.add_grade("Intro to programming", 88)
Aisha.view_grades()

""" 
output:

A̲i̲s̲h̲a̲ ̲S̲a̲a̲d̲,̲ ̲I̲D̲:̲ ̲1̲8̲2̲3̲5̲9̲ ̲-̲ ̲G̲r̲a̲d̲e̲s̲ ̲T̲r̲a̲n̲s̲c̲r̲i̲p̲t̲:̲ 
1. SQL foundation .......... 98
2. Python foundation .......... 62
3. Intro to programming .......... 88

"""

# 9. connect the students as classmates
Fatma.add_classmate(Aisha)

# 10. View classmates for the different students
Fatma.view_classmates()
Aisha.view_classmates()

""" 
output:

F̲a̲t̲m̲a̲ ̲E̲l̲a̲s̲o̲u̲a̲d̲'̲s̲ ̲c̲l̲a̲s̲s̲m̲a̲t̲e̲s̲: ['Aisha Saad']
A̲i̲s̲h̲a̲ ̲S̲a̲a̲d̲'̲s̲ ̲c̲l̲a̲s̲s̲m̲a̲t̲e̲s̲: ['Fatma Elasouad']

"""

# 11. create one more classmate
Rana = CFGStudent("Rana Masud", 23, 174902)
Rana.set_nanodegree_stream("Software")
Rana.add_grade("SQL foundation", 92)
Rana.add_grade("Python foundation", 99)
Rana.add_grade("Intro to programming", 93)
Rana.add_classmate(Fatma)
Rana.add_classmate(Aisha)

# 12. print the classmates
Fatma.view_classmates()
Aisha.view_classmates()
Rana.view_classmates()

""" 
output:

F̲a̲t̲m̲a̲ ̲E̲l̲a̲s̲o̲u̲a̲d̲'̲s̲ ̲c̲l̲a̲s̲s̲m̲a̲t̲e̲s̲: ['Aisha Saad', 'Rana Masud']
A̲i̲s̲h̲a̲ ̲S̲a̲a̲d̲'̲s̲ ̲c̲l̲a̲s̲s̲m̲a̲t̲e̲s̲: ['Fatma Elasouad', 'Rana Masud']
R̲a̲n̲a̲ ̲M̲a̲s̲u̲d̲'̲s̲ ̲c̲l̲a̲s̲s̲m̲a̲t̲e̲s̲: ['Fatma Elasouad', 'Aisha Saad']

"""

# 13. new CFG data students, set data stream and add subject and grades
Layan = CFGStudent("Layan", 25, 2893472)
Layan.set_nanodegree_stream("Data")
Layan.add_grade("SQL foundation", 92)
Layan.add_grade("Python foundation", 99)

# 14. try to add classmates from different stream
Layan.add_classmate(Fatma)

"""
output:

Sorry, classmates must be in the same stream! Please add classmate from the Data stream.

"""
