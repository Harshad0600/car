from django.contrib import admin
# from .models import cservice
# from .models import LoginInfo
from .models import *

# Register your models here.
admin.site.register(cservice)
admin.site.register(LoginInfo)
admin.site.register(SignupInfo)