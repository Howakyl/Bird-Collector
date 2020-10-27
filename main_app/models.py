from django.db import models

class Bird:
    def __init__(self, species, likes, native_to):
        self.species = species
        self.likes = likes
        self.native_to = native_to

# class Bird(models.Model): 
#         species = models.CharField(max_length=200)
#         likes = models.CharField(max_length=200)
#         native_to = models.CharField(max_length=100)

birds = [
    Bird('Great Horned Owl' , 'rodents' , 'North/South America' ),
    Bird('Steller\'s Jay' , 'nuts, berries' , 'Western North America'),
]
