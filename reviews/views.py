from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reviews, ReviewResponse
from .forms import ReviewForm, ReviewResponseForm


def reviews(request):
    # Обработка основного отзыва
    if request.method == 'POST' and 'review_submit' in request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_published = True  # или False, если нужна модерация
            review.save()
            return redirect('reviews')

    # Обработка ответа на отзыв
    elif request.method == 'POST' and 'response_submit' in request.POST:
        response_form = ReviewResponseForm(request.POST)
        if response_form.is_valid():
            review_id = request.POST.get('review_id')
            review = get_object_or_404(Reviews, id=review_id, is_published=True)
            response = response_form.save(commit=False)
            response.review = review
            response.is_published = True  # или False
            response.save()
            return redirect('reviews')

    # Инициализация форм
    review_form = ReviewForm()
    response_form = ReviewResponseForm()

    # Загрузка отзывов с ответами
    reviews = Reviews.objects.filter(is_published=True).prefetch_related(
        'responses'
    ).order_by('-date_writing')

    return render(request, 'reviews/reviews.html', {
        'rev': reviews,
        'review_form': review_form,
        'response_form': response_form,
    })