class  Student:
    def __init__(self,student_id,student_name,student_email):
        self.student_id=student_id
        self.student_name=student_name
        self.student_email=student_email

class Course:
    def __init__(self,course_id,course_name,course_duration):
        self.course_id=course_id
        self.course_name=course_name
        self.course_duration=course_duration

class Enrollment:
    def __init__(self,student,course):
        self.student=student
        self.course=course

class Enrollment_Services:
    # storage
    def __init__(self):
        self.students={}
        self.courses={}
        self.enrollments=[]
    # adding students
    def add_student(self):
        student_id=input("enter student  id : ")
        if student_id in self.students:
            print ("student already exists")
            return
        student_name=input("enter student name: ")
        student_email=input("enter student email: ")

        student=Student(student_id,student_name,student_email)
        self.students[student_id]=student
        print("student added sucessfully")

        #    ADDING COURSE

    def add_course(self):
        course_id=input("enter course id: ")
        if course_id in self.courses:
            print("course already exists")
            return
        course_name=input("enter course name: ")
        course_duration=input("enter course duration: ")
        course=Course(course_id,course_name,course_duration)
        self.courses[course_id]=course
        print("course added sucessfully")

        # ENROLL STUDENT 

    def enroll_student(self):
        student_id=input("enter student id :")
        if student_id not in self.students:
            print("student not found")
            return
        course_id=input("enter course id : ")
        if course_id not in self.courses :
            print("couse not found")
            return
        student=self.students[student_id]
        course=self.courses[course_id]
        self.enrollments.append(Enrollment(student,course))
        print("student enrolled succesfully in the course ")

#       REMOVE ENROLLEMENTS
    def remove_enrollment(self) :
        student_id=input("enter  student id : ")
        course_id =input("enter course id : ")
        for enrollment in self.enrollments:
            if enrollment.student.student_id==student_id and enrollment.course.course_id==course_id:
                self.enrollments.remove(enrollment)
                print("enrollment remove successfully")
                return
        print("enrollment not found")    


#       VIEW STUDENTS and COURSES
     
    def view_student_courses(self):
        student_id=input ("enter student id :")
        if student_id not in self.students:
            print("students not found")
            return
        for enrollment in self.enrollments:
            if enrollment.student.student_id==student_id:
                print("student name:",enrollment.student.student_name)
                print("student email:",enrollment.student.student_email)
                print("course name:",enrollment.course.course_name)
                print("course duration:",enrollment.course.course_duration)
            else:
                print("enrollment not found")

            # DISPLAY STUDENTS

    def display_student(self):
        if not self.students:
            print("empty students")
            return
        for student in self.students.values():
            print(f"student id :{student.student_id}")
            print(f"student name:{student.student_name}")
            print(f"student email:{student.student_email}")


        #DISPLAY COURSES

    def display_course(self):
        if not self.courses:
            print("empty courses")
            return
        for course in self.courses.values():
            print(f"course id:{course.course_id}")
            print(f"course name:{course.course_name}")
            print(f"course duration:{course.course_duration}")

service=Enrollment_Services()
while True:
        print("\n=====STUDENT COURSE ENROLLMENT SYSTEM=====")
        print("1. Add student")
        print("2. Add Course")
        print("3. Enroll student")
        print("4. Remove enrollment")
        print("5. View student courses")
        print("6. Display students")
        print("7. Display courses")
        print("8. Exit")
        choice=  input("enter choice")
        if choice=="1"  :
            service.add_student()
        elif choice=="2":
            service.add_course()
        elif choice=="3":
            service.enroll_student()
        elif choice=="4":
            service.remove_enrollment()
        elif choice=="5":
            service.view_student_courses()    
        elif choice=="6":
            service.display_student()    
        elif choice=="7":
            service.display_course()
        elif choice=="8":
            print("thank you for using student course enrollment system")
            break        
        else:
            print("invalid choice")
        
