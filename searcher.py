import requests
from bs4 import BeautifulSoup

# Define the search query
query = "lol meaning"
# Replace spaces in the query with '+'
query = query.replace(' ', '+')

# Define the URL for the Google search
url = f'https://www.google.com/search?q={query}'

# Define the headers for the request
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

# Send a GET request to the URL
data = requests.get(url, headers=header)

# If the request is successful
if data.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(data.content, "html.parser")
    
    # Find the first search result
    g = soup.find('div',  {'class':'g'})
    
    # If a search result is found
    if g:
        # Find all the anchors in the search result
        anchors = g.find_all('a')
        
        # If an anchor is found
        if anchors:
            # Get the href attribute of the first anchor
            link = anchors[0]['href']
            
            # Get the text of the first h3 element (the title of the search result)
            title = g.find('h3').text
            
            # Try to get the text of the first div with data-sncf attribute '2' (the description of the search result)
            try:
                description = g.find('div', {'data-sncf':'2'}).text
            except Exception as e:
                description = "-"
            
            # Format the result
            result = str(link)

# Send a GET request to the URL of the first link
link_data = requests.get(link, headers=header)

# If the request is successful
if link_data.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    link_soup = BeautifulSoup(link_data.content, "html.parser")
    
    # Find the meta description tag
    meta = link_soup.find('meta', attrs={'name': 'description'})
    
    # If a meta description tag is found
    if meta:
        # Get the content attribute of the meta description tag
        meta_description = meta.get('content')
    else:
        meta_description = "No meta description found"

# Print the result and the meta description
print(result)
print(meta_description)
