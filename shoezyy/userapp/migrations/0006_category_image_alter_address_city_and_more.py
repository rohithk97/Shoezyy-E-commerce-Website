# Generated by Django 4.1.7 on 2023-04-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_alter_address_city_alter_userprofile_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Hydrabad', 'Hydrabad'), ('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Hubli', 'Hubli'), ('Coimbator', 'Coimbator'), ('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram')], max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, choices=[('Hydrabad', 'Hydrabad'), ('Madurai', 'Madurai'), ('Kozhikkode', 'Kozhikkode'), ('Hubli', 'Hubli'), ('Coimbator', 'Coimbator'), ('Kannur', 'Kannur'), ('Banglore', 'Banglore'), ('Ernakulam', 'Ernakulam'), ('Thiruvananthapuram', 'Thiruvananthapuram')], max_length=20, null=True),
        ),
    ]