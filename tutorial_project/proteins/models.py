# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Gene(models.Model):
    id = models.IntegerField(primary_key=True)
    gene_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gene'


class Organism(models.Model):
    name = models.CharField(max_length=255)
    sci_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organism'


class Protein(models.Model):
    uniprot_id = models.CharField(primary_key=True, max_length=255)
    reviewed = models.IntegerField()
    entry_name = models.CharField(max_length=255)
    length = models.IntegerField()
    protein_names = models.CharField(max_length=255)
    gene = models.ForeignKey(Gene, models.DO_NOTHING)
    organism = models.ForeignKey(Organism, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'protein'


class StructureSegment(models.Model):
    uniprot_id = models.CharField(max_length=255)
    pdb_id = models.CharField(max_length=10, blank=True, null=True)
    chain_id = models.CharField(max_length=1, blank=True, null=True)
    unp_start = models.IntegerField(blank=True, null=True)
    unp_end = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'structure_segment'
