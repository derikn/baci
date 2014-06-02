from __future__ import absolute_import

from django.db.models import Count
from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from braces import views
from . import models
from . import forms

class AssetListView(
	views.LoginRequiredMixin,
	views.PermissionRequiredMixin,
	generic.ListView,):
    model = models.Asset
    permission_required = "assetdb.add_asset"
    template_name = "assetdb/asset_list.html"

class AssetCreateView(
	views.LoginRequiredMixin,
	views.SetHeadlineMixin,
	views.PermissionRequiredMixin,
	generic.CreateView):

	form_class = forms.AssetForm
	headline = 'Create'
	model = models.Asset
	permission_required = "assetdb.add_asset"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(AssetCreateView, self).form_valid(form)

class AssetUpdateView(
	views.LoginRequiredMixin,
	views.SetHeadlineMixin,
	views.PermissionRequiredMixin,
	generic.UpdateView):
	
	template_name_suffix = '_update_form'
	form_class = forms.AssetForm
	headline = 'Update'
	model = models.Asset
	permission_required = "assetdb.add_asset"


class AssetDetailView(
	views.LoginRequiredMixin,
    views.PrefetchRelatedMixin,
    generic.DetailView
):

    form_class = forms.TicketForm
    http_method_names = ['get', 'post']
    model = models.Asset

    def get(self, request, *args, **kwargs):
    	self.object = self.get_object()
    	if not self.object.public:
    		return HttpResponseRedirect(reverse('assetdb:list'))
    	else:
    		context = self.get_context_data(object=self.object)
    		return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context.update({'form': self.form_class(self.request.POST or None)})
        event = self.object
        context['ticket_count'] = asset.tickets.count()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = self.get_object()
            ticket = form.save(commit=False)
            ticket.asset = obj
            ticket.save()
        else:
            return self.get(request, *args, **kwargs)
        return redirect(obj)

# Create your views here.
class AssetDeleteView(generic.DeleteView,
	views.PermissionRequiredMixin,
	views.LoginRequiredMixin):
	#set the reference model
	model = models.Asset

	permission_required = "assetdb.delete_asset"

	#pass attendee's parent event id to kwargs
	def get_success_url(self):
		return reverse('assetdb:list')