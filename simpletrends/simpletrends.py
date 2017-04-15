import sys
from instagram.client import InstagramAPI
from instagram.helper import timestamp_to_datetime
from datetime import datetime, timedelta, date, time
import time
import params

class SimpleTrends(object): 

    def __init__(self, *args,**kwargs):
        super(SimpleTrends, self).__init__(**kwargs)

    def all_recent_posts_for_tag(self, **kwargs):

        timedelta_days = kwargs.pop("days_old")
        tag_name = kwargs.pop("hashtag")

        cutoff_date = datetime.utcnow() - timedelta(timedelta_days-1)
        
        if params.with_debug_logging:
            print("Time period: ", timedelta_days," days back")
            print("Hashtag:", tag_name)
            print("Cutoff date [UTC]:", cutoff_date)

        all_usernames = set()
        all_recent_posts = []
        recent_posts = []
        filtered_recent_posts = []

        recent_posts, next_ = params.instagram_api.tag_recent_media_crawl_tag(count=params.batch_size, tag_name=tag_name, pagination_format='next_min_tag_id', scope='public_content')
        all_recent_posts.extend (filter(lambda a_post, cutoff_dt=cutoff_date : (a_post.created_time > cutoff_dt), recent_posts))

        burst_iter = 1
        while next_:
            recent_posts,next_ = params.instagram_api.tag_recent_media_crawl_tag(count=params.batch_size, tag_name=tag_name, pagination_format='next_min_tag_id',min_tag_id=next_, scope='public_content')
            filtered_recent_posts = [a_post for a_post in recent_posts[1:] if a_post.created_time > cutoff_date]
            for post in filtered_recent_posts:
                all_usernames.add(post.user.username)

            if params.with_debug_logging:
                all_recent_posts.extend(filtered_recent_posts)

            if (len(recent_posts)>1 and recent_posts[len(recent_posts)-1].created_time <= cutoff_date):
                break

            burst_iter=burst_iter+1
            if burst_iter>params.burst_size:
                burst_iter=0
                time.sleep(params.sleep_time)

        if params.with_debug_logging:
            return all_usernames, all_recent_posts
        
        return all_usernames

    def _call_example_2_days(self):
        all_usernames = set()
        all_posts = []        
        if params.with_debug_logging:
            all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
        else:
            all_usernames = self.all_recent_posts_for_tag(self, days_old=2, hashtag="urbandecay")
        
        print("List of handles who posted #urbandecay on Instagram in the last 2 (TWO) days is: ")
        print (all_usernames)    
        if params.with_debug_logging:
            print("Detailed log of posts follows.\n [* Note: log times are in UTC which is PST+7hrs now is:",datetime.utcnow()," ]")
            for post in all_posts:
                print (post.user.username, post.created_time, post.post_text, sep=" at ")
        print("\n")

    def _call_example_90_days(self):
        all_usernames = set()
        all_posts = []        
        if params.with_debug_logging:
            all_usernames, all_posts = self.all_recent_posts_for_tag(self, days_old=90, hashtag="urbandecay")
        else:
            all_usernames = self.all_recent_posts_for_tag(self, days_old=90, hashtag="urbandecay")
        
        print("List of handles who posted #urbandecay on Instagram in the the last 90 days is: ")
        print (all_usernames)    
        if params.with_debug_logging:    
            print("Detailed log of posts follows.\n [* Note: log times are in UTC which is PST+7hrs now is:",datetime.utcnow()," ]")
            for post in all_posts:
                print (post.user.username, post.created_time, post.post_text, sep=" at ")
        print("\n")


# def main(args):
#     st=SimpleTrends
#     print("Example 1: 90 days back")
#     st._call_example_90_days(st)
#     print("Example 2: 2 days back")
#     st._call_example_2_days(st)


# if __name__ == '__main__':
#     main(sys.argv)







