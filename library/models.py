from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(
        'auth.User',
        related_name='books',
        on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=False)
    isbn = models.CharField(max_length=13, null=False)

    def __str__(self):
        return self.title
