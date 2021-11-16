from django.contrib import admin

from .models import Post, Comment
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    list_display = ('__str__', 'title', 'photo', 'photographer', 'created', 'modified')
    readonly_fields = ('created', 'modified')
    list_editable = ('title', 'photo', 'photographer')
    search_fields = (
        'profile__user__email',
        'profile__user__username',
        'profile__user__first_name',
        'profile__user__last_name',
        'title'
    )
    list_filter = (
        'profile__user__is_active',
        'profile__user__is_staff',
        'created',
        'modified',
    )


admin.site.register(Comment)