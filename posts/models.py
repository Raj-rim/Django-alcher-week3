from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField()
    release = models.DateField()
    poster = models.ImageField(default='fallback.png', blank=True)
    backdrop = models.ImageField(default='fallback2.png', blank=True)
    overview = models.TextField(blank=True)
    rating=models.FloatField(default=0.0)
    popularity=models.FloatField(default=0.0)
    
    likes=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Cast(models.Model):
    post = models.ForeignKey(Post, related_name='casts', on_delete=models.CASCADE)
    original_name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    profile_path = models.ImageField(upload_to='casts/',default='fallback3.png',blank=True)

    def __str__(self):
        return self.original_name
