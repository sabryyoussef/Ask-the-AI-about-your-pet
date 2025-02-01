from django.db import models

class Symptom(models.Model):
    CATEGORY_CHOICES = [
        ('mobility', 'Mobility Issues'),
        ('emergency', 'Emergency'),
        ('behaviour', 'Behaviour'),
        ('brain_spinal', 'Brain & Spinal'),
        ('breathing', 'Breathing'),
        ('breeds', 'Breeds'),
        ('ears', 'Ears'),
        ('eyes', 'Eyes'),
        ('fleas', 'Fleas, Ticks & Worms'),
        ('hazards', 'Hazards & Poisons'),
        ('joints', 'Joints & Mobility'),
        ('mouth', 'Mouth & Teeth'),
        ('nails_pads', 'Nails & Pads'),
        ('nose', 'Nose'),
        ('older_pet', 'Older Pet'),
        ('other', 'Other'),
        ('tummy', 'Poorly Tummy'),
        ('pregnancy', 'Pregnancy & Genitals'),
        ('seasonal', 'Seasonal'),
        ('skin_coat', 'Skin & Coat'),
        ('tail', 'Tail'),
        ('urinary', 'Urinary'),
        ('wounds_trauma', 'Wounds & Trauma'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='symptom_icons/', blank=True)

    def __str__(self):
        return self.name
