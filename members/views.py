from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from members.models import Member

class MemberListView(ListView):
    template_name = "members.html"
    model = Member
    context_object_name = "members"
    paginate_by = 6

    def get_queryset(self):
        queryset = Member.objects.all()

        member_type = self.request.GET.get("type")

        if member_type:
            queryset = queryset.filter(member_type=member_type)

        return queryset


class MemberDetailView(DetailView):
    template_name = "member_detail.html"
    model = Member
    context_object_name = "member"


class MemberCreateView(CreateView):
    template_name = "member_form.html"
    model = Member
    fields = [
        "member_type",
        "name",
        "designation",
        "department",
        "email",
        "phone",
        "photo",
    ]
    success_url = reverse_lazy("members")
    extra_context = {"page_title": "Add Member"}


class MemberUpdateView(UpdateView):
    template_name = "member_form.html"
    model = Member
    fields = [
        "member_type",
        "name",
        "designation",
        "department",
        "email",
        "phone",
        "photo",
    ]
    success_url = reverse_lazy("members")
    extra_context = {"page_title": "Edit Member"}


class MemberDeleteView(DeleteView):
    template_name = "member_confirm_delete.html"
    model = Member
    success_url = reverse_lazy("members")
    context_object_name = "member"
