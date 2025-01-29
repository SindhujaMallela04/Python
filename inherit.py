class Institution:
    def __init__(self):
        print("This is an Institution")
    
    def Teachers(self):
        print("There are teachers")
    
    def Students(self):
        print("There are students")

    def classrooms(self):
        print("There are classrooms")

class School(Institution):
    def __init__(self, name):
        self.__name = name

    def Teachers(self):
        print("There are 15 teachers in this school")
    
    def get_name(self):
        return self.__name

    def classes(self, classes):
        print(f"There are {classes} no. of classes in the school")

class College(Institution):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_depts(self):
        print("There are depts in the college")

class UG(College):
    def __init__(self, course_name):
        self.__course_name = course_name

    def get_course(self):
        return self.__course_name

    def get_depts(self):
        print("There are 5 depts in the UG course")

class PG(College):
    def __init__(self, course_name):
        self.__course_name = course_name

    def get_course(self):
        return self.__course_name

    def get_depts(self):
        print("There are 5 depts in the PG course")

list_of_schools = list(map(School, input("Enter the school names separated by spaces: ").split()))
for school in list_of_schools:
    print(school.get_name())






