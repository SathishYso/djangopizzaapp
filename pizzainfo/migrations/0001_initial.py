# Generated by Django 3.2.5 on 2021-08-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzatype', models.CharField(max_length=30)),
                ('pizzasize', models.CharField(max_length=30)),
                ('pizzatoppings', models.CharField(max_length=30)),
            ],
        ),
    ]