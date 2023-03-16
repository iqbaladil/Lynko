from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        # Display the order alphabatically in dashboard.html
        ordering = ('name',)

    def __str__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(Category, related_name='links', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        # Display the links based last created at ordering.
        ordering = ('-created_at',)