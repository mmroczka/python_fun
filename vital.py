import requests
import mechanicalsoup
import bs4

# res = requests.get('https://imvital.com/')
# res.raise_for_status()
#
# parser = bs4.BeautifulSoup(res.text, "html.parser")
#
# elems = parser.select("#ctl00_PageContent_UserName")
#
# for e in elems:
#     print(e)
br = mechanicalsoup.Browser()
username = 'Tony_Stark1'
password = input("What's the password?")
url = "https://www.myfitnesspal.com/account/login"
print("Logging in")
login_page = br.get(url)
login_form = login_page.soup.find("form", {"class":"form login LoginForm"})
# print(login_form)
login_form.find("input", {"id":"username"})["value"] = username
login_form.find("input", {"id":"password"})["value"] = password

print("Login sent")
response = br.submit(login_form, login_page.url)
print("Login response received")
