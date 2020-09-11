from tkinter import *
import tkinter as tk
import requests
root = tk.Tk()
root.title("Instagram User Details")
root.geometry('500x400')


def search():
    user_name = user_id_entry.get()
    url = f"https://www.instagram.com/{user_name}/?__a=1"
    data = requests.get(url).json()
    print(data)

    def pic():
        import webbrowser
        user_pic = data['graphql']['user']['profile_pic_url']
        webbrowser.open(user_pic)
    if user_details.get(1.0, END) != "":
        user_details.delete(1.0, END)
        user_details.insert(1.0, f"\tUsername : {data['graphql']['user']['username']}\n\tFollowers : {data['graphql']['user']['edge_followed_by']['count']}\n\tFollowing : {data['graphql']['user']['edge_follow']['count']} \n\tFull Name : {data['graphql']['user']['full_name']} \n\tTotal Post : {data['graphql']['user']['edge_owner_to_timeline_media']['count']}\n\tCategory : {data['graphql']['user']['category_enum']} \n\tEmail : {data['graphql']['user']['business_email']} \n\tBio-Link:{data['graphql']['user']['external_url']}\n\tPrivate Account:{data['graphql']['user']['is_private']}\n\tVerified Account:{data['graphql']['user']['is_verified']}\n\tBussiness Account:{data['graphql']['user']['is_business_account']}\n\tDirect Profile Picture")
        Button(frame3, text="Click to see", relief=RAISED, borderwidth=1, font=(
            'verdana', 8, 'bold'), bg='red', fg="white", command=pic).place(x=250, y=170)


frame1 = Frame(root, width=500, height=400,
              relief=RIDGE, borderwidth=5, bg='blue')
frame1.place(x=0, y=0)
frame2 = LabelFrame(frame1, width=480, height=380, relief=RIDGE, borderwidth=3,
                        bg='red', highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame2.place(x=5, y=5)
user_id_entry = Entry(frame1, width=30, relief=RIDGE, borderwidth=3)
user_id_entry.place(x=130, y=15)
search_id = Button(frame1, text="Search", relief=RAISED, borderwidth=2, font=(
    'verdana', 8, 'bold'), bg='red', fg="white", command=search)
search_id.place(x=330, y=15)
frame2 = LabelFrame(frame1, width=460, height=330, relief=RIDGE, borderwidth=3,
                        bg='blue', highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame2.place(x=15, y=45)
frame3 = LabelFrame(frame2, text="Users Details", width=440, height=310, highlightbackground="white",
                         highlightcolor="white", highlightthickness=5, font=('verdana', 10, 'bold'))
frame3.place(x=5, y=5)
user_details = Text(frame3, height=420, width=320, relief=RIDGE, borderwidth=5,
               highlightbackground="white", highlightcolor="white", font=('courier', 9, ''))
user_details.place(x=0, y=0)
root.mainloop()
