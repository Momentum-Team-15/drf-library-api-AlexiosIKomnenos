from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Book(models.Model):
    featured = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateField()
    genre = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", null=True, blank=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='mybook')
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Notes(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="booknotes", null=True, blank=True)

    def __str__(self):
        return f"{self.book} notes on created {self.created_at}"

class ReadStatus(models.Model):
    read_status = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="readstatuses", null=True, blank=True)

    def __str__(self):
        return self.read_status

