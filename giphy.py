#!/usr/bin/env python3
import argparse
import requests
import json
from keys import API_KEY


# Hit the trending endpoint and get a gif.
def giphy_trending():
    url = "https://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC"
    resp = requests.get(url)
    if resp.status_code == 200:
        gifs = json.loads(resp.text)
        cnt = 0
        for image in gifs[u'data']:
            data = requests.get(image[u'images'][u'original_still'][u'url'])
            try:
                with open('./gifs/'+str(cnt)+'.gif', mode='w') as f:
                    f.write(data.text)

            except Exception as e:
                print('[-] {}'.format(e))
            cnt += 1
        #print(gifs)
    else:
        print('[-] {}: {}'.format(resp.status_code, resp.text))

# Decide which Giphy endpoint to hit
def main():
    giphy_trending()


if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument("")
    #args = parser.parse_args()
    #main(args)
    main()
