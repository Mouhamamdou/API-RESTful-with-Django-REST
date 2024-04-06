from rest_framework import serializers
from .models import Project, Issue, Comment
from authentication.models import User


class ProjectListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author', 'created_time']


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    contributors = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), required=False, many=True)
    issues = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author', 'contributors', 'issues', 'created_time']

    def get_issues(self, obj):
        return [{'id': issue.id, 'titre': issue.titre} for issue in obj.issues.all()]


class IssueListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'titre', 'description', 'status', 'created_time']


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    project = serializers.SlugRelatedField(slug_field='title', queryset=Project.objects.all())
    contributor = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), allow_null=True, required=False)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'project', 'titre', 'description', 'author', 'contributor', 'priority', 'balise', 'status',
                  'comments', 'created_time']

    def validate(self, data):
        project = self.instance.project
        contributor = data.get('contributor')

        if contributor and not project.contributors.filter(id=contributor.id).exists():
            raise serializers.ValidationError("Le contributeur doit faire partie des contributeurs du projet.")

        return data


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    issue = serializers.SlugRelatedField(slug_field='titre', queryset=Issue.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'author', 'issue', 'description', 'created_time']
        read_only_fields = ['author']
