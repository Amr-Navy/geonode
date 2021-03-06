# Generated by Django 2.2.12 on 2020-04-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_merge_20200323_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='doi',
            field=models.CharField(blank=True, help_text='a DOI will be added by Admin before publication.', max_length=255, null=True, verbose_name='DOI'),
        ),
    ]
