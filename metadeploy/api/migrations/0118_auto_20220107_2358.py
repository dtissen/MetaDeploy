# Generated by Django 3.1.14 on 2022-01-07 23:58

from django.db import migrations
import metadeploy.api.models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0117_auto_20211020_1509"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteprofiletranslation",
            name="master_agreement",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        )
    ]