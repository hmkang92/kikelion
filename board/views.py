from django.shortcuts import render

def post_list(requests):
	return render(requests, 'board/post_list.html')
