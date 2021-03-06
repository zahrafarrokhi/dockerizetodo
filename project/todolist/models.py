from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Django ORM (object-relational mapper)
# Django ORM and Working with QuerySets
# Django comes with a powerful database lets you create, retrieve, update,and delete objects
# ************** QuerySets.
# The Django ORM is based on QuerySets. 
# A QuerySet: is a collection of database queries to retrieve objects from your database. 
# **************Creating Objects
# python manage.py shell
# *
# from todolist.models import Task
# 1
# task=Task(title="Another task")
# task.save()
# 2
# Task.objects.create(title="One more task")
# all******************
# all_task=Task.objects.all()
# get*************
# Using get() method:allows you to retrieve only a single object from the database.
# Task.objects.get(title='Another task')
# filter************
# Using filter() method:you can retrieve all tasks with a “task” word included.
# Task.objects.filter(title__icontains='task')
# *********
# QuerySet chaining multiple filters:
# Task.objects.filter(title__icontains='Task').filter(completed=False)
# *****
# Using order_by() method:Ascending 
# Task.objects.order_by('title')
# *****
# descending order 
# Task.objects.order_by('-title')

# **********
# Updating objects
# task=Task.objects.get(title='Another task')
# task.title
# task.title="Another task is this..."
# task.title
# task.save()
# *****************
# Deleting objects
# task=Task.objects.get(id=2)
# task.delete()
# Note that deleting objects will also delete any dependent relationships for 
# ForeignKey objects defined with on_delete set to CASCADE.
# Here we perform CRUD operation in python shell.
#  Same logic we will write and apply in the Django view.
