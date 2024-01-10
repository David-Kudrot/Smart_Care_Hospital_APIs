from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    problem = models.TextField()
    
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us" #admin panel a contact uss hoye gese tai, ekhane meta die verbose_name_plural set kore dilam karon us plural form