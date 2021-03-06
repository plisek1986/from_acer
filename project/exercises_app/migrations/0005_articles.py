# Generated by Django 3.1.7 on 2021-03-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=64, null=True)),
                ('content', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('inprogress', 'w trakcie pisania'), ('waiting', 'czeka na akceptację'), ('published', 'opublikowany')], max_length=10)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
    ]
