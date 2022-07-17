import logging
logging.basicConfig(filename= 'task_log.log', level= logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

class ineuron_course:

    def course_details(self):
        print("we are in ineuron-course class")
        logging.info("ineuron_course class")


class ML(ineuron_course):

    def course_details(self):
        print("we are enrolled in machine learning course")
        logging.info("ML class")

class AI(ineuron_course):

    def course_details(self):
        print("we are enrolled in artificial intelligence course")
        logging.info("AI class")

class full_stack(ML, AI):

    def course_details(self):
        print("we are enrolled full stack data science course")
        logging.info("Full stack class")

a = full_stack()
b = AI()
a.course_details()
b.course_details()
print("this is the example of method over-riding")


# Method overriding - Where the inherited method of parent class is modified as per need in the child class.