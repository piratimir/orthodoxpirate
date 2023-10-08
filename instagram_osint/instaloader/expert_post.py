"""
This script is useful when one wants to
learn about the usage of tools, for example
cyber security tools, or others.
"""

import instaloader

USER = "your_user_here"
PROFILE = "profile_for_investigation_here"

l = instaloader.Instaloader()
l.load_session_from_file(USER)

profile = instaloader.Profile.from_username(l.context, PROFILE)


for post in profile.get_posts():
    print("##########################")
    print("Location: ", post.location)
    print(post.title, post.comments)
    print("Likes:%d" % post.likes)
    print("Media count:%d" % post.mediacount)
    print("Liked by viwer: %s" % post.viewer_has_liked)
    print("TypeName: %s" % post.typename)
    print("##########################")
    print("\n")

    # if post is a collection of photos, download it
    if post.typename == "GraphSidecar":
        l.download_post(post, PROFILE)

