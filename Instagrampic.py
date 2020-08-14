import instaloader
access_bot = instaloader.Instaloader()
instagram_username_profile_pic = '_rituraj10_'
print(access_bot.download_profile(
    instagram_username_profile_pic, profile_pic_only=True))
