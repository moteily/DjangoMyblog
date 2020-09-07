from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    birth =models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20, null=True)
#下面的__str__(self)方法，表示当输出这个类创建的对象时，默认会输出这个对象的username字段
    def __str__(self):
        return 'user {}'.format(self.user.username)
