import sys
from instagram.client import InstagramAPI
from instagram.helper import timestamp_to_datetime
from datetime import datetime, timedelta, date, time
import time


access_token=""
client_secret=""
batch_size = 0
burst_size = 0
sleep_time = 0
with_debug_logging = True
api = InstagramAPI()


class SimpleTrends(object): 

	#def __init__(self, *args, **kwargs):
	#	super(SimpleTrends, self).__init__(**kwargs)


	def __init__(self):
		# TBD - read in from a config file for the system
		self.access_token = "3463673370.9d470f7.5ef8019afecd446eaf7b74c410596676"
		self.client_secret = "d9520b95d70249d49ac8c0539fdf030c"
		self.batch_size = 2
		self.burst_size = 3
		self.sleep_time = 10
		self.with_debug_logging = True
		api = InstagramAPI(access_token=self.access_token, client_secret=self.client_secret)

	def all_recent_posts_for_tag(self, **kwargs):

		timedelta_days = kwargs.pop("days_old")
		tag_name = kwargs.pop("hashtag")

		cutoff_date = datetime.utcnow() - timedelta(timedelta_days)
		
		if with_debug_logging:
			print("Cutoff date [UTC]:", cutoff_date)
			print("Hashtag:", tag_name)

		all_recent_posts=[]
		all_usernames=set()

		recent_posts, next_ = api.tag_recent_media_crawl_tag(count=batch_size, tag_name=tag_name, pagination_format='next_min_tag_id')
		all_recent_posts.extend (filter(lambda a_post, cutoff_date=cutoff_date : (a_post.created_time > cutoff_date), recent_posts))

		burst_iter = 0
		while next_:
			recent_posts,next_ = api.tag_recent_media_crawl_tag(count=batch_size, tag_name=tag_name, pagination_format='next_min_tag_id',max_tag_id=next_)
			filtered_recent_posts = filter(lambda a_post, cutoff_date=cutoff_date : (a_post.created_time > cutoff_date), recent_posts[1:]) 
			for post in filtered_recent_posts:
				all_usernames.add(post.user.username)

			if with_debug_logging:
				all_recent_posts.extend(filtered_recent_posts)
			
			if burst_iter>burst_size:
				burst_iter=0
				sleep(sleep_time)
			else:
				burst_iter=burst_iter+1

		if with_debug_logging:
			print("All posts newer than cutoff date:")
			for a_post in all_recent_posts:
				print(a_post.user.username, a_post.created_time, sep=' at ')

		if with_debug_logging:
			return all_usernames, all_recent_posts
		
		return all_usernames


	def _call_example_2_days(self,**kwargs):
		all_usernames = set()
		all_posts = []		
		if with_debug_logging:
			all_usernames, all_posts = self.all_recent_posts_for_tag(days_old=2, hashtag='urbandecay')
		else:
			all_usernames = self.all_recent_posts_for_tag(days_old=2, hashtag='urbandecay')
		
		print("Users who posted #urbandecay on Instagram in the the last 2 days:","\n")
		print(all_usernames)
		if with_debug_logging:
			print("Detailed log of posts")
			for post in all_posts:
				print (post.user.username, post.created_time, sep=" at ")


	def _call_example_30_days(self):
		print("In", ...)
		all_usernames = set()
		all_posts = []		
		if with_debug_logging:
			all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=30, hashtag='urbandecay')
		else:
			all_usernames = self.all_recent_posts_for_tag(self, days_old=30, hashtag='urbandecay')
		
		print("Users who posted #urbandecay on Instagram in the the last 30 days:","\n")
		print(all_usernames)	
		if with_debug_logging:
			print("Detailed log of posts")
			for post in all_posts:
				print (post.user.username, post.created_time, sep=" at ")

# def main(args):
# 	st=SimpleTrends
# 	st._call_example_30_days()
# 	st._call_example_2_days()


# if __name__ == '__main__':
#     main(sys.argv)








