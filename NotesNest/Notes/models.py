from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class User(AbstractUser):
    ROLES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(choices=ROLES, default='USER', max_length=5)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Notes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(User, related_name='uploaded_notes', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='notes', on_delete=models.CASCADE)
