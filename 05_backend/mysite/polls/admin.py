from django.contrib import admin

from .models import Question, Choice

# Dodaj:
# - wyszukiwanie
# - filtrowanie po dacie
# - filtrowanie po pozostałych polach
# - pobrania zależnych modeli
# - sortowanie

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']


# - autouzupełnianie
class ChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
