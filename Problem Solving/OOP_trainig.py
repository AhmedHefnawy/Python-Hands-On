from datetime import date


class Students:
    """ Class Students will be the main class that show the information about the extends classes and working in oop Arch !!"""
    departemnt = "general"
    bounus_ = 57  # class variable
    fu_marks_ = 1000
    sid = 0

    def __init__(self, fname, lname, age, marks): # self : tell the python where to look at o computer memeory
        """ __init__ method is a Regular method Pass III inistance >  as the first argument (SELF....)
            but it actually work every time we create a inestance opr using the class
        """
        self.fname = fname
        self.lname = lname
        self.age = age
        self.marks = marks

    # ======================================================================================================================
    @classmethod
    def byBirthYear(cls, fname, lname, year, marks):
        """
        class method can access and modify the state of the class ,,
        pass the class #cls as the first argument
        Call it by Class name !NOT instance name !!
        """
        return cls(fname, lname, date.today().year - year, marks)  # >>> Modify the state and act like __init__ method

    # ======================================================================================================================
    @staticmethod
    def isAdult(age):
        """
        static method know nothing about the class state and it cant change any thing or access to anything in the class ,
        NO Pass (self or cls ) >As parameters :) <><<<><><><>
        it pass any utility arguments not [Class or object ],,
        call it by Class and instance name BOTH $$$$ ....
        """
        if age > 30:
            print("Student State is : Accepted , His Age is {}".format(age))
        else:
            print("Student State is : Rejected , His Age is {} He Have to wait more {} years".format(age, 30 - age))

    @staticmethod
    def isAdultByYear(year):
        if (date.today().year - year) < 1990:
            print("Student State is : Accepted , His Birth Year is over 1990")
        else:
            print("Student State is : Rejected , His birth Year is {} ".format(year))

    # ======================================================================================================================

    def print_info(self):
        """ Regular method Pass III inistance >  as the first argument (SELF....)  """
        Students.sid += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nSitudrnt ID :{}".format(
            Students.sid))
        print(
            'Student Name :{} '
            '\nStudent Departement : {}'
            '\nStudent Age :{} '
            '\nStudent Lvl :{} '
            '\nStudent Marks :{} '
            '\nStudent Bounus :{} '
            '\nStudent UP-Bounus :{} '
            '\nStudent Final Degree :{} %'
            '\n ^^^^^^^^^^^^^'.format(

                self.fname + " " + self.lname,
                self.departemnt,
                self.age,
                self.age - 6,
                self.marks,
                self.bounus_,
                self.marks + self.bounus_,
                ((self.marks + self.bounus_) / self.fu_marks_) * 100))


# ========================================Working in main CLass======================================================
"""                Working in oop class                 """

Student_1 = Students("Ahmed", "Mohamed Hefnawy ", 35, 794)
Student_1.print_info()
Student_1.isAdult(35)

Student_2 = Students("Osama", "Ali Kasem ", 25, 666)
Student_2.bounus_ = 30
Student_2.print_info()
Student_2.isAdult(25)

Student_3 = Students.byBirthYear("Zeiad", "Hamdy Eid ", 1989, 852)
# Student_3 = Student_3.byBirthYear("Zeiad" , "Hamdy Eid " , 1998 , 852 ) # >>> you cant call class method by instance name EVER !!
Student_3.bounus_ = 80
# Students.isAdultByYear(1998)        #  >>> you can call static by the both ways
Student_3.print_info()
Student_3.isAdultByYear(1998)

Student_4 = Students.byBirthYear("Zeiad", "Hamdy Eid ", 1992, 768)
# Student_3 = Student_3.byBirthYear("Zeiad" , "Hamdy Eid " , 1998 , 852 ) # >>> you cant call class method by instance name EVER !!
Student_4.bounus_ = 70
# Students.isAdultByYear(1998)        #  >>> you can call static by the both ways
Student_4.print_info()
Student_4.isAdultByYear(1992)

print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n$$$$$$$$$$$$$$$$$$$$$$$$$$$ >>>>>>>>>>>>>>>>>> Inheritance A Sub Class <<<<<<<<<<<<<<<<<<<< $$$$$$$$$$$$$$$$$$$$$$$$$$")


class Developer(Students):
    departemnt = "SW Egineering"
    dev_ID = 0

    def __init__(self, fname, lname, age, marks, prog_lang):
        super().__init__(fname, lname, age, marks)
        self.prog_lang = prog_lang

    def print_Dev_info(self):
        """ Regular method Pass III inistance >  as the first argument (SELF....)  """
        Developer.dev_ID += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDeveloper ID :{}".format(
            Developer.dev_ID))
        print(
            'Developer Name :{} '
            '\nDeveloper Departement : {}'
            '\nDeveloper Age :{} '
            '\nDeveloper Lvl :{} '
            '\nDeveloper Marks :{} '
            '\nDeveloper Bounus :{} '
            '\nDeveloper UP-Bounus :{} '
            '\nDeveloper Final Degree :{} %'
            '\n ^^^^^^^^^^^^^'.format(

                self.fname + " " + self.lname,
                self.departemnt,
                self.age,
                self.age - 6,
                self.marks,
                self.bounus_,
                self.marks + self.bounus_,
                ((self.marks + self.bounus_) / self.fu_marks_) * 100))


# ========================================Working in Sub CLass======================================================
Dev_1 = Developer("Aliaa", "Osama", 27, 666, "python")
Dev_1.print_Dev_info()

Dev_2 = Developer("Islam", "Mohamed", 33, 782, "java")
Dev_2.print_Dev_info()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      "$$$$$$$$$$$$$$$$$$$$$$$$$$$ >>>>>>>>>>>>>>>>>> Multiple Inheritance <<<<<<<<<<<<<<<<<<<< $$$$$$$$$$$$$$$$$$$$$$$$$$")


class Manager(Developer):
    mgr_ID = 0

    def __init__(self, fname, lname, teamName, developers=None):
        self.fname = fname
        self.lname = lname
        self.teamName = teamName
        if developers is None:
            self.developers = []
        else:
            self.developers = developers

    def add_Developer(self, dev):
        if dev not in self.developers:
            self.developers.append(dev)

    def remove_dev(self, dev):
        if dev not in self.developers:
            self.developers.append(dev)

    def print_mgr_info(self):
        Manager.mgr_ID += 1
        print(" ^^^^^^^^^^^^^\nManager ID :{}"
              "\nManager name :{}"
              "\nTeam name :{}".format(
            self.mgr_ID,
            self.lname + " " + self.fname,
            self.teamName)
        )
        for dev in self.developers:
            print("Team Leader :{}".format(dev.fname + " " + dev.lname))

    """working in Dander methods >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|||| """

    def __repr__(self):
        """" ++++++++ Magic_Dunder Method (SELF) ||||
        __repr__ >> using for changing how the objects and instance are printed and display
        __ str__  >> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        return "\n<<<<<<< Print MANAGER INF __repr__() Dunder Method >>>>>>>>>>>>\n*** Manager Inf *** \n ID :{} \n NAME :{} \n TEAM LEADER :{}\n".format(
            self.mgr_ID, self.fname + self.lname, self.teamName)

    def __str__(self):
        """" ++++++++ Magic_Dunder Method (SELF) ||||
        __repr__ >> using for changing how the objects and instance are printed and display
        __ str__  >> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        return "\n<<<<<<< Print MANAGER INF __str__() Dunder Method >>>>>>>>>>>>\n*** Manager Inf ***\n ID :{} || NAME :{} || TEAM LEADER :{}".format(
            self.mgr_ID, self.fname + self.lname, self.teamName)

    def __add__(self, other):
        """" ++++++++ Magic_Dunder Method __add__(SELF , OTHER) ||||
                __add__ >> using to make an Arth operation with two objects and return the value you want
                int + int ,, Strings Concatination ,,,, or any addition operation you want
                """
        return "\nThe compination between the two Instance IDs\n >>>> is:{}".format(self.mgr_ID + other.mgr_ID)

    def __len__(self):
        """" ++++++++ Magic_Dunder Method __len__(SELF) ||||
        __len__ >> using to return the length of the parameter you pass from instance :)
        """
        return "_________Dunder____len()_______Method________\n>>>>> the length of team name is {} ".format(
            len(self.teamName))


# ========================================Working in Sub CLass======================================================

mgr_1 = Manager("HOSAAM", "KAMEL", "AI TEAM", [Dev_2])
mgr_1.print_mgr_info()
mgr_2 = Manager("Asmaa", "Tark", "Data Science TEAM", [Dev_1])
mgr_2.print_mgr_info()

print(mgr_1.__repr__())
print(mgr_1.__str__())
print(mgr_1 + mgr_2)  # the __add__ dander method is called Automatically , its a Dander __method__ :)
print(mgr_2.__len__())


# ==================================================================================


class DataSciences():
    DataSc_ID = 0
    department = "Machine Learning"
    bounus_ = 90  # class variable
    fu_marks_ = 1000

    def __init__(self, F_name, L_name):
        self.f_name = F_name
        self.l_name = L_name

    """ @property allow me to access the function as variable without using () and passing the value that will be affect in the class or instance state 
    """

    @property
    def email(self):
        return '{}.{}12356@yahoo.com'.format(self.f_name, self.l_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.f_name, self.l_name)

    @fullname.setter
    def fullname(self, flname):
        """
           @fullname.setter allow me to access fullname(self) and passing the value in it ,, to maka effect in instance state
        """
        f_name, l_name = flname.split(' ')
        self.f_name = f_name
        self.l_name = l_name\


DS_1 = DataSciences("Ahmed", "hefnawy")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(DS_1.f_name)
print(DS_1.l_name)
print(DS_1.fullname)
print(DS_1.email)
print("\n")
DS_1.fullname = 'MahOuD HamAdA'
print(DS_1.f_name)
print(DS_1.l_name)
print(DS_1.fullname)
print(DS_1.email)

class Networks():
    Net_ID = 0

    def __init__(self , **kwargs):
        self.Data = kwargs

    Net_ID += 1

    def printInf(self):
        print("Test...\n",self.Data)
net_1 = Networks(name="Fadwa" , Departement = "IT" , Level = 1)
net_1.printInf()











