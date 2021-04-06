# Generated by Django 2.2.6 on 2019-10-28 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('points', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('team_home_goals', models.BigIntegerField(blank=True, null=True)),
                ('team_away_goals', models.BigIntegerField(blank=True, null=True)),
                ('team_away', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_away', to='football.Team')),
                ('team_home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games_home', to='football.Team')),
            ],
        ),
    ]
