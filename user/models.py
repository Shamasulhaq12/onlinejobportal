from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserAccountManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError({'error': 'something went wrong while getting profile'})
		print(email)
		# if '@gmail' in email:
		# 	raise Response({'error': 'something went wrong while getting profile'})
		user = self.model(email=self.normalize_email(email), name=name)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, name, password=None):
		if password is None:
			raise TypeError("user must have an password")
		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=100, unique=True)
	name = models.CharField(max_length=100,)
	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)

	objects = UserAccountManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name',]

	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name

	def __int__(self):
		return self.email
