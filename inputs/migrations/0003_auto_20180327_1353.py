# Generated by Django 2.0.3 on 2018-03-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0002_baser_science'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baser',
            old_name='science',
            new_name='subject',
        ),
    ]