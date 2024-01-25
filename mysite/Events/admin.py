from django.contrib import admin

# Register your models here.
from .models import venue, MyclubUser, Events


# admin.site.register(venue)
@admin.register(venue)
class venueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'web', 'email_address')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Events)
class venue(admin.ModelAdmin):
    search_fields = ('name', 'address')
# admin.site.register(Events)


class EventAdmin(admin.ModelAdmin):
    # fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name', 'venue'), 'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description', 'manager')

        }),
    )

admin.site.register(MyclubUser)
# admin.site.register(Events)
