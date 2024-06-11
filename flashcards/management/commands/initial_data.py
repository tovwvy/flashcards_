# flashcards/management/commands/initial_data.py

from django.core.management.base import BaseCommand
from flashcards.models import DifficultyLevel, QuestionType

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        DifficultyLevel.objects.get_or_create(name='Початковий')
        DifficultyLevel.objects.get_or_create(name='Середній')
        DifficultyLevel.objects.get_or_create(name='Високий')

        QuestionType.objects.get_or_create(name='Питання з відповідями')
        QuestionType.objects.get_or_create(name='Вставити слово')
        QuestionType.objects.get_or_create(name='Відповідності')

        self.stdout.write(self.style.SUCCESS('Початкові дані успішно додані'))
