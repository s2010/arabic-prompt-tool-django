from django.db import models
from django.contrib.auth.models import User # Using Django's built-in User model

class Prompt(models.Model):
    """Represents an Arabic AI prompt."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False) # For moderation

    def __str__(self):
        return self.title

class Upvote(models.Model):
    """Represents a user's upvote on a prompt."""
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure a user can only upvote a prompt once
        unique_together = ('prompt', 'user')

    def __str__(self):
        return f"{self.user.username} upvoted {self.prompt.title}"

from django.db import models

# Create your models here.
