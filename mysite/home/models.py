from django.db import models

from wagtail.models import Page


from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class Values(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    date = models.CharField(max_length=100, default="")
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    dob = models.CharField(max_length=100, default="")
    qualification = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    organisation = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    member = models.CharField(max_length=100, default="no")
    transactionid = models.CharField(max_length=100, default="", unique=True)
    appliedfor = models.CharField(max_length=100, default="")
    class Meta:
        db_table="user"

class Admin(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    class Meta:
        db_table="admin"