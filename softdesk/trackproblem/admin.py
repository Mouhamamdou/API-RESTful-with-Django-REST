from django.contrib import admin
from .models import Project, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')


class IssueAdmin(admin.ModelAdmin):

    list_display = ('titre', 'description', 'author')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'issue', 'project')

    @admin.display(description='Project')
    def project(self, obj):
        return obj.issue.project


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
