# Generated by Django 2.2.5 on 2019-10-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0005_contactme'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainerdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('post', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]