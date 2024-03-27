import requests
from bs4 import BeautifulSoup
import os

# Function to fetch and parse the webpage
def fetch_image_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all <a> tags and extract 'href' attribute
        image_links = [a['href'] for a in soup.find_all('a') if a['href'].endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        return image_links
    else:
        print("Failed to fetch the webpage.")
        return []

# Function to check for links and download images
def download_images(links, base_url):
    for link in links:
        print(f"Found link: {link}")
    user_input = input("Do you want to download these images? (y/n): ")
    if user_input.lower() == 'y':
        for link in links:
            # Add the base URL to the image link
            full_url = base_url + link
            response = requests.get(full_url)
            if response.status_code == 200:
                # Extract the file name from the link
                file_name = link.split("/")[-1]
                # Save the image to the IMAGES folder
                with open(os.path.join('/home/mich/Dokumenty/Kursy/IMAGES', file_name), 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded image: {file_name}")
            else:
                print(f"Failed to download image from link: {link}")
    else:
        print("Download canceled.")

# The URL of the webpage you want to search for image links
webpage_url = "http://699340.youcanlearnit.net"

# Fetch the image links from the webpage
image_links= fetch_image_links(webpage_url)

# Download the images if the user confirms
download_images(image_links,base_url=webpage_url+"/")

