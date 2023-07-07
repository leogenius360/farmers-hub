from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . models import Product, Store
from . forms import BusinessRegistrationForm


class RegisterBusinessView(LoginRequiredMixin, generic.CreateView):
    template_name = "dashboard/register.html"
    form_class = BusinessRegistrationForm
    model = Store
    success_url = reverse_lazy('admin')

register = RegisterBusinessView.as_view()


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/index.html"
    # form_class = BusinessRegistrationForm
    model = Store
    # success_url = reverse_lazy('dashboard')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user"] = self.request.user
    #     return context

dashboard = DashboardView.as_view()


class DashboardProducts(LoginRequiredMixin, generic.ListView):
    template_name = "dashboard/products.html"
    # form_class = BusinessRegistrationForm
    model = Store
    # success_url = reverse_lazy('dashboard_stores')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uid = self.request.user.id
        context.update({
            'products': Product.objects.filter(created_by = uid)
        })
        return context
    

dash_products = DashboardProducts.as_view()


class HomeView(generic.ListView):
    template_name = "index.html"
    # form_class = BusinessRegistrationForm
    model = Store
    # success_url = reverse_lazy('dashboard_stores')

home = HomeView.as_view()


class StoresView(generic.ListView):
    template_name = "stores.html"
    # form_class = BusinessRegistrationForm
    model = Store
    # success_url = reverse_lazy('dashboard_stores')

stores = StoresView.as_view()
