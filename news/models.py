from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
    
    
    

class News(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    news = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

