# Generated by Django 4.0.3 on 2022-03-08 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_grouptypeuserapp_token_alter_typeuserapp_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapp',
            name='ma_type_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='users.typeuserapp'),
        ),
    ]