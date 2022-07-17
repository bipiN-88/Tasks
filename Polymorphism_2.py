import logging
logging.basicConfig(filename="task_log.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Software_Developer:

    logging.info("we are in software_developer class")
    def work_profile(self):
        return "write code to develop software"

    def software_work(self):
        return " work on framework, technology and IDE"

    def head_profile(self):
        return "tech lead is the head of the project-development"


class Software_Tester:

    logging.info("we are in software_tester class")

    def work_profile(self):
        return "testing of execution of the code on different test sets "

    def software_work(self):
        return " work on automation framework"

    def head_profile(self):
        return "test lead is the head of the testing a project-development"

def check_work_profile(engineer):
    return engineer.work_profile()


developer = Software_Developer()
tester = Software_Tester()

print(check_work_profile(developer))
print(check_work_profile(tester))


