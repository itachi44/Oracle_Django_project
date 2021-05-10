from django.db import models

# Create your models here.
class Clientapp(models.Model):
    id_client = models.IntegerField(primary_key=True)
    nom_client = models.CharField(max_length=200)
    prenom_client = models.CharField(max_length=200)
    telephone_client = models.CharField(max_length=12)
    adresse_client = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'clientapp'

class Compteclient(models.Model):
    id_compteclient = models.IntegerField(primary_key=True)
    id_client = models.ForeignKey(Clientapp, models.DO_NOTHING, db_column='id_client')
    email_client = models.CharField(max_length=200)
    password_client = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'compteclient'


class Domaine(models.Model):
    id_domaine = models.IntegerField(primary_key=True)
    label_domaine = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'domaine'

class Prestataire(models.Model):
    id_prestataire = models.IntegerField(primary_key=True)
    nom_prestataire = models.CharField(max_length=200)
    prenom_prestataire = models.CharField(max_length=200)
    adresse_prestataire = models.CharField(max_length=200)
    site_web = models.CharField(max_length=25, blank=True, null=True)
    telephone_prestaire = models.CharField(max_length=12)
    experience = models.CharField(max_length=1000, blank=True, null=True)
    desc_competences = models.CharField(max_length=1000, blank=True, null=True)
    id_domaine = models.ForeignKey(Domaine, models.DO_NOTHING, db_column='id_domaine')

    class Meta:
        managed = False
        db_table = 'prestataire'


class Profilprestataire(models.Model):
    id_profil = models.IntegerField(primary_key=True)
    id_prestataire = models.ForeignKey(Prestataire, models.DO_NOTHING, db_column='id_prestataire')
    email_prestaire = models.CharField(max_length=150)
    password_prestataire = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilprestataire'

class Serviceapp(models.Model):
    id_service = models.IntegerField(primary_key=True)
    id_client = models.ForeignKey(Clientapp, models.DO_NOTHING, db_column='id_client')
    id_prestataire = models.ForeignKey(Prestataire, models.DO_NOTHING, db_column='id_prestataire')
    label_service = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'serviceapp'


class Servicedemandee(models.Model):
    id_service = models.OneToOneField(Serviceapp, models.DO_NOTHING, db_column='id_service', primary_key=True)
    id_client = models.ForeignKey(Clientapp, models.DO_NOTHING, db_column='id_client')
    date_demande = models.DateField(blank=True, null=True)
    paye = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicedemandee'
        unique_together = (('id_service', 'id_client'),)