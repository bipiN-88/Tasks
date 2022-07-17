

class Blog:

    def about_blog(self):
        print("blog is a regularly updated web page generally in informal style")


class Health_Blog(Blog):

    def about_health_blog(self):
        print("blogs about health and medical topics")


class Travel_Blog(Blog):

    def about_travel_blog(self):
        print("blogs about experience, information on travels to different places")


class Personal_blog(Health_Blog, Travel_Blog):

    def about_peronal_blog(self):
        print("blog about individual person")


personal = Personal_blog()
personal.about_blog()
personal.about_travel_blog()
personal.about_health_blog()
personal.about_peronal_blog()


# Multiple_Inheritance: the Derived class inherits properties from two different base classes.