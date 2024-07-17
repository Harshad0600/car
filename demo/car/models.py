from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cservice(models.Model):
    name = models.CharField(max_length=50, null=False)
    mail = models.EmailField(max_length=50, null=False)
    number = models.BigIntegerField(null=False)
    service = models.CharField(max_length=50, null=False)
    message = models.CharField(max_length=200, null=True)



class LoginInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=False)
    login_datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_datetime}"
    

class SignupInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=254)
    signup_date = models.DateTimeField(auto_now_add=True)
    terms_agreed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username