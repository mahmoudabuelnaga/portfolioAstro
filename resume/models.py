from django.db import models
from django.urls import reverse
# Create your models here.

class Home(models.Model):
    img1    = models.ImageField(upload_to='my-photes/') 
    img2    = models.ImageField(upload_to='my-photes/') 
    summary = models.TextField()
    about   = models.TextField()
    phone   = models.CharField(max_length=20)
    emali   = models.CharField(max_length=50)
    resume  = models.FileField(upload_to='my-resume/')

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    name    = models.CharField(max_length=254)
    email   = models.EmailField(max_length=254)
    message = models.TextField()
    time    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Portfolio(models.Model):
    title       = models.CharField(max_length=254)
    slug        = models.SlugField(max_length=254)
    imgFormal   = models.ImageField(upload_to='portfoilios-images/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('resume:post-detail', args=[self.pk, self.slug])


class portfolioImg(models.Model):
    portfolio   = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    img         = models.ImageField(upload_to='portfoilios-images/')

    def __str__(self):
        return str(self.id)