from django.contrib import admin


from equation.models import SolvingEquation, Comments


class CommentsAdmin(admin.ModelAdmin):
    """ Admin panel with functionality for working with comments """

    list_display = ('username', 'comment_text', 'created_at')
    list_display_links = ('username',)
    search_fields = ('username', 'comment_text')
    list_editable = ('comment_text',)
    list_filter = ('created_at',)


admin.site.register(Comments, CommentsAdmin)
admin.site.register(SolvingEquation)
