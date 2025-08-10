from django.shortcuts import reverse
from django.db import models

from django.contrib.auth import get_user_model

class Post(models.Model):
   STATUS_CHOICES = (
      ('pub', 'Published'),
      ('drf', 'Draft'),
   )

   title = models.CharField(max_length = 50)
   text = models.TextField()
   author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
   datetime_created = models.DateTimeField(auto_now_add = True)
   datetime_modified = models.DateTimeField(auto_now = True)
   status = models.CharField(choices = STATUS_CHOICES, max_length = 3)

   def __str__(self):
      return self.title
   
   
   def get_absolute_url(self):
      return reverse('post_detail', args= [self.id])



class Comment(models.Model):
   post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
   author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='comments')
   body = models.TextField()
   active = models.BooleanField(default=True)
   date_time_created = models.DateTimeField(auto_now=True)


   
   def __str__(self):
      return self.body[:30]
   

   def get_absolute_url(self):
       return reverse("post_detail", kwargs={"pk": self.post.id})
   