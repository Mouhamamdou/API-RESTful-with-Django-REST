from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from trackproblem.models import Project, Issue

PROJECTS = [
                {
                        'title': 'Projet A',
                        'description': 'Description du Projet A',
                        'type': 'iOS',
                        'issues': [
                            {'titre': 'Issue 1 du Projet A', 'description': 'Détail de l\'issue 1'},
                            {'titre': 'Issue 2 du Projet A', 'description': 'Détail de l\'issue 2'},
                        ]
                    },
                    # Ajoutez d'autres projets ici
]

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'


class Command(BaseCommand):

    help = 'Initialise les données pour le développement local'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Initialisation des données..."))

        UserModel = get_user_model()
        superuser = UserModel.objects.get(username=ADMIN_USERNAME)

        # Suppression des données existantes
        Project.objects.all().delete()

        # Initialisation des nouveaux données
        for project_data in PROJECTS:
            project = Project.objects.create(
                title=project_data['title'],
                description=project_data['description'],
                type=project_data['type'],
                author=superuser
            )
            for issue_data in project_data['issues']:
                Issue.objects.create(
                    project=project,
                    titre=issue_data['titre'],
                    description=issue_data['description'],
                    author=superuser
                )

