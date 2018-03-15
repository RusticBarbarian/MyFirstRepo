import pyautogui as pg
import time
import webbrowser 


points = 0


# Question 1

answer = pg.prompt(
"""
Which would you rather do?

a) Play guitar in a band
b) Sing in a band
c) Play drums in a band
"""
    )


# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# Question 2 

answer = pg.prompt(
"""
Which of these songs have you most heard of?

a) Master of Puppets
b) Havana 
c) Take Five 
"""
    )


# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3





# Question 3

answer = pg.prompt(
"""
Which band/artist have you heard most of?

a) Avenged Sevenfold
b) Bruno Mars  
c) Louis Armstrong and His Hot Five 
"""
    )


# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 4
webbrowser.open("https://drive.google.com/file/d/1O7hUPHPkkc6OqgUc0dAG5JEC3GHNGF47/view?usp=sharing")
answer = pg.prompt(
"""
Which guitar do you like better?

a) 
b) 
c) 
"""
    )


# Give Points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3



# END OF SURVEY

pg.alert("You are a...")

# Metalhead
if points < 6: 
    pg.alert("Metalhead")
    webbrowser.open("https://www.artsfon.com/large/201512/78976.jpg")
    webbrowser.open("https://www.youtube.com/watch?v=QLoNbArsQP0")
# Pop Star
elif points >6 and points <9:
    pg.alert("Pop Star")
    webbrowser.open("https://s.yimg.com/ny/api/res/1.2/heq5nbsaurkdMbRqe3tlng--/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9NjA4O2g9MzQyO2lsPXBsYW5l/http://a.abcnews.com/images/US/JT-half-time-show-super-bowl-ap-hb-180204_16x9_608.jpg")
    webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
# Cool Cat
elif points >= 9:
    pg.alert("Cool Cat")
    webbrowser.open("http://inspirekent.co.uk/wp-content/uploads/2017/06/jazz1.jpg")
    webbrowser.open("https://www.youtube.com/watch?v=QAvmjazU1sA")




















