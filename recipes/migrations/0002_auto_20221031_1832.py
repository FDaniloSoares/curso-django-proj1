# Generated by Django 3.2.16 on 2022-10-31 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
