from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from blog.models import Post
from .form import CommentForm


@require_POST
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        cmt = form.save(commit=False)
        cmt.post = post
        cmt.save()
        return redirect(post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'comments/preview.html', context=context)

