# flashcards/management/commands/add_tests.py

from django.core.management.base import BaseCommand
from flashcards.models import DifficultyLevel, QuestionType, Test, Question, Answer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        levels = ['Початковий', 'Середній', 'Високий']
        types = ['Питання з відповідями', 'Вставити слово', 'Відповідності']

        for level in levels:
            difficulty = DifficultyLevel.objects.get(name=level)
            for i in range(1, 4):
                test = Test.objects.create(name=f"{level} Test {i}", difficulty=difficulty)

                for t in types:
                    q_type = QuestionType.objects.get(name=t)
                    for j in range(1, 11):
                        question = Question.objects.create(test=test, type=q_type,
                                                           text=f"Question {j} for {level} {t} in Test {i}")

                        for k in range(1, 5):
                            Answer.objects.create(question=question, text=f"Answer {k}", is_correct=(k == 1))

        self.stdout.write(self.style.SUCCESS('Тести успішно додані'))
