# Generated by Django 4.0.1 on 2022-01-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_form_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='plans',
            field=models.CharField(choices=[('3 Months', 'p1'), ('6 Months', 'p2'), ('12 Months', 'p3')], default=False, max_length=9),
        ),
    ]
