from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    publish_Date=job.find('span', class_='sim-posted').text.strip()
    if 'few' in publish_Date:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()

        skills = job.find('span', class_='srp-skills').text.replace(' ','')

        print(publish_Date)
        print(f'company Name: {company_name}')
        print(f'Skills Required: {skills}')
#















# with open('D:/ReactApps/ES6/Product Landing Page/index.html','r') as html_file:
#     content =html_file.read()
#     soup =BeautifulSoup(content, 'lxml')
#     tag =soup.find_all('section', class_='section-footer')

#     for company in tag:
#         comp = company.div.find_all('div')
#         cp=comp[1:-1]

#         for info in cp:
#             companyName=info.h3.text
#             print(companyName)
     
    
      
      

  
  

    
    

