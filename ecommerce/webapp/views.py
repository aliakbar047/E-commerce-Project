from django.shortcuts import render
from django.views.generic import View

from .models import *
from .forms import SearchForm

# Create your views here.

class HomePage(View):
    def get(self, *args, **kwargs):
        companies = Company.objects.all()
        form = SearchForm()

        context = {
                'form': form,
                'companies': companies
        }

        return render(self.request, "webapp/home.html", context)

    def post(self, *args, **kwargs):
        form = SearchForm(self.request.POST or None)
        if form.is_valid():
            search = form.cleaned_data.get(
                    'search')

            companies = Company.objects.filter(company_category__category_name__contains = search)

        else:
            companies = Company.objects.all()

        context = {
                'form': form,
                'companies': companies
        }

        return render(self.request, "webapp/home.html", context)


def detailPage(request,pk):
    company = Company.objects.get(id = pk)
    products = Product.objects.filter(company=company)

    context = {
        'company':company,
        'products':products
    }

    return render(request, 'webapp/details.html', context)
        

            


