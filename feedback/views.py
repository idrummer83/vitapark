from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Hotel, Feedback
from .forms import FeedbackForm

def detail(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        # hotel = request.POST.get('hotel', None)
        if form.is_valid():
            Feedback.objects.create(
                nick=form.cleaned_data['nick'],
                feedback=form.cleaned_data['feedback'],
                # hotel=form.cleaned_data[''],
                # hotel=hotel,
            )
            messages.success(request, 'Feedback is added successfully')
            return redirect('/feedback/feedback/')
    return render(
        request,
        'feedback.html',
        {
            # 'hotel': Hotel.objects.all(),
            'form': form,
            # 'feedbacks': Feedback.objects.filter(hotel=hotel),
            'feedbacks': Feedback.objects.all(),
        }
    )
