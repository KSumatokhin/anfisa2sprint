from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

admin.site.empty_value_display = 'Не задано'


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(
        admin.StackedInline):
    model = IceCream
    # extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    # Какие поля будут показаны на странице списка объектов
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    # Какие поля можно редактировать прямо на странице списка объектов.
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    # Кортеж с перечнем полей, по которым будет проводиться поиск.
    # Форма поиска отображается над списком элементов.
    search_fields = ('title',)
    # Кортеж с полями, по которым можно фильтровать записи.
    # Фильтры отобразятся справа от списка элементов.
    list_filter = ('is_published',)
    # Это свойство определеяет записи при клике на которые можно перейти на
    # страницу просмотра и редактирования записи
    list_display_links = ('title',)
    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Регистрируем кастомное представление админ-зоны
admin.site.register(Category, CategoryAdmin)
admin.site.register(IceCream, IceCreamAdmin)
# Регистрируем модели Topping и Wrapper
admin.site.register(Topping)
admin.site.register(Wrapper)
