import json
import os.path

import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        file_path = "tutorial/spiders/download/angular/"

        def createLicense(id, imageUrl, searchCorrelationId):
            print("Create license")
            imageUrl = "https://elements.envato.com/api/v1/items/" + id + "/license.json"

            payload = json.dumps({
                "itemId": id,
                "searchCorrelationId": searchCorrelationId,
                "licenseType": "trial"
            })
            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                'content-type': 'application/json',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/angular',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
                'x-csrf-token': 'Briv4SmPSwoZRZFnlDaSXfOMN4MdTcbeZzLa1h4xO9S6WUM+sY4yisRtcOxLUT2SIsPsNjyLid+pkIZGNUXbvg==',
            }

            response = requests.request(
                "POST", imageUrl, headers=headers, data=payload)

            # print(response.text)
            return createDownload(id, searchCorrelationId)

        def createDownload(id, searchCorrelationId):
            print("Start Download")
            url = "https://elements.envato.com/api/v1/items/" + id + "/download.json"

            payload = json.dumps({
                "licenseType": "trial",
                "searchCorrelationId": searchCorrelationId
            })
            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                # Already added when you pass json=
                'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _clck=1hs85ru|1|f0i|0; _gat_elements=1; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=pnildd|1649587295131|10|0|d.clarity.ms/collect; outbrain_cid_fetch=true; _elements_session_4=VzlIa2l1Y05OV1VnTlJNazVGMXFHWlNsOUFLNjRjWlpCbTh2WGJqMWdUWXlCMzJMTGpZVHZYcUNJRzRWdGhNSVdKQXBGQzNUc01hRkRLc1NaTEFjWDViTkswK3hpYXlCZXhUZ2FhWW83M05uaU5wZGhYYVJ6SnkrbnNPVVJNaGhGMmhHakpsVTFUaDlFcDdoajNhVkNsRjViZ2U1RS9sL3MwcW82ODZYZFZSK05ydlBBTUVFVGMzV0Y4M0NjbXVXMS92K2VoWm5ZdTc0TkUwcFJhc1ErMmRWcHdPRUd1eWR1WFpSSVFTcVl0MD0tLXZDaHNlUVovZDBWdFlxNzB3NkF3VXc9PQ%3D%3D--1b5e2d62c0829f3fe274eccd89046d2982b07129',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/angular',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
                'x-csrf-token': 'Briv4SmPSwoZRZFnlDaSXfOMN4MdTcbeZzLa1h4xO9S6WUM+sY4yisRtcOxLUT2SIsPsNjyLid+pkIZGNUXbvg==',
            }

            response = requests.request(
                "POST", url, headers=headers, data=payload)

            # print(response.text)
            res = json.loads(response.text)
            downloadUrl = res['data']['attributes']['downloadUrl']
            print("\t" + res['data']['attributes']['downloadUrl'])
            return downloadUrl

        # search json by key
        def search_json(self, key, value, json_file):
            with open(json_file) as f:
                data = json.load(f)
                for p in data['items']:
                    if p[key] == value:
                        return p

        f = open('data.json')
        data = json.load(f)

        x = 0
        for i in data['data']['items']:
            x = x + 1
            id = i['id']
            imageUrl = i['coverImage']['w2740']
            fileName = i['title']
            indexSearchCorrelationId = search_json(
                self, 'id', id, 'search.json')
            searchCorrelationId = indexSearchCorrelationId['itemUuid']
            print("\n")
            print(x, ": \t", id, "\n\t", imageUrl, "\n\t", fileName)

            # Download image
            if os.path.exists(file_path + "preview/" + fileName + ".jpg"):
                print("Image already exists")
            else:
                print("Download image")
                yield scrapy.Request(url=imageUrl, callback=self.parse, cb_kwargs={'fileName': fileName, 'ext': 'jpg', 'file_path': file_path})

            # Download file
            if os.path.exists(file_path + fileName + ".zip"):
                print("File already exists")
            else:
                downloadUrl = createLicense(id, imageUrl, searchCorrelationId)
                print("Download file: ")
                yield scrapy.Request(url=downloadUrl, callback=self.parse, cb_kwargs={'fileName': fileName, 'ext': 'zip', 'file_path': file_path})
        f.close()

    def parse(self, response, fileName, ext, file_path):
        if ext == 'jpg':
            with open(file_path + "preview/" + fileName + "." + ext, 'wb') as f:
                f.write(response.body)
        else:
            with open(file_path + fileName + "." + ext, 'wb') as f:
                f.write(response.body)
        self.log(f'Saved file {fileName}')
