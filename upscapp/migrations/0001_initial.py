# Generated by Django 2.2 on 2020-01-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('about', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesData',
            fields=[
                ('subject_code', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100, unique=True)),
                ('subject_duration', models.CharField(max_length=100)),
                ('subject_startdate', models.DateField(max_length=100)),
                ('subject_starttime', models.TimeField(max_length=100)),
                ('subject_instructor_name', models.CharField(max_length=100)),
                ('subject_instructor_experience', models.CharField(max_length=100)),
            ],
        ),
    ]
