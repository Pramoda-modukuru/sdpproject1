# Generated by Django 5.0 on 2024-02-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module1', '0003_form_delete_feedbackform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='comments',
            field=models.CharField(max_length=100),
        ),
    ]
