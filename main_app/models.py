from django.db import models
from django.contrib.auth.models import User

# class Bird:
#     def __init__(self, species, likes, native_to):
#         self.species = species
#         self.likes = likes
#         self.native_to = native_to

# birds = [
#     Bird('Great Horned Owl' , 'rodents' , 'North/South America' ),
#     Bird('Steller\'s Jay' , 'nuts, berries' , 'Western North America'),
# ]

TIMES = (
    ('DWN', 'Dawn'),
    ('MRN', 'Morning'),
    ('AFT', 'Afternoon'),
    ('DSK', 'Dusk'),
    ('NIT', 'Night')
)

class Habitat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bird(models.Model): 
    species = models.CharField(max_length=200)
    likes = models.TextField(max_length=200)
    native_to = models.CharField(max_length=100)

    habitats = models.ManyToManyField(Habitat)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.species

#Spotting model, will be the 'many' in the one to many relationship
class Spotting(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    time_of_day = models.CharField(
        max_length=3,

        choices=TIMES,
        default=TIMES[0][0]
        )

    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bird.species} at {self.location} - during {self.get_time_of_day_display()}, on {self.date}'

    class Meta:
        ordering = ['-date']

