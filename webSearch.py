import subprocess
import webbrowser

search = input("Enter what you want to search for: ")

payload = search.replace(' ', '+')

search_engine = input("Enter Google or Bing: ")

if search_engine.lower() == "google":
    visit = "https://www.google.com/search?q=" + payload

if search_engine.lower() == "bing":
    visit = "http://www.bing.com/search?q=" + payload


webbrowser.open_new_tab(visit)
