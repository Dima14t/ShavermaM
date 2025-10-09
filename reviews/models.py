from django.db import models

class Reviews(models.Model):
    RATING_CHOICES = (
        ('1', "Плохо"),
        ('2', "Не очень"),
        ('3', "Удовлетворительно"),
        ('4', "Хорошо"),
        ('5', "Отлично"),
    )
    review = models.TextField()
    reviewer = models.CharField(max_length=250)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)  # лучше CharField, а не TextField
    is_published = models.BooleanField(default=False)
    date_writing = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.reviewer} ({self.get_rating_display()})"


class ReviewResponse(models.Model):
    review = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='responses'  # позволяет делать review.responses.all()
    )
    author = models.CharField(max_length=250)
    response_text = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ответ от {self.author} на отзыв от {self.review.reviewer}"
