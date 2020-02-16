# Generated by Django 3.0.2 on 2020-02-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='blog/'),
        ),
    ]