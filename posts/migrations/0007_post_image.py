# Generated by Django 5.0.7 on 2024-08-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_teg_alter_comment_posts_post_teg'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts_images/'),
        ),
    ]
