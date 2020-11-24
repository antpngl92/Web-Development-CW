from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from news.models import News, Category

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, dob, password=None):
        if not username:
            raise ValueError("You must provide username!")
        if not email:
            raise ValueError("You must provide email address!")
        if not dob:
            raise ValueError("You must provide your date of birth!")

        user = self.model(
            username=username,
            email = self.normalize_email(email),
            dob=dob,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, dob, password):
        user = self.create_user(
            username=username,
            email=email,
            dob=dob,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=20, unique=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    dob = models.DateField(verbose_name='date of birth', null=True)
    favourite = models.ManyToManyField(Category, blank=True )
    likes = models.ManyToManyField(News, related_name="users")
    profile_picture = models.ImageField(upload_to ='profilePic/', default = 'profilePic/pp.png')

    # The fields bellow are REQUIRED for AbstractBaseUser class (for custom user model)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Whatever you want to be able to log in, use this
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    # Tell this account model where the Manager is
    objects = MyAccountManager()

    # Print model as username
    def __str__(self):
        return self.username

     # Required functions for custom users
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    @property
    def favourites(self):
        return this.favourite
