from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils import timezone

from .models import Review
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm


# Create your views here.

def index(request):
    page = request.GET.get('page','1')
    review_list = Review.objects.order_by('-create_date')

    paginator = Paginator(review_list, 10)
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'review/review_list.html', context)

def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'review/review_detail.html', context)

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.create_date = timezone.now()
            review.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'review/review_form.html', context)
