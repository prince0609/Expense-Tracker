# Generated by Django 5.1.6 on 2025-03-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0006_alter_profile_budget_alter_profile_expense_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
