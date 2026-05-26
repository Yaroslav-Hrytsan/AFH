from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    birth_day = models.DateField(null=True)
    bio = models.TextField(null=True)
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):        
        return self.name
class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)
class Books(models.Model):
    title = models.TextField(max_length=100)
    year = models.IntegerField()
    publisher_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ManyToManyField(Genre, related_name="books")

    objects = models.Manager()
    available = AvailableManager()
    def __str__(self):
        return self.title



    
