"""
Script to gather information such as username,
biography, profile pic url, verification, full
name on followers of the target profile.
"""

import instaloader




# user attrs
USER = "your_username_here"
PROFILE = "username_for_osint_here"

# creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# login to Instagram with session

bot.load_session_from_file(USER)
profile = instaloader.Profile.from_username(bot.context, PROFILE)
print(profile)

# followers = [follower.username for follower in profile.get_followers()]

followers = profile.get_followers()
# for f in followers:print("%s has %d followers and follows %d" % (f.username, f.followers, f.followees))
# for f in followers:print("biography of %s: %s" % (f.username, f.biography))

for f in followers:
    print("Full name: %s" % f.full_name)
    print("Is private:%s" % f.is_private)
    print("Is verified: %s" % f.is_verified)
    print("Followed by viewer:%s" % f.followed_by_viewer)
    print("Bio: %s" % f.biography)
    print("Profile pic url: %s" % f.profile_pic_url)
    print("============================================")

