# Generated by Django 4.2.2 on 2023-07-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_orders_customer_orders_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
