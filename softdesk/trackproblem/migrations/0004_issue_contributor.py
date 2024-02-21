# Generated by Django 5.0.2 on 2024-03-12 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackproblem', '0003_alter_comment_author_alter_comment_issue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='contributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributed_issue', to='trackproblem.contributor'),
        ),
    ]