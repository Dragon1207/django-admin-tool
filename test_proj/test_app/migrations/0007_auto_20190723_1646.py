# Generated by Django 2.2.2 on 2019-07-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_auto_20190723_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner_content_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='owner_id',
            new_name='object_id',
        ),
    ]
