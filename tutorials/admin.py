from django.contrib import admin
from .models import Language,StudentExperience,TutorialSeries,Lesson
# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name','active',)

admin.site.register(Language, LanguageAdmin)
admin.site.register(StudentExperience)

class TutorialSeriesAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name','archived',)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)

class LessonAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title','active','free_preview',)
admin.site.register(Lesson, LessonAdmin)