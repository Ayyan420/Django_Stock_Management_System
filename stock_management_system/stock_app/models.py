from django.db import models

import datetime

from django.utils import timezone

# Create your models here.


category_choices = (
    ('Furniture', 'Furniture'),
    ('IT Equipment', 'IT Equipment'),
    ('Phone', 'Phone'),
    ('Electronics', 'Electronics'),
    )



# foreign  key modle
class Categorie(models.Model):
    name = models.CharField(max_length=50 , null=True, blank=False)
    created_by = models.CharField(max_length=50 , null=True, blank=False)
    upload_file = models.FileField(blank=True, null = True, upload_to = "files/%Y/%m/%d")
    upload_img = models.ImageField(blank=True, null = True, upload_to = "images/%Y/%m/%d")
    # like this # 2018/12/12


    def __str__(self): 
        return self.name

class Stock(models.Model):

    # category = models.CharField(max_length=50 , null=True , choices=category_choices)

    # category = models.CharField(max_length=50, blank = True, null = True)

    # item_name = models.CharField(max_length=50, blank = True, null = True)

    # category = models.ForeignKey(Categorie, on_delete=models.PROTECT , blank=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE , blank=True)
    # for link with another model like many2one
    item_name = models.CharField(max_length=50 , null=True, blank=True)
    receive_by = models.CharField(max_length=50, blank = True, null = True)
    quantity = models.IntegerField(default = 0, blank = True, null = True)
    issue_by = models.CharField(max_length=50, blank = True, null = True)
    issue_to = models.CharField(max_length=50, blank = True, null = True)
    created_by = models.CharField(max_length=50, blank = True, null = True)
    receive_quantity = models.CharField(max_length=50, blank = True, null = True)
    phone_number = models.IntegerField(default = 0, blank = True, null = True)
    issue_quantity = models.IntegerField(default = 0, blank = True, null = True)
    reorder_level = models.IntegerField(default = 0, blank = True, null = True)
    last_update = models.DateTimeField( auto_now_add= False, auto_now = True )
    timestampp = models.DateTimeField( auto_now_add= True, auto_now = False )
    date = models.DateTimeField( auto_now_add= False, auto_now = False ,default = datetime.datetime.now())
    
    def __str__(self):
        name = str(self.item_name)
        qty = str(self.quantity)
        all_name = "{} {}".format(name,qty) 
        return all_name


class StockListHistory(models.Model):

    category = models.ForeignKey(Categorie, on_delete=models.CASCADE , blank=True , default=None)
    item_name = models.CharField(max_length=50 , null=True, blank=True)
    receive_by = models.CharField(max_length=50, blank = True, null = True)
    quantity = models.IntegerField(default = 0, blank = True, null = True)
    issue_by = models.CharField(max_length=50, blank = True, null = True)
    receive_quantity = models.IntegerField(default = 0, blank = True, null = True)
    issue_quantity = models.IntegerField(default = 0, blank = True, null = True)
    last_update = models.DateTimeField(null=True, auto_now_add= False, auto_now = False )
    
    def __str__(self):
        name = str(self.item_name)
        qty = str(self.quantity)
        all_name = "{} {}".format(name,qty) 
        return all_name