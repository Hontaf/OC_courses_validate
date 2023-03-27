from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
     #utilisation d'une classe imbriquée pour definir des choix à opérer
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    ...
    genre= models.fields.CharField(choices=Genre.choices,max_length=5)
    ...
    biography = models.fields.CharField(max_length=1000)
    year_formed= models.fields.IntegerField(
        validators = [MinValueValidator(1900),MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    
    official_homepage = models.fields.URLField(null=True,blank=True)
    #like_new = models.fields.BooleanField(default=False)

    #une methode ui nous permettra de recuperer le nom de lelement dans le site d'administration de django (personnalisation )
    def __str__(self):
        return f'{self.name}'
   
    


class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    descrption = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default = False)
    year = models.fields.IntegerField(validators = [MinValueValidator(1980),MaxValueValidator(2023)],null=True , blank= True)
    
    #Une nouvelle classe imbriquée 
    class Type (models.TextChoices):
        Records = "Re"
        Clothing = "Cl"
        Posters = "Po"
        Miscellaneous = "Mi"

    type = models.fields.CharField(choices=Type.choices,max_length=5)
    band = models.ForeignKey(Band,null = True ,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
