# Generated by Django 4.2.1 on 2023-05-29 20:59

from django.db import migrations, models
import uuid

# def populate_tech_lead(apps, schema_editor):
#     A


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_cart_id_alter_fabric_id_alter_size_id_and_more'),
        ('main', '0008_alter_cart_id_alter_product_photo_and_more'),
        ('main', '0017_remove_categories_slug_remove_product_slug_and_more'),
        ('main', '0018_alter_cart_id_alter_productformainpage_pic'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='Colors',
        #     name='available_products',
        #     field=models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
        # )
    ]
