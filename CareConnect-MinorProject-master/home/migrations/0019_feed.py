# Generated by Django 5.0.1 on 2024-03-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_patient_info_emargency_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]