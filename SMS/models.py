from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField()  # null=True,blank=True
    mobileNo = models.CharField(max_length=12) # null=True,blank=True
    dob = models.DateField(null=True,blank=True)
    pic = models.ImageField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    

class CourseStudent(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='course_enrollments',null=True,blank=True)

    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='student_enrollments',null=True,blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"



class PaymentDetails(models.Model):
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=100,choices=[("cash","Cash"),("debit card","Debit Card"),("credit card","Credit Card"),("paytm","PayTM")])
    payment_date = models.DateTimeField(auto_now=True)

    student = models.ForeignKey(Student, null=False,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount}"


    


    
 

