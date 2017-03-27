from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.http import Http404
from .forms import PostForm

def post_list(request):
	qs = Post.objects.all()

	q = request.GET.get('q', '')
	if q:
		qs = qs.filter(title__icontains=q)

	return render(request, 'board/post_list.html', {
		'post_list': qs,
		'q' : q,
	})


def post_detail(request, id):

#	try:
#		post = Post.objects.get(id=id)
#	except Post.DoesNotExist:
#		raise Http404

	post = get_object_or_404(Post, id=id)

	return render(request, 'board/post_detail.html', {
		'post' : post,		
	})


def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():

			# solution1)
			#post = Post()
			#post.title = form.cleaned_data['title']
			#post.content = form.cleaned_data['content']
			#post.save()

			# solution2)
			#post = Post(title = form.cleaned_data['title'],
			#			content = form.cleaned_data['content'], )
			

			post = form.save()

			# solution3)
			#post = Post(**form.cleaned_data)
			#post.save()
			return redirect(post)
		else:
			form.errors

	else:
		form = PostForm()
	return render(request, 'board/post_form.html', {
		'form' : form,
	})

def post_edit(request, id):
	post = get_object_or_404(Post, id=id)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(post)
		else:
			form.errors

	else:
		form = PostForm(instance=post)
	return render(request, 'board/post_form.html', {
		'form' : form,
	})