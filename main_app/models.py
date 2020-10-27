from django.db import models

# class Bird:
#     def __init__(self, species, likes, native_to):
#         self.species = species
#         self.likes = likes
#         self.native_to = native_to

# birds = [
#     Bird('Great Horned Owl' , 'rodents' , 'North/South America' ),
#     Bird('Steller\'s Jay' , 'nuts, berries' , 'Western North America'),
# ]


class Bird(models.Model): 
    species = models.CharField(max_length=200)
    likes = models.TextField(max_length=200)
    native_to = models.CharField(max_length=100)

    def __str__(self):
        return self.species


