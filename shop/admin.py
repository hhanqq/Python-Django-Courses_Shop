from django.contrib import admin
from . import models

admin.site.site_header = 'Courses Administration'
admin.site.site_title = 'My Courses'
admin.site.index_title = 'Welcome to the Courses admin Area'

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')

class CoursesInline(admin.TabularInline):
    model = models.Course
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']})
    ]
    inlines = [CoursesInline]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
