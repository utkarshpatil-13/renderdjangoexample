# Generated by Django 5.0.3 on 2024-03-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_flower_delete_approvals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='Petal_Length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='flower',
            name='Petal_Width',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='flower',
            name='Sepal_Length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='flower',
            name='Sepal_Width',
            field=models.FloatField(),
        ),
    ]
