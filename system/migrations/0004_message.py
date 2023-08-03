# Generated by Django 4.2.3 on 2023-08-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_myprofile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
