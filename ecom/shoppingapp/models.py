from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.urls import reverse


class Categary(models.Model):
        name=models.CharField(max_length=250,unique=True)
        slug=models.SlugField(max_length=250,unique=True)
        description=models.TextField(blank=True)
        image=models.ImageField(upload_to='categary',blank=True)

        class Meta:
                ordering = ('name', )
                verbose_name = 'categary'
                verbose_name_plural = 'categaries'

        def get_url(self):
          return reverse('shoppingapp:product_by_categary',args=[self.slug])


        def __str__(self):
          return '{}'.format(self.name)

class Product(models.Model):
        name = models.CharField(max_length=250, unique=True)
        slug = models.SlugField(max_length=250, unique=True)
        description = models.TextField(blank=True)
        price=models.DecimalField(max_digits=10,decimal_places=2)
        categary=models.ForeignKey(Categary,on_delete=models.CASCADE)
        image = models.ImageField(upload_to='Product', blank=True)
        stock=models.IntegerField()
        available=models.BooleanField(default=True)
        created=models.DateTimeField(auto_now_add=True)
        updated=models.DateTimeField(auto_now=True)

        def get_url(self):
                return  reverse('shoppingapp:productdetail',args=[self.categary.slug,self.slug])

        class Meta:
                ordering = ('name',)
                verbose_name = 'product'
                verbose_name_plural = 'products'


        def __str__(self):
         return '{}'.format(self.name)