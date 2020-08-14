import os
import instaloader


def pic_download(instagram_username_profile_pic):
    access_bot = instaloader.Instaloader()
    os.chdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
    if os.path.isdir("Instagram Downloads"):
        os.chdir("Instagram Downloads")
        return access_bot.downlaod_profile(instagram_username_profile_pic, profile_pic_only=True)
    else:
        os.mkdir("Instagram Downloads")
        os.chdir("Instagram Downloads")
        return access_bot.downlaod_profile(instagram_username_profile_pic, profile_pic_only=True)


if __name__ == "__main__":
    instagram_username_profile_pic = input(
        "Enter the username of the account whose profile pic ypu want to download")
    pic_download(instagram_username_profile_pic)
