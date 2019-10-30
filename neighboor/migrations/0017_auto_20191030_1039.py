# Generated by Django 2.2.6 on 2019-10-30 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighboor', '0016_auto_20191029_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='datecreated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='image',
            field=models.ImageField(default='hood.jpg', upload_to='hood/'),
        ),
    ]