from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse

from .models import Lecture
from .forms import AddLectureForm


class LecturesDetailView(DetailView):
    model = Lecture
    template_name = 'lectures/details_view.html'
    context_object_name = 'lecture'


class LecturesUpdateView(UpdateView):
    model = Lecture
    template_name = 'lectures/add_lecture.html'
    form_class = AddLectureForm


class LecturesDeleteView(DeleteView):
    model = Lecture
    success_url = '/lectures/'
    template_name = 'lectures/news-delete.html'


def lectures_home(request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures/lectures_home.html', {'lectures': lectures})


def create(request):
    if request.user.is_teacher == False:
        messages.error(request, 'Недостаточно прав для выполнения операции')
        return redirect('..')
    if request.method == 'POST':
        form = AddLectureForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # form.creator_id = request.user
            # form.save()
            lecture = form.save(commit=False)
            lecture.creator = request.user
            # lecture.video_url = lecture.video_url[0:12:-1]
            lecture.save()
            messages.success(request, 'Вы успешно добавили лекцию')
            return redirect('..')
    else:
        form = AddLectureForm()
    
    context = {'form': form}
    return render(request, 'lectures/add_lecture.html', context)
