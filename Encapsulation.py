import logging
logging.basicConfig(filename='task_log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Student:

    def __init__(self, name, age, course):

        logging.info("we are init function of the Student Class")
        try:
             self.name = name
             self.age = age
             self.course = course
             self.__grade = 'c'

        except Exception as e:
            logging.exception(e)

    def __repr__(self):
        logging.info("we are in the _repr function to print the attributes of the object")
        return  f"Name:{self.name}, Age:{self.age}, Course: {self.course}, Grade:{self.__grade}"

    def get_grades(self):
        return self.__grade

    def set_grades(self, grade):
        logging.info("we are set grade function to set the grade")
        self.__grade = grade
        return self.__grade


student1 = Student("Ravi", 20, "MI")
student2 = Student("Kailash", 21, "MI")

student1.__grades
student1.set_grades("A")
student2.set_grades("B")
print(student1)
print(student2)


# Encapsulation - which prevent access of the data by the user by declaring private variable and method.
# private variable are then accessed only vide public methods.