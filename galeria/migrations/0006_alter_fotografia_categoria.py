# Generated by Django 4.2.1 on 2023-09-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta'), ('TELESCÓPIO', 'telescópio')], default='', max_length=100),
        ),
    ]
