from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, role, password=None):
        """
        Creates and saves a User with the given email,role and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, role, password=None):
        """
        Creates and saves a superuser with the given email,role and password.
        """
        user = self.create_user(
            email,
            password=password,
            role=role, phone=phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    options = (("employer", "employer"), ("jobseeker", "jobseeker"))
    phone = models.PositiveIntegerField(unique=True)
    role = models.CharField(max_length=30, choices=options, default="jobseeker")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'role', 'password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin






class CompanyProfile(models.Model):
    company = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,unique=True)
    logo = models.ImageField(upload_to='logo',null=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class JobseekerProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True)
    skill = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes',null=True)
    def __str__(self):
        return self.name


class JobModel(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    job_details = models.CharField(max_length=100)

    def __str__(self):
        return self.job_name


class ApplicationModel(models.Model):

    job_name = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    user = models.ForeignKey(JobseekerProfile, on_delete=models.CASCADE)
    options = ("selected", "selected"), ("rejected", "rejected"),("under_valuation","under_valuation")
    status = models.CharField(max_length=100, choices=options, default="under_valuation")

    def __str__(self):
        return self.user

    def is_valid(self):
        pass
