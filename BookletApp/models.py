from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#class User(models.Model):
	#username= models.CharField(max_length= 150)
	#email= models.CharField(max_length= 150)
	#password= models.CharField(max_length= 50, blank= True)
    #def __str__(self):
        #return self.email


class Category(models.Model):
    name= models.CharField(max_length= 50, blank= True)
    description= models.TextField(max_length= 250, blank= True)
    class Meta:
        verbose_name_plural= 'Categories'



class File(models.Model):
    name= models.CharField(max_length= 50, blank= True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    upload_file= models.FileField(upload_to= 'UploadsSite', blank= True)
    Specialized= models.BooleanField(default= False)
    General= models.BooleanField(default= False)
    author= models.CharField(max_length= 50, blank= True)
    uploaded_date= models.DateTimeField(null= True)
    file_type= models.CharField(max_length= 50, blank= True)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.name #, self.upload_file        

class Download(models.Model):
    #user= models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    date_time= models.DateTimeField(auto_now_add= True)
    file= models.ForeignKey(File, on_delete= models.CASCADE, null= True)

class Upload(models.Model):
    #user= models.ForeignKey(User, on_delete= models.CASCADE, null= True)
    date_time= models.DateTimeField(auto_now_add= True)
    file= models.ForeignKey(File, on_delete= models.CASCADE, null= True)

class Comment(models.Model):
    file= models.ForeignKey(File, on_delete= models.CASCADE)
    text= models.TextField()
    created_time= models.DateTimeField(auto_now_add= True)
    uploaded_date= models.DateTimeField(auto_now_add= True)       


