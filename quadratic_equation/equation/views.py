from django.shortcuts import render, redirect

from equation.forms import CommentForm, ValuesForm
from equation.models import Comments
from services import solution_of_the_equation


def homepage(request):
    """ Returning the main page """
    comments = Comments.objects.all().order_by('-created_at')[:5]

    if request.method == "POST":
        form = ValuesForm(request.POST)
        if form.is_valid():
            values = form.cleaned_data
            answer = solution_of_the_equation(values)
            context = {
                'form': form,
                'answer': answer,
                'comments': comments
            }
            return render(request, 'equation/homepage.html', context)
    else:
        form = ValuesForm()
        context = {
            'form': form,
            'comments': comments
        }
        return render(request, 'equation/homepage.html', context)


def comment_page(request):
    """ Display comments """
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
        return redirect('homepage')
    else:
        form = CommentForm()
        context = {
            'form': form
        }
        return render(request, 'equation/new_comment.html', context)

