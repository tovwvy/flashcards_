from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import FlashcardForm, MyCustomLoginForm, MyCustomUserCreationForm
from .models import Flashcard, Pack
from django.shortcuts import render
from .forms import FlashcardForm, PackChoiceForm
from django.http import JsonResponse
from .models import FavoriteCard
import json


def index(request):
    return render(request, 'index.html')


def flashcards(request):
    # Отримуємо пак "Початковий" з бази даних
    beginner_pack = Pack.objects.get(name="Початковий")
    # Фільтруємо флеш-картки за паком "Початковий"
    flashcards = Flashcard.objects.filter(pack=beginner_pack)
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcards')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards.html', {'form': form, 'flashcards': flashcards})

def create_flashcard(request):
    if request.method == 'POST':
        flashcard_form = FlashcardForm(request.POST)
        pack_form = PackChoiceForm(request.POST)

        if flashcard_form.is_valid() and pack_form.is_valid():
            flashcard = flashcard_form.save(commit=False)
            flashcard.user = request.user
            flashcard.save()

            pack = pack_form.cleaned_data['pack']  # Отримуємо обраний пак з форми
            pack.flashcards.add(flashcard)
            return redirect('flashcards')

    else:
        flashcard_form = FlashcardForm()
        pack_form = PackChoiceForm()  # Ініціалізуємо форму для вибору пака

    return render(request, 'create_flashcard.html', {'flashcard_form': flashcard_form, 'pack_form': pack_form})
def tests(request):
    return render(request, 'tests.html')


def login_view(request):
    if request.method == 'POST':
        form = MyCustomLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = MyCustomLoginForm(request)
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def signup_view(request):
    if request.method == 'POST':
        form = MyCustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MyCustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def mini_dictionary(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'mini_dictionary.html', {'flashcards': flashcards})


def my_flashcards(request):
    user_flashcards = Flashcard.objects.filter(user=request.user)
    return render(request, 'my_flashcards.html', {'user_flashcards': user_flashcards})

def beginner_pack_words(request):
    beginner_pack = Pack.objects.get(name="Початковий")
    flashcards = Flashcard.objects.filter(category="Початковий")
    words_list = [{'ukrainian': flashcard.ukrainian, 'english': flashcard.english} for flashcard in flashcards]
    return JsonResponse(words_list, safe=False)


def save_favorite(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            english = data.get('english')
            ukrainian = data.get('ukrainian')
            if english and ukrainian:
                # Перевірка чи вже існує така картка
                if not FavoriteCard.objects.filter(english=english, ukrainian=ukrainian).exists():
                    favorite_card = FavoriteCard(english=english, ukrainian=ukrainian)
                    favorite_card.save()
                    return JsonResponse({'status': 'success'}, status=201)
                return JsonResponse({'status': 'error', 'message': 'Flashcard already exists'}, status=400)
            return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def get_favorites(request):
    if request.method == 'GET':
        favorites = FavoriteCard.objects.all().values('english', 'ukrainian')
        return JsonResponse(list(favorites), safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def english_level_test(request):
    if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        # Перевірка відповідей та визначення рівня англійської мови
        # Додайте ваш код перевірки тут і визначте рівень англійської мови
        # Зазвичай це залежить від кількості правильних відповідей

        # Повернення результатів тесту на сторінку
        return render(request, 'english_level_test.html', {'test_results': 'Intermediate'})  # Змініть на свої дані

    # Якщо метод не POST, поверніть порожню сторінку
    return render(request, 'english_level_test.html')

def vocabulary_test(request):  # Нове представлення
    return render(request, 'vocabulary_test.html')


def packs(request):
    # Логіка для відображення списку паків
    return render(request, 'packs.html')

def add_pack(request):
    if request.method == 'POST':
        # Отримати дані форми з запиту
        pack_name = request.POST.get('pack-name', '')
        pack_description = request.POST.get('pack-description', '')

        # Зберегти пак у базі даних або виконати інші необхідні дії

        # Повернути відповідь у форматі JSON
        return JsonResponse({'success': True})  # Повернути успішну відповідь

    else:
        return JsonResponse({'success': False})  # Повернути помилку, якщо метод запиту не POST

def dictionary(request):
    # Ваш код для обробки запиту та відображення сторінки словника
    return render(request, 'dictionary.html')