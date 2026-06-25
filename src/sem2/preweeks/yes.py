import requests

BASE_URL = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses"

params = {
    "AppliedFilter": "FilterByCourses",
    "Source": "Breadcrumb",
    "ShowAll": "true",
    "PageIndex": 0,
    "MaxPageSize": 100,
    "PageSize": 100,
    "SortColumn": "",
    "SortDirection": "",
    "InitailSearchRequestedFromExternalPage": "false",
    "SearchText": "",
    "SelectedYear": 2026,
    "CollegeName": "All Colleges",
    "ModeOfDelivery": "All Modes",
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://programsandcourses.anu.edu.au/catalogue?FilterByCourses=true",
}

resp = requests.get(BASE_URL, params=params, headers=headers)
data = resp.json()["Items"]

fyc = [x for x in data if x["CourseCode"][4] == "1"]  # First year courses
print(fyc[1])
[
    print(
        f"{x["CourseCode"]}: {x["Name"]}, can be found at https://programsandcourses.anu.edu.au/course/{x["CourseCode"]}"
    )
    for x in fyc
]
