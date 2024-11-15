from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic

from lectures.forms import CreateLectureForm
from lectures.models import Lecture


class CreateLecture(LoginRequiredMixin, generic.CreateView):
    form_class = CreateLectureForm
    template_name = 'lectures/create_lecture.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@login_required
def delete_view(request, pk):
    obj = get_object_or_404(Lecture, pk=pk)
    context = {'resource': obj}
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("courses:list"))
    return render(request, "lectures/delete_confirm_lecture.html", context)