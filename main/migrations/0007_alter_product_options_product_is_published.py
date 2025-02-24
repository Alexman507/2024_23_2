# Generated by Django 4.2.13 on 2024-06-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name'], 'permissions': [('can_change_is_published', 'can edit is published'), ('can_change_product_description', 'can edit products description'), ('can_change_product_category', 'can edit products category')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, help_text='опубликовать (сделать видимым для пользователей)', verbose_name='опубликовано'),
        ),
    ]
