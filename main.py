from indeed import extract_indeed_pages, extract_indeed_jobs
from save import save_to_file

max_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(max_indeed_page)
print(len(indeed_jobs))
save_to_file(indeed_jobs)