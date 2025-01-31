from django.db import models

class Symptom(models.Model):
    CATEGORY_CHOICES = [
        ('mobility', 'Mobility Issues'),
        ('fleas', 'Fleas, Ticks & Worms'),
        ('joints', 'Joints & Mobility'),
        ('mouth', 'Mouth & Teeth'),
        ('tummy', 'Poorly Tummy'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='symptom_icons/', blank=True)

    def __str__(self):
        return self.name
