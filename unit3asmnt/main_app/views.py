from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WidgetForm
from .models import Widget
from django.db.models import Sum
# Create your views here.

def home(request):
    my_widgets = Widget.objects.all()
    widget_form = WidgetForm()
    widget_total = Widget.objects.aggregate(Sum('quantity'))["quantity__sum"]
    return render(request, 'index.html', {
        "widget_form": widget_form,
        "widget_list": my_widgets,
        "widget_total": widget_total
    })

def create(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        add_widget = form.save(commit=False)
        add_widget.save()
    my_widgets = Widget.objects.all()
    widget_form = WidgetForm()
    widget_total = Widget.objects.aggregate(Sum('quantity'))["quantity__sum"]
    return redirect('/', {
        "widget_form": widget_form,
        "widget_list": my_widgets,
        "widget_total": widget_total
    })

def delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    my_widgets = Widget.objects.all()
    widget_form = WidgetForm()
    widget_total = Widget.objects.aggregate(Sum('quantity'))["quantity__sum"]
    return redirect('/', {
        "widget_form": widget_form,
        "widget_list": my_widgets,
        "widget_total": widget_total
    })