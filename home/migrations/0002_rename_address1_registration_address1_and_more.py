# Generated by Django 5.0.1 on 2024-02-09 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='Address1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Address2',
            new_name='address2',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Fathers_Name',
            new_name='fathers_name',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Full_Name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='State',
            new_name='state',
        ),
    ]