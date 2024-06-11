from django.urls import path, include  # Додайте include до імпортів
from .views import beginner_pack_words
from .views import index, flashcards, create_flashcard, tests, login_view, logout_view, signup_view, mini_dictionary, packs
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('flashcards/', flashcards, name='flashcards'),
    path('create_flashcard/', create_flashcard, name='create_flashcard'),
    path('tests/', tests, name='tests'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Використовуйте ваш новий view для виходу з системи тут
    path('signup/', signup_view, name='signup'),
    path('mini_dictionary/', mini_dictionary, name='mini_dictionary'),
    path('api/beginner_pack_words/', beginner_pack_words, name='beginner_pack_words'),
    path('save_favorite/', views.save_favorite, name='save_favorite'),
    path('get_favorites/', views.get_favorites, name='get_favorites'),
    path('english-level-test/', views.english_level_test, name='english_level_test'),
    path('vocabulary_test/', views.vocabulary_test, name='vocabulary_test'),  # Новий маршрут
    path('packs/', packs, name='packs'),
    path('add_pack/', views.add_pack, name='add_pack'),  # Додайте цей рядок для обробки додавання нового пака
    path('dictionary/', views.dictionary, name='dictionary'),  # Додайте маршрут для сторінки словника

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
