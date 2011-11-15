from django.db import models

class Url(models.Model):
    input_url = models.CharField(max_length=500)
    string = models.CharField(max_length=10)
    appended_url = models.CharField(max_length=510)
#    def __unicode__(self):
#        return self.string

