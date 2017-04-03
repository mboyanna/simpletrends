import sys
from simpletrends import SimpleTrends, params
from datetime import datetime, date, time
import params

def _call_example_2_days(self):
	all_usernames = set()
	all_posts = []

	print("Collecting handles...")
	if params.with_debug_logging:
		all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
	else:
		all_usernames = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")

	if params.with_debug_logging:
		print("[* Note: log times are in UTC which is PST+7hrs. Current UTC time is:",datetime.utcnow()," ]\nReviewing posts...")
		for post in all_posts:
			print (post.user.username, post.created_time, post.post_text, sep=" at ")
	print("List of handles who posted #urbandecay on Instagram in the last 2 (TWO) days is: ")
	print (all_usernames)
	
	print("\n")

def _call_example_90_days(self):
	all_usernames = set()
	all_posts = []
	
	print("Collecting handles...")
	if params.with_debug_logging:
		all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=90, hashtag="urbandecay")
	else:
		all_usernames = self.all_recent_posts_for_tag(self, days_old=90, hashtag="urbandecay")
	
	if params.with_debug_logging:	
		print("[* Note: log times are in UTC which is PST+7hrs. Current UTC time is:",datetime.utcnow()," ]\nReviewing posts...")
		for post in all_posts:
			print (post.user.username, post.created_time, post.post_text, sep=" at ")
	print("List of handles who posted #urbandecay on Instagram in the the last 90 days is: ")
	print (all_usernames)

	print("\n")


def main(args):
	st=SimpleTrends
	print("Example 1")
	_call_example_2_days(st)
	print("Example 2")
	_call_example_90_days(st)


if __name__ == '__main__':
	main(sys.argv)


