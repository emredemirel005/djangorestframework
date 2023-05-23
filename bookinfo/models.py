from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publish_date = models.DateField()
    page_number = models.IntegerField()
    stock = models.IntegerField()

    
    
    def __str__(self):
        return self.title
    
    