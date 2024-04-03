from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10, null=True)
    

    #def __str__(self):
     #   return self.fullname  # Return a string representation of the 'fullname' attribute

   
    def __str__(self):
        
        return f"{self.fullname} - {self.email} - {self.mobile} - {self.subject} - {self.message}"
    class Meta:
        verbose_name_plural = "Contacts" 

class member(models.Model):
    image = models.ImageField(max_length=200, null= False)
    description = models.CharField(max_length=200, null=False)
    
    
    def __str__(self):
        return f"{self.image}{self.description}"


class Blog(models.Model):
    video_file = models.FileField(upload_to='videos/')  # Field for the video file
    description = models.TextField()

    def __str__(self):
        return f"{self.description[:50] }{self.video_file}" # Display first 50 characters of description
    


class Team(models.Model):
    image = models.ImageField(upload_to='team_members/')
    description = models.TextField()

    def __str__(self):
        return f"{self.description[:50]}{self.image}"

class Training(models.Model):
    image = models.ImageField(upload_to='training/')
    description = models.TextField()

    def __str__(self):
        return f"{self.description[:50]}{self.image}"


from django.db import models

class Event(models.Model):
    image = models.ImageField(upload_to='event_images/')
    link = models.URLField()

    def __str__(self):
        return f"{self.image}{self.link}"