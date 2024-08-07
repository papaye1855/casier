from django.db import models
from .constants import (
    PAYS_CODES_CHOICES,
    ETAT_DEMANDE_TYPES_CHOICES,
    GENRE_CHOICES,
    PROFESSION_TYPES_CHOICES,
    STATUS_MATRINONIAL_CHOICES,
)
# Create your models here.


class LocaliteBackOffice(models.Model):
    nom_province = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    backend_api_gateway = models.CharField(max_length=255)
    code_localite = models.CharField(max_length=255)


    def __str__(self) -> str:
        return f"{self.nom_province}({self.ville})"


class CasierJudiciaire(models.Model):
    code_demande = models.PositiveIntegerField()
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    nom_pere = models.CharField(max_length=255) 
    nom_mere = models.CharField(max_length=255) 
    date_naisance = models.DateField() 
    lieu_naissance = models.CharField(max_length=255) 
    pays = models.CharField(max_length=255,choices=PAYS_CODES_CHOICES) 
    nationalite = models.CharField(max_length=255,choices=PAYS_CODES_CHOICES) 
    profession = models.CharField(max_length=255,choices=PROFESSION_TYPES_CHOICES,default="etudiant")
    etat_familiale = models.CharField(max_length=255,choices=STATUS_MATRINONIAL_CHOICES,default="celibataire") 
    adresse = models.CharField(max_length=255) 
    telephone = models.CharField(max_length=255)
    piece_justificatif = models.FileField(upload_to="static/piecesjustificatifs/")
    etat = models.CharField(max_length=255,choices=ETAT_DEMANDE_TYPES_CHOICES,default="traitement")
    genre = models.CharField(max_length=255,choices=GENRE_CHOICES,default="homme")
    localite = models.ForeignKey(LocaliteBackOffice,on_delete=models.CASCADE)
    backoffice_received = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Demande de casier judiciaire N° : " + str(self.code_demande)