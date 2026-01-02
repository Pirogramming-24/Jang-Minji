from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100) 
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Idea(models.Model):
    # DEVTOOL_CHOICES = [
    #     ('django', 'django'),
    #     ('react', 'react'),
    #     ('Spring', 'Spring'),
    #     ('Node.js', 'Node.js'),
    #     ('Java', 'Java'),
    #     ('C++', 'C++'),
    # ]

    title = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE)

class IdeaStar(models.Model):
    idea = models.OneToOneField(Idea, on_delete=models.CASCADE, related_name='star')
    is_starred = models.BooleanField(default=False)