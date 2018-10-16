# Generated by Django 2.1.1 on 2018-10-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Details',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('title', models.CharField(choices=[('Mr', 'Mr.'), ('Mrs', 'Mrs.')], max_length=3)),
                ('first_Name', models.CharField(max_length=20)),
                ('last_Name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
