# Generated by Django 2.2.5 on 2019-10-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(blank=True, null=True, upload_to='')),
                ('des', models.CharField(blank=True, max_length=30000, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('post', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
