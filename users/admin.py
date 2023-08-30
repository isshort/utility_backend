from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User
 
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "fullname",
        "email",
        "phone",
        'is_active'
    )
    list_display_links = ('fullname', 'phone')
    readonly_fields = ('last_login',)
    search_fields = (
        'fullname',
        'phone',
        'email',
        'country__name'
    )
    ordering = ('phone', 'email')

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('fullname', 'email', )}),
         (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', ),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email','password1', 'password2',),
        }),
    )
    date_hierarchy="last_login"
