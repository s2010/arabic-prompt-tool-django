# prompts/management/commands/seed_prompts.py
import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from prompts.models import Prompt # Import your Prompt model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with initial prompts from a CSV file if the Prompt table is empty.'

    def handle(self, *args, **options):
        # Define the path to the CSV file inside the container
        # This assumes your CSV is at the project root on the host,
        # mounted to /app in the container.
        csv_file_path = '/app/sead_prompts.csv'

        # Check if the Prompt table is empty
        if Prompt.objects.exists():
            self.stdout.write(self.style.SUCCESS('Prompt table is not empty. Skipping seeding.'))
            return

        # Check if the CSV file exists
        if not os.path.exists(csv_file_path):
            raise CommandError(f'CSV file not found at {csv_file_path}')

        self.stdout.write(self.style.MIGRATE_HEADING(f'Seeding prompts from {csv_file_path}...'))

        try:
            # Find the superuser to assign as the author
            # Assumes at least one superuser exists
            superuser = User.objects.filter(is_superuser=True).first()
            if not superuser:
                 raise CommandError('No superuser found. Please create a superuser first.')

            with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                prompts_to_create = []
                for row in reader:
                    # Assuming your CSV has '\ufefftitle' and 'prompt' columns based on your error log
                    # Corrected to match the keys found in the user's error output
                    title = row.get('\ufefftitle')
                    content = row.get('prompt')

                    if not title or not content:
                        self.stdout.write(self.style.WARNING(f'Skipping row due to missing data: {row}'))
                        continue

                    prompts_to_create.append(
                        Prompt(
                            title=title,
                            content=content,
                            author=superuser, # Assign superuser as author
                            is_approved=True # Optionally set seeded prompts as approved
                        )
                    )

                # Bulk create the prompts for efficiency
                Prompt.objects.bulk_create(prompts_to_create)

            self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(prompts_to_create)} prompts.'))

        except Exception as e:
            raise CommandError(f'Error seeding prompts: {e}')
