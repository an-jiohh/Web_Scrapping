import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages() :
    resul =  requests.get(URL)
    soup = BeautifulSoup(resul.text, "html.parser")
    pagination = soup.find("div",{"class":"pagination"})
    pages = pagination.find_all('a')
    spans = []

    for page in pages[0:-1] :
        spans.append(int(page.find("span").string))
    max_page = spans[-1]
    return max_page

def extract_job(html) :
    title = html.find("span", title=True).text
    company = html.find("span", {"class":"companyName"}).text
    location = html.find("div", {"class":"companyLocation"}).text
    job_id = html['data-jk']
    return {'title' : title, 'company' : company, 'location' : location, 'link' : f"https://www.indeed.com/viewjob?jk={job_id}"}

def extract_indeed_jobs(last_pages) :
    jobs = []
    for page in range(last_pages) :
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        #results = soup.find_all("div", {"class": "job_seen_beacon"})
        results = soup.find_all('a', {"class":"fs-unmask"}) #이후를 위해 더 넓은 범위의 태그 사용
        for result in results :
            job = extract_job(result)
            jobs.append(job)

    return jobs