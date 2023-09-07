from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.models import User, Group


from .filters import InformsFilter
from .forms import NA_Form
from .models import Inform



@login_required()
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name = 'authors').exists():
        authors_group.user_ser.add(user)
    return redirect('/inform/search/')




class InformsList(ListView):
    model = Inform
    ordering = 'name'
    template_name = 'an_search_all.html'
    context_object_name = 'informs'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = InformsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['filterset'] = self.filterset
      return context


class NA_Detail(DetailView):
   model = Inform
   template_name = 'an_search.html'
   context_object_name = 'one_object'


class NA_Create(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('forms.na_create',)
    form_class = NA_Form
    model = Inform
    template_name = 'na_create.html'

    def form_valid(self, form):
       post = form.save(commit=True)
       # post.categoryType = 'NW'
       return super().form_valid(form)

class NA_Delete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('forms.na_delete',)
    model = Inform
    template_name = 'na_delete.html'
   # success_url = reverse_lazy('product_list')
    success_url = reverse_lazy('an_search_all')


class NA_Update(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('forms.na_edit',)
    form_class = NA_Form
    model = Inform
    template_name = 'na_edit.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Inform.objects.get(pk=id)