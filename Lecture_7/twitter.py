import re

url = input("URL: ").strip()
    # replace the email with "" = empty space in this case
    #.removeprefix("https://twitter.com/") just remove
# username = url.replace("https://twitter.com/", "")

                     # ? for http. and ()? for the hole thing inside the parentheses
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
