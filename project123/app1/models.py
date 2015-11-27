# 101102103@fnbic.ru for 103 group

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=(('f', 'Female'), ('m', 'Male'), ('n', 'N/A')), max_length=1)
    age = models.DecimalField(decimal_places=0, max_digits=2)
    photo = models.FileField(upload_to='photos')
    group = models.ForeignKey('Group')
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    recepient = models.ForeignKey(User, related_name='recepient')
    message = models.TextField()
    ts = models.DateTimeField(auto_now=True)    
    
    def __unicode__(self):
        return "%s->%s: %s" % (self.sender, self.recepient, self.message[:100])
    
class Group(models.Model):
    group_name = models.CharField(max_length=200)
    info = models.TextField()
    
    def __unicode__(self):
        return "%s - %s" % (self.group_name, self.info)
    
# Create your models here.
