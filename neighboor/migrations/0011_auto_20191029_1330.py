# Generated by Django 2.2.6 on 2019-10-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighboor', '0010_auto_20191028_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile/'),
        ),
    ]