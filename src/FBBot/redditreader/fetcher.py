import praw



def top(subreddit, limit=10):
	r = praw.Reddit(user_agent="Vlad's Reddit Fetcher")
	submissions = r.get_subreddit(subreddit).get_hot(limit=limit)
	return submissions
	
