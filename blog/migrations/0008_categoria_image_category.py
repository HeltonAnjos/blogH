# Generated by Django 4.2 on 2023-05-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_emphasis_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='image_category',
            field=models.ImageField(blank=True, null=True, upload_to='category_img/%Y/%m/%d/', verbose_name='Imagem'),
        ),
    ]