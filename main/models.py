from django.core.files.storage import FileSystemStorage
from django.core.validators import FileExtensionValidator
from django.db import models

from os import path
from uuid import uuid4



class UUIDFileStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        name, ext = path.splitext(name)
        return name + '___' + uuid4().hex + ext



class Info(models.Model):
    tag = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=50)
    data = models.JSONField()

    def getData(self, *args):
        gottenData = self.data

        for arg in args:
            if arg not in gottenData: return False
            gottenData = gottenData[arg]

        return gottenData

    def __str__(self):
        return self.name

    class Meta:
        db_table_comment = "Configs and information"
        ordering = ('tag',)
        verbose_name = "Info"
        verbose_name_plural = "Info"


class Category(models.Model):
    order = models.IntegerField(default=10, null=True, blank=True)
    tag = models.SlugField(default='', null=True, unique=True)
    name = models.CharField(max_length=96)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='subcat'
    )


    def __str__(self):
        return self.name

    class Meta:
        db_table_comment = "Product`s categories"
        ordering = ('tag',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    tag = models.SlugField(default='', null=True, unique=True)
    addingTime = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=96)
    description = models.TextField()
    photo = models.ImageField(storage=UUIDFileStorage)
    characteristics = models.FileField(
        storage=UUIDFileStorage, upload_to="products_data",
        validators=[
            FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])
        ]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'[{self.pk}] ({self.tag}) {self.name}'


    class Meta:
        db_table_comment = "Products"
        ordering = ('tag',)
        verbose_name = "Product"
        verbose_name_plural = "Products"
