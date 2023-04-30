from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Player


@receiver(user_logged_in)
def create_player(sender, request, user, **kwargs):
    # Check if the player already exists
    if not hasattr(user, 'player'):
        # Create a new player instance for the user
        player = Player(user=user, name=user.username)
        player.save()
