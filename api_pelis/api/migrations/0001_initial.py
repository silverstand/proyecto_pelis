# Generated by Django 2.2.3 on 2019-11-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('estreno', models.IntegerField(default=2000)),
                ('imagen', models.URLField(help_text='De imdb mismo')),
                ('resumen', models.TextField(help_text='Descripción corta')),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
    ]
