from django.contrib.auth.models import User
from django.db import models

class Flashcard(models.Model):
    category = models.CharField(max_length=100, default='')  # Встановлюємо значення за замовчуванням
    pack = models.ForeignKey('Pack', on_delete=models.CASCADE, related_name='flashcards')
    ukrainian_word = models.CharField(max_length=100)
    english_word = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ukrainian_word} - {self.english_word}"



class Pack(models.Model):
    name = models.CharField(max_length=100)

class Word(models.Model):
    pack_id = models.ForeignKey(Pack, on_delete=models.CASCADE)
    ukrainian = models.CharField(max_length=100)
    english = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ukrainian} - {self.english}"

class FavoriteCard(models.Model):
    english = models.CharField(max_length=100)
    ukrainian = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.english} - {self.ukrainian}"
