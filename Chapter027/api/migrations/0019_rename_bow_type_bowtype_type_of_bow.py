# Generated by Django 5.1.1 on 2025-06-01 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_bowtype_bow_type_bowtype_max_arrow_length_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bowtype',
            old_name='bow_type',
            new_name='type_of_bow',
        ),
    ]
