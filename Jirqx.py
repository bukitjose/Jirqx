import requests
import sys

print("Jirqx, Open source python search module")
print("created by Jose")
def jirax():
    while True:
        query = input("Enter your search query: ")
        url = f"https://api.duckduckgo.com/?q={query}&format=json&pretty=1&no_html=1&max_answers=10"
        headers = {"User-Agent": "DuckDuckGo-Python-Wrapper/1.0"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            answers = data.get("AnswerBoxes", []) + data.get("RelatedTopics", [])
            if not answers:
                print("No answer found.")
            else:
                for result in answers:
                    if "FirstURL" in result:
                        print(result["Text"])
                        print(result["FirstURL"])
                        print()
                confirmation = input("Do you want to search again? (Y/N) ").lower()
                if confirmation != 'y':
                    sys.exit(0)
        else:
            print(f"Error: {response.status_code}")
            confirmation = input("Do you want to try again? (Y/N) ").lower()
            if confirmation != 'y':
                sys.exit(0)

if __name__ == "__main__":
    jirax()