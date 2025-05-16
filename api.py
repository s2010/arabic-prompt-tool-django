# api.py
from fastapi import FastAPI, HTTPException # Import HTTPException
from pydantic import BaseModel # Import BaseModel
from typing import List # Import List
from django.db.models import Count
# Import your Django models
from prompts.models import Prompt, Upvote
from django.contrib.auth.models import User

# Create a FastAPI application instance
api_app = FastAPI()

# Define Pydantic models for data validation and serialization
class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True # Allow Pydantic to read from Django ORM models

class PromptBase(BaseModel):
    title: str
    content: str
    is_approved: bool

    class Config:
        orm_mode = True # Allow Pydantic to read from Django ORM models

class PromptList(PromptBase):
    id: int
    author: UserBase # Include author information
    upvote_count: int = 0 # Add upvote count, default to 0
    # user_has_upvoted is specific to the requesting user, might not include in general list API

class PromptDetail(PromptList):
    created_at: str # Represent datetime as string
    updated_at: str # Represent datetime as string


# Define an app_name for Django's include (although we are mounting via asgi.py now,
# keeping this doesn't hurt and might be useful if you change routing later)
# app_name = "api" # Removed this line in previous step, keep it removed


@api_app.get("/health/")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "message": "FastAPI is running!"}

# Add a FastAPI endpoint to list approved prompts
@api_app.get("/prompts/", response_model=List[PromptList])
async def list_prompts():
    """List all approved prompts with upvote counts."""
    # Use Django ORM to fetch approved prompts and annotate upvote count
    approved_prompts = Prompt.objects.filter(is_approved=True).annotate(
        upvote_count=Count('upvotes')
    ).order_by('-created_at')

    # Convert Django querySet to a list of dictionaries for Pydantic
    # Pydantic with orm_mode=True can often handle querysets directly,
    # but explicit conversion can sometimes be clearer or necessary.
    # Let's try passing the queryset directly first.
    return approved_prompts


# Add a FastAPI endpoint to get a single prompt by ID
@api_app.get("/prompts/{prompt_id}", response_model=PromptDetail)
async def get_prompt(prompt_id: int):
    """Get a single approved prompt by ID."""
    # Fetch the prompt, ensuring it's approved and annotating upvote count
    prompt = Prompt.objects.filter(id=prompt_id, is_approved=True).annotate(
        upvote_count=Count('upvotes')
    ).first() # Use .first() as we expect at most one result

    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found or not approved")

    return prompt


# You will define other FastAPI endpoints here later
# e.g., for submitting prompts via API (requires authentication)
# @api_app.post("/prompts/")
# async def create_prompt(...):
#     pass
