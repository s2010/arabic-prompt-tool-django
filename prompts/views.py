# prompts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count, Exists, OuterRef, Q
# We might not need Case, When, Value, BooleanField with this approach,
# but let's keep the import for now in case other parts of the code use them.
from django.db.models import Case, When, Value, BooleanField
from .forms import PromptForm
from .models import Prompt, Upvote



def home(request):
    """Basic home page view."""
    # Annotate prompts with upvote count and whether the current user has upvoted
    approved_prompts = Prompt.objects.filter(is_approved=True).annotate(
        upvote_count=Count('upvotes'), # Annotate with total upvote count
        # Check if an Upvote exists for this prompt and the current authenticated user
        # Use a Python conditional to pass the user object or None to the filter
        user_has_upvoted=Exists(
            Upvote.objects.filter(
                prompt=OuterRef('pk'),
                user=request.user if request.user.is_authenticated else None # <-- Ensure this line is correct
            )
        )
    ).order_by('-created_at')

    return render(request, 'home.html', {'prompts': approved_prompts})

@login_required
def submit_prompt(request):
    """View for submitting a new prompt."""
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save(commit=False)
            prompt.author = request.user
            prompt.save()
            return redirect('home')
    else:
        form = PromptForm()

    return render(request, 'prompts/submit_prompt.html', {'form': form})


def search_prompts(request):
    """View to handle HTMX search requests and return filtered prompts."""
    query = request.GET.get('q', '') # Get the search query from GET parameters
    approved_prompts = Prompt.objects.filter(is_approved=True).annotate(
        upvote_count=Count('upvotes'),
        # Apply the same Python conditional annotation for search results
        user_has_upvoted=Exists(
            Upvote.objects.filter(
                prompt=OuterRef('pk'),
                user=request.user if request.user.is_authenticated else None
            )
        )
    ).filter( # Add filtering based on the query
        Q(title__icontains=query) | Q(content__icontains=query) # Search in title or content (case-insensitive)
    ).order_by('-created_at')

    # Render only the list snippet
    return render(request, 'prompts/prompt_list.html', {'prompts': approved_prompts})

@login_required
def upvote_prompt(request, prompt_id): # Ensure this function exists and is named correctly
    """View to handle upvoting/un-upvoting a prompt via HTMX."""
    if request.method == 'POST':
        # ... (upvote logic) ...
        pass
    else:
        return HttpResponse(status=405)
