# Generated by Django 4.0.1 on 2022-01-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_form_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='plans',
            field=models.CharField(choices=[('3 Months', '3 Months'), ('6 Months', '6 Months'), ('12 Months', '12 Months')], default=False, max_length=9),
        ),
    ]
