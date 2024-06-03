# Generated by Django 5.0.3 on 2024-05-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_counterdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterdata',
            name='best_award',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='counterdata',
            name='coffee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='counterdata',
            name='happy_people',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='counterdata',
            name='recipe',
            field=models.IntegerField(default=0),
        ),
    ]
