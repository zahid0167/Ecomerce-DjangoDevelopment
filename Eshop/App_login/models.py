from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.


class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """creates and saves a user with given email $ pass """
        if not email:
            raise ValueError("Email must be added")
        email= self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

class Userprofile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(
        ugettext_lazy('staff status'),
        default=False,
        help_text=ugettext_lazy('Designates whether the user canlog in this site')
    )
    is_active = models.BooleanField(
        ugettext_lazy('active'),
        default=True,
        help_text = ugettext_lazy('Designates whether the user should be treated as activeunseleted this instend of deleting issue')
    )

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(Userprofile, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=265, blank=True)
    fullname = models.CharField(max_length=265, blank=True)
    addresh = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phon = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username
    
    def is_fully_filled(self):
        fields_name= [f.name for f in self._meta.get_fields()]

        for field_name in fields_name:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True



@receiver(post_save, sender=Userprofile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Userprofile)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    


    

    
