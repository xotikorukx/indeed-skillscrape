# indeed-skillscrape

This is a limited-scope script I busted out in half an hour while watching netflix on another monitor to scrape all the possible skills listed on indeed for my resume.

- Built in: Python 3.10
- Dependencies: requests (`pip install requests`)
- Instructions: Open the networking tab of your favorite browser. Type a single letter into the "skills" field. Copy the request URL into the program as a comment. Copy `seqId`, `ctk`, `sessionId` from the request URL you copied into lines 34-36. Run it.
- Outputs: Occasional statuses. `indeed-suggestions.md` file (attached).
