from django.db import models

# Create your models here.


class ApolloModelA(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=300,null=False,default="")

class ApolloModelP(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=300,null=False,default="")
    insta = models.CharField(max_length=50,null=False)
    face = models.CharField(max_length=50,null=False)
    twitter = models.CharField(max_length=50,null=False)
    pintrest = models.CharField(max_length=50,null=False)

class ApolloModelO(models.Model):
    image1 = models.CharField(max_length=50,null=False)
    image2 = models.CharField(max_length=50,null=False)
    image3 = models.CharField(max_length=50,null=False)

class ApolloModelL(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=300,null=False,default="")

class ApolloModelL2(models.Model):
    image1 = models.CharField(max_length=50,null=False)
    image2 = models.CharField(max_length=50,null=False)
    image3 = models.CharField(max_length=50,null=False)

class ApolloModelO2(models.Model):
    mail = models.CharField(max_length=50,null=False)
    subject = models.CharField(max_length=50,null=False)
    message = models.CharField(max_length=50,null=False)