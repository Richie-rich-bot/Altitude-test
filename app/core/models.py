from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Record(models.Model):
    Category_Code = models.CharField(max_length=255)
    Diagnosis_Code = models.IntegerField()
    Full_Code = models.CharField(max_length=255, blank=True) 
    Abbreviated_Description = models.CharField(max_length=255)
    Full_Description = models.CharField(max_length=255)
    Category_Title = models.CharField(max_length=255)

@receiver(pre_save, sender=Record)
def auto_fill_full_code(sender, instance, **kwargs):
    # Auto-fill Full_Code when both Category_Code and Diagnosis_Code are present
    if instance.Category_Code and instance.Diagnosis_Code:
        instance.Full_Code = f"{instance.Category_Code}{instance.Diagnosis_Code}"
