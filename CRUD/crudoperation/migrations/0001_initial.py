# Generated by Django 3.0.6 on 2020-10-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(db_column='firstname', max_length=100)),
                ('LastName', models.CharField(db_column='lastname', max_length=100)),
                ('Address', models.CharField(db_column='address', max_length=1000)),
                ('DOB', models.DateField(db_column='date', default=2000)),
                ('Phone', models.IntegerField(db_column='phone')),
                ('Image', models.ImageField(db_column='image', upload_to='images')),
                ('Faculty', models.CharField(db_column='faculty', max_length=100)),
            ],
        ),
    ]
