from django.db import models

# Create your models here.

class Student(models.Model):
    Student_ID=models.AutoField(primary_key=True)
    FirstName = models.CharField(db_column='firstname', max_length=100, blank=False)
    LastName = models.CharField(db_column='lastname', max_length=100, blank=False)
    Address = models.CharField(db_column='address', max_length=1000, blank=False)
    DOB = models.DateField(db_column='date',blank=False, default=2000)
    Phone=models.IntegerField(db_column='phone',blank=False)
    Image=models.ImageField(db_column='image',upload_to='images',blank=False)
    Faculty=models.CharField(db_column='faculty',max_length=100,blank=False)
 
    
