import requests

suggestions = []

try:

    results = []

    maxl = 0

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    suggestions = []

    for letter1 in letters:
        print(f"Running queries on '{letter1}'")

        for letter2 in letters:
            query = f"{letter1}{letter2}"

            _params = {
                "country": "US",
                "language": "en",
                "count": 100,
                "formatted": 1,
                "query": query,
                "useEachWord": True,
                "showAlternateSuggestions": False,
                "page": "myindeed",
                "merged": True,
                "rich": False,

                "seqId": `fill me in! (int)`,
                "ctk": "`fill me in! (str)`",
                "sessionId": "`fill me in! (str)`",
            }
            
            response = requests.get(
                "https://autocomplete.indeed.com/api/v0/suggestions/taxonomy/skills", params=_params)

            #print(f"Response Code {response.status_code} for query '{query}'.")

            if response.status_code != 200:
                NotImplementedError(
                    f"Death to the codes! Error {response.status_code}!")

            jArray = response.json()

            for jDict in jArray:
                if jDict["suggestion"] not in suggestions:
                    suggestions.append(jDict["suggestion"])

except Exception as e:
    print("Error! ", e)
    print("\n")

finally:
    print("Writing results...")
    with open("indeed-suggestions.md", "w") as a:
        for suggest in suggestions:
            a.write(f"{suggest}\n")

    print("Done!")
