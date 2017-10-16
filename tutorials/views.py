from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import TutorialSeries, Lesson
# Create your views here.

def tutorial_series_detail(request,slug):
    series = get_object_or_404(TutorialSeries,slug=slug)
    lesson = series.lesson_set.filter(tutorial_series = series)
    template = 'tutorials/tutorialseries_detail.html'
    context = {
        'series' : series,
        'lesson' : lesson
    }
    return render(request,template,context)

# class TutorialSeriesDetailView(DetailView):
#     model = TutorialSeries
#     template_name = 'tutorials/tutorialseries_detail.html'

#     def get_context_data(self, **kwargs):

#         context = super(TutorialSeriesDetailView,self).get_context_data(**kwargs)
#         context['lessons'] = Lesson.objects.filter(tutorial_series__name= self.object)
#         return context

def lessons_detail(request, tutorial_series, slug):
    object = get_object_or_404(Lesson.objects.filter(tutorial_series__slug = tutorial_series, slug=slug))

    template = 'tutorials/lesson_detail.html'

    context = {
        'objects':object
    }
    return render(request, template, context)
