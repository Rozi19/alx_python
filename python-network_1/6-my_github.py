"""
takes your GitHub credentials (username and password) and 
uses the GitHub API to display your id
"""
import requests
import sys

def main():
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json().get('id'))
    except ValueError:
        print('Not a valid JSON')

if __name__ == "__main__":
    main()