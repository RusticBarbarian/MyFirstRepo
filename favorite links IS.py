import pyautogui as q
import webbrowser

videos = ["https://www.youtube.com/watch?v=3tUCuMSPQwE","https://www.youtube.com/watch?v=gneBUA39mnI"]

music = ["https://open.spotify.com/browse","https://www.youtube.com/watch?v=OGSrioil96c"]

answer = q.prompt(
    """
Which would you rather do?
a) Watch videos
b) Listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
