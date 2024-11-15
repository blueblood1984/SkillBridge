# Generated by Django 5.1.1 on 2024-11-12 08:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='score',
        ),
        migrations.AddField(
            model_name='transcripts',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transcripts',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transcripts', to='quizzes.quiz'),
        ),
    ]
