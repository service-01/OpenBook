# Generated by Django 5.0.6 on 2024-07-15 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_comment_post_share'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='share',
            unique_together=set(),
        ),
    ]
