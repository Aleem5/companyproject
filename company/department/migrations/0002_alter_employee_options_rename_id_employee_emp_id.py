# Generated by Django 4.1.7 on 2023-02-16 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['emp_id']},
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='id',
            new_name='emp_id',
        ),
    ]