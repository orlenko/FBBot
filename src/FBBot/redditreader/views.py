from django.shortcuts import render
from django.views import generic
import fetcher


class TopSubmissions(generic.ListView):
	template_name = 'redditreader/top.html'
	context_object_name = 'submissions'

	def get_query_set(self):
		return fetcher.top() 


def top(request, subreddit):
	if subreddit.startswith('r/'):
		subreddit = subreddit[2:]
	return render_to_response()