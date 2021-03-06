# Generated by Django 3.2 on 2021-05-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0003_alter_tree_humidity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='continentality',
            field=models.IntegerField(blank=True, null=True, verbose_name='Contiinentalité'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='family',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Famille'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='humidity_a',
            field=models.IntegerField(blank=True, null=True, verbose_name='Humidité_a'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='latin_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Nom latin'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='light',
            field=models.IntegerField(blank=True, null=True, verbose_name='Lumière'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='name',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='name_img',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Nom img'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='organic_material',
            field=models.IntegerField(blank=True, null=True, verbose_name='Matière organique'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='ph',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ph'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='salinity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Salinité'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='texture',
            field=models.IntegerField(blank=True, null=True, verbose_name='Texture'),
        ),
    ]
