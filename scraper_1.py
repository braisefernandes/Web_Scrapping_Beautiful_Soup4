import requests
from bs4 import BeautifulSoup
import pandas as pd

link = input("Enter a link: ")
req = requests.get(link)
soup = BeautifulSoup(req.content, 'html.parser')

courses = []
for course in soup.find_all('a', class_='course-card-title'):  # Adjust class as per actual HTML
    title = course.get_text(strip=True)
    link = course.get('href')
    if title and link:
        courses.append([title, link])

languages = []
for language in soup.find_all('a', class_='language-card-title'):  # Adjust class as per actual HTML
    title = language.get_text(strip=True)
    link = language.get('href')
    if title and link:
        languages.append([title, link])

# Convert to DataFrame
df_courses = pd.DataFrame(courses, columns=["Title", "Link"])
df_languages = pd.DataFrame(languages, columns=["Title", "Link"])

# Save data to an Excel file
with pd.ExcelWriter("geeks_courses_languages.xlsx", engine="xlsxwriter") as writer:
    df_courses.to_excel(writer, sheet_name="Courses", index=False)
    df_languages.to_excel(writer, sheet_name="Languages", index=False)

print("Excel file 'geeks_courses_languages.xlsx' has been created successfully!")