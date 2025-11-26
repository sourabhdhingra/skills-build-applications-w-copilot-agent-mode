from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2025-11-26')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2025-11-25')
        Activity.objects.create(user=users[2], type='swim', duration=60, date='2025-11-24')
        Activity.objects.create(user=users[3], type='yoga', duration=50, date='2025-11-23')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body strength', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Core strength', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
