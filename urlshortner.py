import pyshortners
import pyperclip

def shorten_url(url):
    shortener = pyshortners.Shortner()
    
    shortend_url = shortener.tinyurl.short(url)
    
    return shortend_url

def main():
    url = input("Enter the long url : ")
    
    shortened_url = shorten_url(url)
    
    pyperclip.copy(shortened_url)
    print("Shortened URL:", shortened_url)
    print("Shortened URL has been copied to the clipboard.")
    
if  __name__ == "__main__":
    main()