# Generated by Django 4.1.3 on 2025-01-12 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='نمره')),
                ('date_taken', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آزمون')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Question Body')),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('author', models.CharField(max_length=255, verbose_name='نویسنده')),
                ('category', models.CharField(max_length=100, verbose_name='دسته\u200cبندی')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exams', models.ManyToManyField(related_name='reports', to='group9.exam', verbose_name='آزمون\u200cها')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='report', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='نمره')),
                ('date_completed', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ تکمیل')),
                ('questions', models.ManyToManyField(related_name='exercises', to='group9.question', verbose_name='سوالات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(related_name='exams', to='group9.question', verbose_name='سوالات'),
        ),
        migrations.AddField(
            model_name='exam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
