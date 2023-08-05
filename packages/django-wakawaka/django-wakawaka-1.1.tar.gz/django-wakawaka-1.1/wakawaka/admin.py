from __future__ import unicode_literals

from django.contrib import admin

from wakawaka.models import WikiPage, Revision


class RevisionInlines(admin.TabularInline):
    model = Revision
    extra = 1


class WikiPageAdmin(admin.ModelAdmin):
    inlines = [RevisionInlines]


class RevisionAdmin(admin.ModelAdmin):
    pass


admin.site.register(WikiPage, WikiPageAdmin)
admin.site.register(Revision, RevisionAdmin)
