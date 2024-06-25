from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Blog_author')
    title = models.CharField(max_length=264)
    slug = models.SlugField(max_length=264, unique=True)
    image = models.ImageField(upload_to='blog-images')
    content = models.TextField(verbose_name='Write Content Blog')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publish_date']
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment) + ' ' + str(self.user)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker_user')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='liked_blog')

    def __str__(self):
        return str(self.blog) + '' + str(self.user)