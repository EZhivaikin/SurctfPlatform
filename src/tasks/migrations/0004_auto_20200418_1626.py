# Generated by Django 3.0.2 on 2020-04-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200418_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, choices=[('PWN', 'PWN'), ('CRYPTO', 'CRYPTO'), ('PPC', 'PPC'), ('WEB', 'WEB'), ('STEGANO', 'STEGANO'), ('REVERSE', 'REVERSE'), ('JOY', 'JOY'), ('ADMIN', 'ADMIN'), ('RECON', 'RECON')], max_length=15),
        ),
    ]
