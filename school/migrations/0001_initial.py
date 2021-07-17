# Generated by Django 3.2.5 on 2021-07-14 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
        ('parents', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField()),
                ('class_char', models.CharField(max_length=10)),
                ('curator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('published_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_number', models.IntegerField()),
                ('school_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.region')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('birth_day', models.DateField(null=True)),
                ('clas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.class')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parents.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(null=True)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.staff')),
            ],
        ),
    ]