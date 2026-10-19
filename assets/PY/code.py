from bs4 import BeautifulSoup
import requests

target = "https://dailyinsect.wordpress.com/"

def get_ins():
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(target, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        content = soup.find("div", class_="entry-content")
        if not content:
            return None
        
        image_url = None
        figure_tag = content.find("figure", class_="wp-block-image")
        if figure_tag:
            img_tag = figure_tag.find("img")
            if img_tag:
                image_url = (
                    img_tag.get("data-orig-file")
                    or img_tag.get("data-lazy-src")
                    or img_tag.get("src")
                )

        paragraphs = content.find_all("p", recursive=False)

        insect_name = "Unknown Name"
        scientific_name = "Unknown Scientific Name"
        fun_fact = "Not found"

        for p in paragraphs:
            text = " ".join(p.get_text().split()).strip()
            
            if not text or text.startswith("©"):
                continue

            if "," in text and len(text) < 100:
                if p.find("strong"):
                    continue
                
                parts = text.split(",", 1)
                insect_name = parts[0].strip()
                scientific_name = parts[1].strip()
            
            elif "has-medium-font-size" in p.get("class", []):
                fun_fact = text

        return {
            "name": insect_name,
            "scientific_name": scientific_name,
            "fun_fact": fun_fact,
            "image_url": image_url
        }
    except Exception as e:
        print(f"Error scraping the website: {e}")
        return None

