

class Blog:

    def blog_handler(self):
        print("Blog-Handler: These can be handled based on the discretion of the owner")


class Business_Blog(Blog):

    def business_blog_handler(self):
        print("Business-Blog-Handler: These are handled by teh marketing team of an enterprise")


class CEO_Blog(Business_Blog):

    def ceo_blog_handler(self):
        print("CEO-Blog-Handler: These are handled by CEO of any enterprise")


ceo = CEO_Blog()
ceo.blog_handler()
ceo.business_blog_handler()
ceo.ceo_blog_handler()


# Multilevel inheritance- where behavior of parent class is inherited by child class and child class by its derived class so on