# Generated by Django 5.0.6 on 2024-05-20 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100)),
                ('ukrainian', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=100)),
                ('ukrainian_word', models.CharField(max_length=100)),
                ('english_word', models.CharField(max_length=100)),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='flashcards.pack')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ukrainian', models.CharField(max_length=100)),
                ('english', models.CharField(max_length=100)),
                ('pack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards.pack')),
            ],
        ),
    ]
