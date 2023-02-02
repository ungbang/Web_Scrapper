from extractors.wwr import extract_jobs_wwr
from extractors.indeed import extract_jobs_indeed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

keyword = "next js"

indeed = extract_jobs_indeed(keyword)
wwr = extract_jobs_wwr(keyword)
jobs = indeed + wwr

file = open(f"{keyword}_job_scrap.csv", "w")

file.write('Position,Company,Location,URL\n')

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()