from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# with connections['selfedu'].cursor() as cursor:
#     cursor.execute("SELECT * FROM users__users")


# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, unique=True, db_index=True, verbose_name='URL')
    login = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    door = models.ForeignKey('Doors', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info', kwargs={'info_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Employees, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Approved employees'
        verbose_name_plural = 'Approved employees'
        ordering = ['time_create']


class Doors(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, unique=True, db_index=True, verbose_name='URL')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('category', kwargs={'cat_id': self.pk})
        return reverse('door', kwargs={'door_slug': self.slug})

    class Meta:
        verbose_name = 'Doors'
        verbose_name_plural = 'Doors'
        ordering = ['id']
