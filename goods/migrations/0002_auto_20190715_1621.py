# Generated by Django 2.2.2 on 2019-07-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='colorurl',
            field=models.ImageField(upload_to='media/color/'),
        ),
    ]