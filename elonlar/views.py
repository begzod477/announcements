from django.shortcuts import render, get_object_or_404
from .models import Category, Announcement

# Create your views here.

from django.shortcuts import render
from .models import Category, Announcement

def home(request):
    categories = Category.objects.all()
    announcements = Announcement.objects.all()

    context = {
        'categories': categories,
        'announcements': announcements,
    }

    return render(request, 'home.html', context)

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    context = {
        'announcement': announcement,
    }
    return render(request, 'announcement_detail.html', context)


def select_by_category(request, category_id):

    categories = Category.objects.all()
    announcements = Announcement.objects.filter(category_id=category_id)

    context = {
        'categories': categories,
        'announcements': announcements,
    }
    return render(request, 'home.html', context)