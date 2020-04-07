from django.db import models
#from users.models import User
#from posts.models import Post

class Comment(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        # sort comments according to ascending order time of creation
        ordering = ['created_at']
    
    def __str__(self):
        return f'{self.content} created at {self.created_at}'
