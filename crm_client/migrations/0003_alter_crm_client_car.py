# Generated by Django 4.2.6 on 2023-11-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_client', '0002_alter_crm_client_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_client',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_client.brandauto'),
        ),
    ]
