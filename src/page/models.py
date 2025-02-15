from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Contacts(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}"

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    card_number = models.CharField(max_length=16, default='0000000000000000')
    expiration_date = models.CharField(max_length=5, default='00/00') # Format: MM/YY
    cvv = models.CharField(max_length=4, default='0000')
