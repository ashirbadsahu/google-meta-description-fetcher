import requests
from bs4 import BeautifulSoup


query = "lol meaning"

query = query.replace(" ", "+")

url = f"https://www.google.com/search?q={query}"


# Define the headers for the request
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}


data = requests.get(url, headers=header)

# If the request is successful
if data.status_code == 200:
    soup = BeautifulSoup(data.content, "html.parser")

    first_search_result = soup.find("div", {"class": "g"})

    if first_search_result is not None:
        anchors = first_search_result.find_all("a")

        if anchors is not None:
            link = anchors[0]["href"]

            title = first_search_result.find("h3").text

            # Try to get the text of the first div with data-sncf attribute '2' (the description of the search result)
            try:
                description = first_search_result.find("div", {"data-sncf": "2"}).text
            except Exception as e:
                description = "-"

            result = str(link)

link_data = requests.get(link, headers=header)

# If the request is successful
if link_data.status_code == 200:
    link_soup = BeautifulSoup(link_data.content, "html.parser")

    # Find the meta description tag
    meta = link_soup.find("meta", attrs={"name": "description"})

    if meta is not None:
        meta_description = meta.get("content")
    else:
        meta_description = "No meta description found"

print(result)
print(meta_description)
