# Generated by Django 4.2.6 on 2023-11-07 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_client',
            name='car',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='crm_client.brandauto'),
        ),
    ]
