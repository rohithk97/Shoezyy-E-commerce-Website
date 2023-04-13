# Generated by Django 4.1.7 on 2023-04-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_category_image_alter_address_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kozhikkode', 'Kozhikkode'), ('Hydrabad', 'Hydrabad'), ('Coimbator', 'Coimbator'), ('Ernakulam', 'Ernakulam'), ('Banglore', 'Banglore'), ('Hubli', 'Hubli'), ('Madurai', 'Madurai'), ('Kannur', 'Kannur')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kozhikkode', 'Kozhikkode'), ('Hydrabad', 'Hydrabad'), ('Coimbator', 'Coimbator'), ('Ernakulam', 'Ernakulam'), ('Banglore', 'Banglore'), ('Hubli', 'Hubli'), ('Madurai', 'Madurai'), ('Kannur', 'Kannur')], max_length=20, null=True),
        ),
    ]
