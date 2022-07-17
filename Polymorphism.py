import logging
logging.basicConfig(filename= 'polymorph_task.log', level= logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')


class employee:

    def __init__(self, name, age, expe):        # expe - exprience and type - category of the employee
        try:
            self.name = name
            self.age = age
            self.expe =expe
            logging.info("we are in init function of the employee")

        except Exception as e:
            logging.exception(e)


    def cal_salary(self):
        logging.info("we are in the cal_salary function of employee class")
        pass

class Manager(employee):

    def cal_salary(self):
        logging.info("we are in the cal_salary function of manager class")
        try:
            salary = 100000* self.expe

        except Exception as e:
            logging.exception(e)
        return salary


class Staff(employee):

    def cal_salary(self):
        logging.info("we are in the cal_salary function of staff class")
        try:
            salary = 1000* self.age

        except Exception as e:
            logging.exception(e)

        return salary

try:
    s= Staff("Navin", 45, 5)
    m = Manager("Ravi", 35, 3)
    print(s.cal_salary())
    print(m.cal_salary())
    logging.info("initializing the object class and calling salary function")
except Exception as e:
    logging.exception(e)

# polymorphism : where same function bevave differently inside and outside of the class.