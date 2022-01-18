# Generated by Django 3.1.13 on 2021-12-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_project_reveal_preannotations_interactively'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='parsed_label_config',
            field=models.TextField(blank=True, default='', help_text='Parsed label config in JSON format. See more about it in documentation', null=True, verbose_name='parsed label config'),
        ),
    ]