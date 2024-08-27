from django.db import models

# Create your models here.
class Student(models.Model):
    studentID = models.IntegerField()
    firstName = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    birthdate = models.DateField()
    major = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.studentID} {self.firstName}'
    
class Enrollments(models.Model):
    enrollmentID = models.IntegerField()
    StudentID = models.IntegerField()
    courename = models.CharField(max_length=30)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return self.enrollmentID