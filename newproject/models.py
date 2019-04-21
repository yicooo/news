from django.db import models

# Create your models here.
class article(models.Model):

    title       = models.CharField(max_length= 20)
    source      = models.TextField()

    # @classmethod
    # def create(cls, title):
    #     article = cls(title=title)
        


    #     return article