from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from routine.forms import RoutineForm
from routine.models import Routine


class RoutineListView(ListView):
    template_name = "routine_list.html"
    model = Routine
    context_object_name = "routines"
    paginate_by = 10

    def get_queryset(self):
        queryset = Routine.objects.all()

        day = self.request.GET.get("day")
        class_name = self.request.GET.get("class")

        if day:
            queryset = queryset.filter(day=day)
        if class_name:
            queryset = queryset.filter(class_name__icontains=class_name)

        return queryset


class RoutineDetailView(DetailView):
    template_name = "routine_detail.html"
    model = Routine
    context_object_name = "routine"


class RoutineCreateView(CreateView):
    template_name = "routine_form.html"
    model = Routine
    form_class = RoutineForm
    success_url = reverse_lazy("routines")
    extra_context = {"page_title": "Add Routine"}


class RoutineUpdateView(UpdateView):
    template_name = "routine_form.html"
    model = Routine
    form_class = RoutineForm
    success_url = reverse_lazy("routines")
    extra_context = {"page_title": "Edit Routine"}


class RoutineDeleteView(DeleteView):
    template_name = "routine_confirm_delete.html"
    model = Routine
    success_url = reverse_lazy("routines")
    context_object_name = "routine"
