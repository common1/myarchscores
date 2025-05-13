import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import lorem_ipsum
from api.models import User, Archer, Club, Membership

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='test')
            
            
        # Create sample archers
        archers = [
            Archer(
                author=user,
                first_name="Harrie",
                last_name="Smulders",
            ),
            Archer(
                author=user,
                first_name="Piet",
                last_name="Jansen",
            ),
            Archer(
                author=user,
                first_name="Peter",
                last_name="Vanalles",
            ),
        ]

        # create archers & re-fetch from db
        Archer.objects.bulk_create(archers)
        archers = Archer.objects.all()
        
        # Create sample clubs
        clubs = [
            Club(
                name="De Boogschutters", 
                town="Eindhoven", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Pijlen", 
                town="Veldhoven", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Schutters", 
                town="Breda", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Pijl", 
                town="Tilburg", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Boog", 
                town="Den Bosch", 
                info=lorem_ipsum.paragraph()
            ),
        ]
        
        # create clubs & re-fetch from db
        Club.objects.bulk_create(clubs)
        clubs = Club.objects.all()
        
        for archer in archers:
           for club in clubs:
               Membership.objects.create(
                   archer=archer,
                   club=club,
                   start_date="2023-01-01",
                   end_date="2023-12-31",
               )

