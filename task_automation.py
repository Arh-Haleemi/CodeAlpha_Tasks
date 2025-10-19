import os
import shutil
import re
import requests
from pathlib import Path

def task_automation_menu():
    """Main menu for task automation scripts."""
    
    print("=== TASK AUTOMATION SCRIPTS ===")
    print("Choose an automation task:")
    print("1. Move JPG files to new folder")
    print("2. Extract email addresses from text file")
    print("3. Scrape webpage title")
    print("4. Return to main menu")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                move_jpg_files()
            elif choice == '2':
                extract_emails()
            elif choice == '3':
                scrape_webpage_title()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter 1-4.")
                
        except KeyboardInterrupt:
            print("\nExiting automation menu...")
            break

def move_jpg_files():
    """Move all JPG files from source folder to destination folder."""
    
    print("\n=== JPG FILE MOVER ===")
    
    # Get source folder
    source_folder = input("Enter source folder path (or press Enter for current directory): ").strip()
    if not source_folder:
        source_folder = "."
    
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    
    # Get destination folder
    dest_folder = input("Enter destination folder name (will be created if doesn't exist): ").strip()
    if not dest_folder:
        dest_folder = "moved_jpg_files"
    
    # Create destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)
    
    # Find all JPG files
    jpg_extensions = ['.jpg', '.jpeg', '.JPG', '.JPEG']
    moved_count = 0
    
    try:
        for filename in os.listdir(source_folder):
            if any(filename.endswith(ext) for ext in jpg_extensions):
                source_path = os.path.join(source_folder, filename)
                dest_path = os.path.join(dest_folder, filename)
                
                # Handle duplicate filenames
                counter = 1
                original_dest_path = dest_path
                while os.path.exists(dest_path):
                    name, ext = os.path.splitext(filename)
                    dest_path = os.path.join(dest_folder, f"{name}_{counter}{ext}")
                    counter += 1
                
                shutil.move(source_path, dest_path)
                print(f"Moved: {filename} -> {dest_path}")
                moved_count += 1
        
        print(f"\nTask completed! Moved {moved_count} JPG files to '{dest_folder}' folder.")
        
    except Exception as e:
        print(f"Error moving files: {e}")

def extract_emails():
    """Extract email addresses from a text file and save to another file."""
    
    print("\n=== EMAIL EXTRACTOR ===")
    
    # Get input file
    input_file = input("Enter path to text file to scan for emails: ").strip()
    
    if not os.path.exists(input_file):
        print(f"File '{input_file}' does not exist.")
        return
    
    # Get output file
    output_file = input("Enter output file name (default: extracted_emails.txt): ").strip()
    if not output_file:
        output_file = "extracted_emails.txt"
    
    # Email regex pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    
    try:
        # Read input file
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Extract emails
        emails = re.findall(email_pattern, text)
        unique_emails = list(set(emails))  # Remove duplicates
        
        if unique_emails:
            # Save to output file
            with open(output_file, 'w', encoding='utf-8') as f:
                for email in sorted(unique_emails):
                    f.write(email + '\n')
            
            print(f"\nFound {len(unique_emails)} unique email addresses:")
            for email in sorted(unique_emails):
                print(f"  {email}")
            print(f"\nEmails saved to '{output_file}'")
        else:
            print("No email addresses found in the file.")
            
    except Exception as e:
        print(f"Error processing file: {e}")

def scrape_webpage_title():
    """Scrape the title of a webpage and save it to a file."""
    
    print("\n=== WEBPAGE TITLE SCRAPER ===")
    
    # Get URL
    url = input("Enter webpage URL (include http:// or https://): ").strip()
    
    if not url:
        print("URL cannot be empty.")
        return
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Get output file
    output_file = input("Enter output file name (default: webpage_titles.txt): ").strip()
    if not output_file:
        output_file = "webpage_titles.txt"
    
    try:
        print(f"Fetching webpage: {url}")
        
        # Make request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Extract title using regex
        title_match = re.search(r'<title[^>]*>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)
        
        if title_match:
            title = title_match.group(1).strip()
            # Clean up title (remove extra whitespace and HTML entities)
            title = re.sub(r'\s+', ' ', title)
            title = title.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
            
            print(f"Page title: {title}")
            
            # Save to file
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write(f"Title: {title}\n")
                f.write(f"Scraped on: {__import__('datetime').datetime.now()}\n")
                f.write("-" * 50 + "\n\n")
            
            print(f"Title saved to '{output_file}'")
        else:
            print("Could not find title tag on the webpage.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"Error processing webpage: {e}")

if __name__ == "__main__":
    task_automation_menu()