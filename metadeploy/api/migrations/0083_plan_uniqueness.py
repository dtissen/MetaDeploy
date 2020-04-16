# Generated by Django 2.2.11 on 2020-04-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0082_auto_20200312_1554"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="plan",
            constraint=models.UniqueConstraint(
                fields=("version", "plan_template"), name="unique_version_plan_template"
            ),
        ),
        migrations.AddConstraint(
            model_name="plan",
            constraint=models.UniqueConstraint(
                condition=models.Q(tier="primary"),
                fields=("version",),
                name="unique_version_primary_plan",
            ),
        ),
    ]