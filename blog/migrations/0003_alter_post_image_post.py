# Generated by Django 4.2 on 2023-04-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_summary_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_post",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="post_img/% Y/% m/",
                verbose_name="Imagem",
            ),
        ),
    ]
