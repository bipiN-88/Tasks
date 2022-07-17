import logging
logging.basicConfig(filename="task_log.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


from abc import ABC, abstractmethod

class Onlineclass(ABC):

    def __init__(self):
        print("online class")

    @abstractmethod
    def duration(self):
        sprint("class duration is 12 hours")


class full_stack(Onlineclass):

    def __init__(self):
        print("full stack class")

    def duration(self):
        print("class duration is 3 hours")


fs = full_stack()
fs.duration()


#  abstraction - hiding of implementation part from the user.