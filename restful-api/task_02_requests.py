import requests
import csv

# Base URL of JSONPlaceholder posts
URL = "https://jsonplaceholder.typicode.com/posts"

# Function to fetch and print post titles
def fetch_and_print_posts():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()  # Parse JSON data
        print("Post Titles:")
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")

# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    response = requests.get(URL)
    
    if response.status_code == 200:
        posts = response.json()  # Parse JSON data
        
        # Structure data as list of dictionaries
        structured_posts = []
        for post in posts:
            structured_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        
        # Write to CSV
        csv_file = "posts.csv"
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)
        
        print(f"Posts saved to {csv_file} successfully.")
    else:
        print("Failed to fetch posts.")

# Example usage
if __name__ == "__main__":
    # Print post titles
    fetch_and_print_posts()
    
    # Save posts to CSV
    fetch_and_save_posts()
