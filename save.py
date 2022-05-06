import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w") ##open시 해당파일이 없으면 만들어준다.
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs :
        writer.writerow(list(job.values()))