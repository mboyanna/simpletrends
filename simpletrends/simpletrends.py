import sys
from instagram.client import InstagramAPI
from instagram.helper import timestamp_to_datetime
from datetime import datetime, timedelta, date, time
import time

# TBD - read in from a config file for the system
access_token = "3463673370.9d470f7.5ef8019afecd446eaf7b74c410596676"
client_secret = "d9520b95d70249d49ac8c0539fdf030c"
batch_size = 2
burst_size = 3
sleep_time = 2
with_debug_logging = True
instagram_api = InstagramAPI(access_token=access_token, client_secret=client_secret)

class SimpleTrends(object): 

	def __init__(self, *args,**kwargs):
		super(SimpleTrends, self).__init__(**kwargs)


	def all_recent_posts_for_tag(self, **kwargs):

		timedelta_days = kwargs.pop("days_old")
		tag_name = kwargs.pop("hashtag")

		cutoff_date = datetime.utcnow() - timedelta(timedelta_days-1)
		
		if with_debug_logging:
			print("Cutoff date [UTC]:", cutoff_date)
			print("Hashtag:", tag_name)

		all_usernames = set()
		all_recent_posts = []
		recent_posts = []
		filtered_recent_posts = []

		recent_posts, next_ = instagram_api.tag_recent_media_crawl_tag(count=batch_size, tag_name=tag_name, pagination_format='next_min_tag_id', scope='public_content')
		all_recent_posts.extend (filter(lambda a_post, cutoff_dt=cutoff_date : (a_post.created_time > cutoff_dt), recent_posts))

		burst_iter = 0
		while next_:
			recent_posts,next_ = instagram_api.tag_recent_media_crawl_tag(count=batch_size, tag_name=tag_name, pagination_format='next_min_tag_id',max_tag_id=next_, scope='public_content')
			filtered_recent_posts = [a_post for a_post in recent_posts[1:] if a_post.created_time > cutoff_date]
			for post in filtered_recent_posts:
				all_usernames.add(post.user.username)

			if with_debug_logging:
				all_recent_posts.extend(filtered_recent_posts)

			#DBG
			print("with_debug_logging=", with_debug_logging)
			print("Iteration ", burst_iter+1)
			print("recent_posts: ")
			for m in recent_posts:
				print(m.user.username," at ",m.created_time)
			print("filtered_recent_posts: ")
			for m in filtered_recent_posts:
				print(m.user.username," at ",m.created_time)
			print("All recent posts: ")
			for m in all_recent_posts:
				print(m.user.username," at ",m.created_time)
			#end of DBG

			if (len(recent_posts)>1 and recent_posts[len(recent_posts)-1].created_time <= cutoff_date):
				break

			burst_iter=burst_iter+1
			if burst_iter>burst_size:
				burst_iter=0
				time.sleep(sleep_time)

		if with_debug_logging:
			return all_usernames, all_recent_posts
		
		return all_usernames

	def _call_example_2_days(self):
		all_usernames = set()
		all_posts = []		
		if with_debug_logging:
			all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
		else:
			all_usernames = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
		
		print("\n","\n","List of users who posted #urbandecay on Instagram in the last 2 (TWO) days: ", all_usernames, sep="")	
		if with_debug_logging:
			print("Detailed log of posts follows.\n [* Note: log times are in UTC which is PST+7hrs now is:",datetime.utcnow()," ]")
			for post in all_posts:
				print (post.user.username, post.created_time, post.post_text, sep=" at ")
		print("\n\n")

	def _call_example_30_days(self):
		all_usernames = set()
		all_posts = []		
		if with_debug_logging:
			all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=30, hashtag="urbandecay")
		else:
			all_usernames = self.all_recent_posts_for_tag(self, days_old=30, hashtag="urbandecay")
		
		print("\n","\n","List of users who posted #urbandecay on Instagram in the the last 30 days: ", all_usernames, sep="")	
		if with_debug_logging:
			print("Detailed log of posts follows.\n [* Note: log times are in UTC which is PST+7hrs now is:",datetime.utcnow()," ]")
			for post in all_posts:
				print (post.user.username, post.created_time, post.post_text, sep=" at ")
		print("\n\n")


def main(args):
	st=SimpleTrends
	st._call_example_30_days(st)
	st._call_example_2_days(st)


if __name__ == '__main__':
	main(sys.argv)







