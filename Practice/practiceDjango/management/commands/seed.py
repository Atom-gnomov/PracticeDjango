# practiceDjango/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from practiceDjango.models import Task, Tag
import random

class Command(BaseCommand):
    help = 'Populate the database with sample Tasks and Tags'

    def handle(self, *args, **options):
        # Define some sample tag names
        tag_names = ['urgent', 'home', 'work', 'personal', 'important']

        # Create or get tags
        tags = []
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created tag: {name}"))

        # Clear existing tasks (optional)
        Task.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing tasks."))

        # Create sample tasks
        for i in range(1, 11):
            content = f"Sample Task {i}"
            # Deadlines spaced a day apart from now
            deadline = timezone.now() + timezone.timedelta(days=i)
            done = random.choice([True, False])

            task = Task.objects.create(content=content, deadline=deadline, done=done)

            # Assign 1-3 random tags
            selected = random.sample(tags, k=random.randint(1, 3))
            task.tags.set(selected)

            self.stdout.write(self.style.SUCCESS(
                f"Created task: {task.content} | deadline: {task.deadline:%Y-%m-%d} | done: {task.done} | tags: {[t.name for t in selected]}"
            ))

        self.stdout.write(self.style.SUCCESS("Database population complete."))
