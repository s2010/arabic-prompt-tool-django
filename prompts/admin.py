# prompts/admin.py
from django.contrib import admin
from .models import Prompt

@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    actions = ['approve_prompts'] # Add a custom action

    def approve_prompts(self, request, queryset):
        queryset.update(is_approved=True)
    approve_prompts.short_description = "Mark selected prompts as approved"

# You can register the Upvote model here later if needed
# from .models import Upvote
# admin.site.register(Upvote)
