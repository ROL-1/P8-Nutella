# Generated by Django 3.1.7 on 2021-03-03 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=75, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.categories')),
            ],
        ),
        migrations.CreateModel(
            name='CodesProductsOff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveBigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NutriscoreGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutriscore_grade', models.CharField(max_length=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_fr', models.CharField(max_length=100, unique=True)),
                ('generic_name_fr', models.CharField(max_length=100)),
                ('fat_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('salt_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugars_100g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('url', models.URLField(unique=True)),
                ('image_url', models.URLField()),
                ('Brands', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.brands')),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.categories')),
                ('CodesProductsOff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.codesproductsoff')),
                ('NutriscoreGrades', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.nutriscoregrades')),
            ],
        ),
    ]
