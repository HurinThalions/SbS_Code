from django.db import models

# Create your models here.

class Anleitung(models.Model):
    anleittitel = models.CharField(max_length=100)
    ersteller = models.CharField(max_length=100)
    kategorie = models.CharField(max_length=100)
    dauer = models.TimeField(auto_now_add=True)
    datum = models.DateField('datum_erstellt')
#    thumbnailbild = models.ImageField(upload_to='images/', default=None)
    def __str__(self):
        return self.anleittitel

class Anleitungsschritt(models.Model):
    anleitung = models.ForeignKey(Anleitung, on_delete=models.CASCADE, related_name='anleitungsbezeichnungen')
    schrittbenennung = models.CharField(max_length=50)
    beschreibung = models.CharField(max_length=500)
#    schrittbild = models.ImageField(upload_to='images/Schrittbilder/', default=None)
    schrittinhalt = [schrittbenennung, beschreibung]
    def __list__(self):
        return self.schrittinhalt
    # def __str__(self):
    #     return self.schrittbenennung

class Komponente(models.Model):
    anleitungsschritt = models.ForeignKey(Anleitungsschritt, on_delete=models.CASCADE)
    kompbeschreibung = models.CharField(max_length=100)
#    kompbild = models.ImageField(upload_to='images/Kompbilder', default=None)
    def __str__(self):
        return self.kompbeschreibung
