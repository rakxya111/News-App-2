# Generated by Django 5.1.4 on 2024-12-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0007_alter_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tag',
        ),
    ]
