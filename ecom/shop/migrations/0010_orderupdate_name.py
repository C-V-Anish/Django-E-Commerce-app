# Generated by Django 4.0.4 on 2022-07-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
