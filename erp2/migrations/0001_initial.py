# Generated by Django 4.2 on 2023-04-07 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(default='', max_length=256)),
                ('product_name', models.CharField(default='', max_length=50)),
                ('product_descr', models.CharField(default='', max_length=50)),
                ('product_price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('product_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('product_quantity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'my_product',
            },
        ),
        migrations.CreateModel(
            name='Inbound',
            fields=[
                ('productmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp2.productmodel')),
                ('inbound_quantity', models.IntegerField()),
                ('inbound_date', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('erp2.productmodel',),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('productmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='erp2.productmodel')),
                ('inbound_quantity', models.IntegerField()),
            ],
            bases=('erp2.productmodel',),
        ),
    ]
