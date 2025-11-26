from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='marvel')
        self.assertEqual(user.name, 'Test Hero')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='marvel')
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-11-26')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='marvel', description='Marvel Superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
