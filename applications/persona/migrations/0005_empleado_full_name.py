# Generated by Django 3.1.3 on 2020-12-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_hoja_de_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres Completos'),
        ),
    ]
