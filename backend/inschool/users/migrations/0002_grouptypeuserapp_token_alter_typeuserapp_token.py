# Generated by Django 4.0.3 on 2022-03-07 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouptypeuserapp',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='typeuserapp',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
