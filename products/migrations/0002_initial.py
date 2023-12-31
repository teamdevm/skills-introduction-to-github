# Generated by Django 4.2.2 on 2023-06-08 17:53

from django.db import migrations, models

def insert_initial_data(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    initial_data = [
        ('T-Shirt', 19.99, 'Comfortable cotton t-shirt', 'Tops'),
        ('Jeans', 49.99, 'Classic denim jeans', 'Bottoms'),
        ('Dress', 59.99, 'Elegant evening dress', 'Dresses'),
        ('Shoes', 39.99, 'Stylish sneakers', 'Shoes'),
        ('Jacket', 79.99, 'Warm winter jacket', 'Outerwear'),
    ]
    for name, price, description, category in initial_data:
        Product.objects.create(name=name, price=price, description=description, category=category)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('image', models.CharField(default='placeholder.png', max_length=255)),
                ('image_hash', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.RunPython(insert_initial_data),
    ]
