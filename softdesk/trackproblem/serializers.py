from rest_framework import serializers
from .models import Project, Issue, Comment
from authentication.models import User


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author', 'created_time']


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    contributors = serializers.SerializerMethodField()
    issues = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author', 'contributors', 'issues', 'created_time']

    def get_contributors(self, obj):
        return [contributor.username for contributor in obj.contributors.all()]

    def get_issues(self, obj):
        queryset = obj.issues.all()
        serializer = IssueSerializer(queryset, many=True)
        return serializer.data


class IssueListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'project', 'titre', 'description', 'priority', 'balise', 'status', 'created_time']


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    project = serializers.SlugRelatedField(slug_field='title', queryset=Project.objects.all())
    contributor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Issue
        fields = ['id', 'project', 'titre', 'description', 'author', 'contributor', 'priority', 'balise', 'status',
                  'comments', 'created_time']

    def validate(self, data):
        project = data.get('project')
        contributor = data.get('contributor')

        if not project.contributors.filter(id=contributor.id).exists():
            raise serializers.ValidationError("Le contributeur doit faire partie des contributeurs du projet.")

        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'issue', 'description', 'created_time']
        read_only_fields = ['author']
