from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user        
    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        創建超級用戶時，除了普通用戶需要的字段外，還會自動設置 is_staff 和 is_superuser 為 True。如果這些字段未正確設置，則引發錯誤。
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
     
        return self.create_user(email, username, password, **extra_fields)


class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(primary_key = True , db_column = "email")
    username = models.CharField(max_length = 50,db_column='username',unique=True)
    birthday = models.DateField(null = True , blank = True , db_column = "birthday")
    sex = models.CharField(max_length = 2 , choices = (("M","男"),("F","女")) , db_column = "sex" , null=True , blank=True)
    is_active = models.BooleanField(default = False,db_column="is_active") # 用來標識用戶是否活躍的布爾欄位。
    is_staff = models.BooleanField(default=False,db_column="is_staff") # 用來標識用戶是否具有管理員權限的布爾欄位。
    date_joined = models.DateTimeField(auto_now_add=True) # 用戶創建時間，自動添加。

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return username
    
    
    
    

