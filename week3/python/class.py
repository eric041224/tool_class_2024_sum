class People:
    def __init__(self,name,age): #构造函数
        self.name = name
        self.age = age

class Student(People):
    def __init__(self,name,age,number,grade): #构造函数
        super().__init__(name,age) 
        self.number = number
        self.grade = grade
    def showStudent(self):
        print("姓名："+self.name+" 年龄："+self.age+" 学号："+self.number+" 年级："+self.grade)

wang = Student("小王","14","1","9") #对象的初始化
wang.showStudent()