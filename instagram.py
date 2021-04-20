from instapy import InstaPy
from instapy import smart_run

my_username = 'test_done12345'
my_password = 'testDONE92'

session = InstaPy(username= my_username , password = my_password , headless_browser = False )

with smart_run(session):
    session.set_relationship_bounds(enabled = True , 
                                    delimit_by_numbers = True ,
                                    max_followers = 5000 ,
                                    min_followers = 300 ,
                                    min_following = 50 )

    # session.set_do_follow( True , percentage = 100)
    
    # session.like_by_locations( ['1113688908732608/london-united-kingdom-uk/'] , amount = 100 )

    session.follow_by_tags( ['website'] , amount = 10 )