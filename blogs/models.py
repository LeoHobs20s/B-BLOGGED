from django.db import models

class BlogPost(models.Model):
    """ This class creates the model blog post """

    title = models.CharField(max_length=80)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ This method returns the  """
        return f'{self.title}\n{self.text}'
    