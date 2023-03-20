from django.contrib.auth.models import AbstractUser
from django.db import models
from djstripe.models import Customer, Subscription

class Plan(models.Model):
    name = models.CharField(max_length=255)
    max_num_links = models.IntegerField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    # Before running below code, you need to add fields in shell command as
    # Step 1: python manage.py shell
    # Step 2: from accounts.models import Plan
    # Step 3: Plan.objects.create(name='Free', max_num_links=5)
    # Step 4: Plan.objects.create(name='Pro', max_num_links=100)
    # Step 5: Now run the below code.
    
    plan = models.ForeignKey(Plan, related_name='users', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    subscription = models.ForeignKey(Subscription, null=True, blank=True,on_delete=models.SET_NULL)
    