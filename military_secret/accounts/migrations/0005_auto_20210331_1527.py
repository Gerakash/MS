# Generated by Django 3.1.7 on 2021-03-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210331_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='wheel_type',
            field=models.CharField(choices=[('RH', 'RH'), ('LH', 'LH')], max_length=50),
        ),
    ]