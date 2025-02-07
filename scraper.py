import csv
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")

soup = BeautifulSoup(req.content, 'html.parser')

res=soup.title
print(res.prettify())
print(res.get_text())
print(soup.prettify())
print(soup.append_children)
print(soup.name)
print(soup.attrs)
print(soup.get_text())
x=soup.prettify()
with open("index.html", "w+") as f:
    f.write(x)


courses = []
for course in soup.find_all('a', class_='course-card-title'): 
    title = course.get_text(strip=True)
    link = course.get('href')
    if title and link:
        courses.append([title, link])

languages = []
for language in soup.find_all('a', class_='language-card-title'):  
    title = language.get_text(strip=True)
    link = language.get('href')
    if title and link:
        languages.append([title, link])

# Save data to a CSV file
with open("geeks_courses_languages_1.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    writer.writerows(courses)
    writer.writerows(languages)

print("CSV file 'geeks_courses_languages.csv' has been created successfully!")