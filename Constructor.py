import logging
logging.basicConfig(filename= 'task_log.log', level= logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

class ineuron:

    def __init__(self):
        print("i am currently enrolled in data-science course")
        logging.info("we are in ineuron-init funcion")


i = ineuron()


