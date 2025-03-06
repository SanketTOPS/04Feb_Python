import instaloader

instaID = input("Enter an Instagram ID:")

insta = instaloader.Instaloader()
insta.download_profile(instaID)
print("Download successfully!")
