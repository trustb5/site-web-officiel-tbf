from django.db import models

class Mission(models.Model):
    image = models.ImageField(upload_to="image/")
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class Domaine(models.Model):
    parent = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="domaine/")
    detail = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.parent}'

class Offre(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="domaine/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

class CommandeSoja(models.Model):
    name = models.CharField(max_length=50)
    midname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    quantite = models.CharField(max_length=5)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.midname} {self.firstname} {self.numero}'