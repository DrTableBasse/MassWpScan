import os
from tqdm import tqdm

API_KEY = input ("Enter your API KEY from wpscan website : ")
file = input("Enter the file you want read to wpscanmass : ")

with open(file) as f:
  data = f.read().split('\n')
  for cmd in tqdm(data):
    if cmd.strip() :
      os.system(f"wpscan --url '{cmd}'   --random-user-agent --ignore-main-redirect --stealthy --throttle 5 --output '{cmd}'.json --format json  -- api-token '{API_KEY}'")
    else :
      print("Finished, I created one file.json per website !")