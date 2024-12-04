# apps/projects/models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('design', 'Design'),
        ('photo', 'Photography'),
        ('video', 'Videography'),
        ('illustration', 'Illustration')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    technologies = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title