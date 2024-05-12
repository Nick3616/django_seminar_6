from django.contrib import admin
from .models import Category, Product

@admin.action(description='Установить цену 0')
def set_price_zero(modeladmin, request, queryset):
    queryset.update(price=0)

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ('name', 'price', 'quantity', 'date', 'category', 'image')
    ordering = ('category', '-quantity')
    list_filter = ('date', 'price', 'category')
    search_fields = ('name',)
    actions = [set_price_zero]

    readonly_fields = ('rating', 'date')
    fieldsets = [
        (
        None,
        {
            'fields': ['name']
        },
         ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Описание продукта',
                'fields': ['category', 'description']
            },
        ),
        (
            'Цена и количество',
            {
                'fields': ['price', 'quantity']
            }
        ),
        (
            'Рейтинг и прочие',
            {
                'fields': ['rating', 'date', 'image']
            }
        )
    ]
       

    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

