# Generated by Django 2.2.7 on 2019-11-19 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cours',
                'verbose_name_plural': 'Courss',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(verbose_name='description')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Niveau',
                'verbose_name_plural': 'Niveaus',
            },
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='specialite/image')),
                ('description', tinymce.models.HTMLField(verbose_name='description')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('id_specialite', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Specialisation',
                'verbose_name_plural': 'Specialisations',
            },
        ),
        migrations.CreateModel(
            name='UserSpecialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialiteuser', to='specialisation.Specialisation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_specialite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserSpecialite',
                'verbose_name_plural': 'UserSpecialites',
            },
        ),
        migrations.CreateModel(
            name='ResultatCompos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rang', models.PositiveIntegerField()),
                ('note', models.FloatField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_resultat', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ResultatCompos',
                'verbose_name_plural': 'ResultatComposs',
            },
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('types', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursressources', to='specialisation.Cours')),
            ],
            options={
                'verbose_name': 'Ressources',
                'verbose_name_plural': 'Ressources',
            },
        ),
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='niveaucours', to='specialisation.Niveau'),
        ),
        migrations.AddField(
            model_name='cours',
            name='specialisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialisation', to='specialisation.Specialisation'),
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cours_composition', to='specialisation.Cours')),
            ],
            options={
                'verbose_name': 'Composition',
                'verbose_name_plural': 'Compositions',
            },
        ),
    ]
