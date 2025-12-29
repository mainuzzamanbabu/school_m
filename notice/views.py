from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from notice.models import Notice


class NoticeListView(ListView):
    template_name = "notice_list.html"
    model = Notice
    context_object_name = "notices"
    paginate_by = 10
    ordering = ["-created_at"]


class NoticeDetailView(DetailView):
    template_name = "notice_detail.html"
    model = Notice
    context_object_name = "notice"


class NoticeCreateView(CreateView):
    template_name = "notice_form.html"
    model = Notice
    fields = ["title", "body"]
    success_url = reverse_lazy("notices")
    extra_context = {"page_title": "Add Notice"}


class NoticeUpdateView(UpdateView):
    template_name = "notice_form.html"
    model = Notice
    fields = ["title", "body"]
    success_url = reverse_lazy("notices")
    extra_context = {"page_title": "Edit Notice"}


class NoticeDeleteView(DeleteView):
    template_name = "notice_confirm_delete.html"
    model = Notice
    success_url = reverse_lazy("notices")
    context_object_name = "notice"
