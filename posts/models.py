from django.db import models

class Teg(models.Model):
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.description


# Create your models here.
class Post(models.Model):
#    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teg = models.ManyToManyField(Teg, related_name='posts')


    def __str__(self):
        return f'{self.title} - {self.rate}'


class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=100)