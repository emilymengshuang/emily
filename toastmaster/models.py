from django.db import models

# Create your models here.



class meetings(models.Model):

    theme = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics')
    desc= models.TextField()
    date= models.DateField()
    
    
    # offer= models.BooleanField(default=False)   


# # Create your models here.

#     from django.db import models




# class Destination(models.Model):

#     name = models.CharField(max_length=100)
#     img =models.ImageField(upload_to='pics')
#     desc= models.TextField()
#     price= models.IntegerField()
#     offer= models.BooleanField(default=False) 