# Generated by Django 4.1.7 on 2023-04-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Coimbator', 'Coimbator'), ('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Banglore', 'Banglore'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kannur', 'Kannur'), ('Hubli', 'Hubli'), ('Ernakulam', 'Ernakulam'), ('Hydrabad', 'Hydrabad')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Coimbator', 'Coimbator'), ('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Banglore', 'Banglore'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kannur', 'Kannur'), ('Hubli', 'Hubli'), ('Ernakulam', 'Ernakulam'), ('Hydrabad', 'Hydrabad')], max_length=20, null=True),
        ),
    ]