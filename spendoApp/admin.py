from django.contrib import admin
from .models import Categories, Register, User, Ticket, TicketType

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'monto', 'descripcion', 'categoria')
    search_fields = ['monto']

admin.site.register(Register, RegisterAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'medida')
    search_fields = ['nombre', 'medida']

admin.site.register(Categories, CategoriaAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'permissions_level', 'created_at')
    search_fields = ['nombre', 'medida']

admin.site.register(User, UserAdmin)

class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']

admin.site.register(TicketType, TicketTypeAdmin)    

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'ticket_type', 'user', 'description', 'screenshot')
    search_fields = ['title', 'ticket_type', 'user', 'description']

admin.site.register(Ticket, TicketAdmin)    

