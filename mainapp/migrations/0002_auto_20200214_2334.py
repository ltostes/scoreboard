# Generated by Django 3.0.2 on 2020-02-14 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=5000, null=True)),
                ('first_second_draw', models.BooleanField(default=False)),
                ('second_third_draw', models.BooleanField(default=False)),
                ('third_fourth_draw', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('started', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('playoff_round', models.IntegerField(default=1)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, max_length=5000, null=True)),
                ('subscription_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('confirmation_at', models.DateTimeField(blank=True, null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Edition')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_category', models.CharField(blank=True, max_length=100, null=True)),
                ('scoring_method', models.CharField(choices=[('P', 'Points'), ('W', 'Win or Lose')], default='W', max_length=1)),
                ('playoffs', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
        migrations.AddField(
            model_name='player',
            name='description',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='team',
            name='anthem',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scored', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Participant')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Score')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Player'),
        ),
        migrations.AddField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Team'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('about', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_note', to='mainapp.Participant')),
                ('taken_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='takenby_note', to='mainapp.Participant')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Edition'),
        ),
        migrations.AddField(
            model_name='competition',
            name='fourth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fourth_placed_competition', to='mainapp.Team'),
        ),
        migrations.AddField(
            model_name='competition',
            name='second',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_placed_competition', to='mainapp.Team'),
        ),
        migrations.AddField(
            model_name='competition',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Sport'),
        ),
        migrations.AddField(
            model_name='competition',
            name='third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third_placed_competition', to='mainapp.Team'),
        ),
        migrations.AddField(
            model_name='competition',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner_competition', to='mainapp.Team'),
        ),
    ]