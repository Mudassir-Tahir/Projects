import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
ua = UserAgent()



def save(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def fetch(url):
    headers = {'User-Agent': ua.random}
    r = requests.get(url, headers=headers, timeout=5)
    return r.text


def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for link in soup.find_all("a"):
        linkhref = link.get("href")
        if linkhref is not None:
            if "/dp/" in linkhref:
                links.add(link.get("href").split("ref=")[0])
    return links


def extractor(html):
    data = {}
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find("div", {"id": "title_feature_div"}).get_text()
    data["title"] = title

    price = soup.find("span", {"class": "a-price-whole"}).get_text()
    data["price"] = price.replace(".", "").replace(",", "")

    features = soup.find("div", {"id": "feature-bullets"})
    data["features"] = []

    for index, li in enumerate(features.find_all("li")):
        data[f"feature-{index + 1}"] = li.text

        reviewDiv = soup.find("div", {"id": "cm-cr-dp-review-list"})
        divs = reviewDiv.findChildren("div", recursive=False)

        data["reviews"] = []
        for index, div in enumerate(divs):
            data[f"reviews-{index + 1}"] = (div.getText())
    return data


if __name__ == "__main__":
    print("Starting to collect data...")
    query = "monitor"
    url = f"https://www.amazon.in/s?k={query}"

    # Fetch the content of the url
    text = fetch(url)

    # Save the text as html
    save("index.html", text)

    # Extract relevant product links from the html
    links = extract_links(text)
    finalData = []
    for link in links:
        try:
            print(links)
            content = fetch(f"https://amazon.in{link}")
            # save("product.html", content)
            a = extractor(content)
            finalData.append(a)
        except Exception as e:
            print(e)

df = pd.DataFrame(finalData)
df.to_excel("data.xlsx")