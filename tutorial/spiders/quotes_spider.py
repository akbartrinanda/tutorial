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
                'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _clck=1hs85ru|1|f0h|0; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; __cf_bm=48_hY6ksHpTtltnXW9vVgWvUqlAct_I0PFtEeZK.Si4-1649516863-0-AR55qQe2CLmCa6wLpD2RbSiI44bfWLeaHq72FmqMy74NvbPyhA/BUqeh341RZtXIXWsoZgSmydxInv6XB2nYcp8=; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _gat_elements=1; _elements_session_4=VUt5czdiU0VaaFhsY255MjJoVk9NdHAza2I4UDdwTWxjZ1djeFJMRVovZ2U3anhLYlVMWEpBdEpIS2ZhMzRicFovaTB2TlRaZVZlcC9adEw0cXNQNVpiaDkzc1FhMVJRT0gxQjk1MEpHMGJGZmgzWTQrTjFzaXR1MW5LaG5pVHphWlFHejF3ZmVCdG5TWDN4aDRPNml2cnRvTktrZTVTRUdLQWJpVFZyMkV1ZXhqb1F1UWx3dTF5WFM0VkJEUlQwRFVHdlJZMjZXRm9jTjhKU2VwOEFNeVhtci8wblE5TGE3VEh6OFFBSVo1Yz0tLVREbVNUNTJDZUxUcFVFV1lmTlViTUE9PQ%3D%3D--3ca4be88e9488ea475e3ad8ba278b7fa9dcf4b6f; _elements_session_4=MFdTZ3BFVktWdU5hYzZ3dHFUeHhFZyt0ZzFvcUVYdGpQWWtXK1g5Ukg5TlJIUnh3a21NWlA0OXFsazFRZWhhWVlNQW9lcDNvVHdYQm9Kdjk5TUxDUGpkZExKbkF1YU44WFdqZEdBdmw5Z2dTR3JKUlNacWtzdWZTLzdiUnFsc0JVRXFBcHd6emZsZmh0cnQxQlRxejM0MXVvWU4rMFBIcW1HSS9QUURTdkhxRzM3aVd2SStiRU1aMGNscCtYajcweFdOcnRVREdVd3kzZFVMMzNXbmhGMFFTZnRjNUptM3Y2dEc3dUI3R0NUcz0tLUtBbERoODFSVWYyZ2lLUkhKSk5Qbmc9PQ%3D%3D--59d3076ea99a3a06fd4b485f4d58a94ee86e2868',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/angular',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
                'x-csrf-token': 'KhLKwMche4UbQEp7L0NlLh4o6KNeCd6vMqSkrNhym9KwL9fFbwLJFC8ZGovSw31HSvWqzSlT0vfWzybm7/lGfQ=='
            }

            response = requests.request(
                "POST", imageUrl, headers=headers, data=payload)

            # print(response.text)
            return createDownload(id)

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
                'content-type': 'application/json',
                'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _clck=1hs85ru|1|f0h|0; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; __cf_bm=48_hY6ksHpTtltnXW9vVgWvUqlAct_I0PFtEeZK.Si4-1649516863-0-AR55qQe2CLmCa6wLpD2RbSiI44bfWLeaHq72FmqMy74NvbPyhA/BUqeh341RZtXIXWsoZgSmydxInv6XB2nYcp8=; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _gat_elements=1; _elements_session_4=eUptNjk4aVVZRU0rMHVpN0FmdVRJRHlyVzViRTB0dTN3YmJKbkNHSVAzdHJkNW9iL2VPRFhaaEZyTHFSRHpVUmx1Q0JCajh3Z2plOTJvbnliS3ViMVExaUJKV3JjK1ZJZy8ydVpWUHNZODNtTGVPUnVMcjM1VFFxNTlDbkhDSlM4NFRiUXRjeE5PT3J1bklrQ25TSzJhMk9jT1A3QjMyZFl1aUhQWjRYRU9pSHFEYWtBMThrRnV6eG9wVGJXVWVLSGRBbVhJdUoyRkZpeldCYmo3Z2ZsWXRnRStnMUJYZTNsTXZjM0ZJMXJ0bz0tLTk0c3dGWTBQK2dhcTNMNWU1bTZGQVE9PQ%3D%3D--f074c527a3cdc56480e1ebc1f3cdb5db33b95d68; _elements_session_4=MFdTZ3BFVktWdU5hYzZ3dHFUeHhFZyt0ZzFvcUVYdGpQWWtXK1g5Ukg5TlJIUnh3a21NWlA0OXFsazFRZWhhWVlNQW9lcDNvVHdYQm9Kdjk5TUxDUGpkZExKbkF1YU44WFdqZEdBdmw5Z2dTR3JKUlNacWtzdWZTLzdiUnFsc0JVRXFBcHd6emZsZmh0cnQxQlRxejM0MXVvWU4rMFBIcW1HSS9QUURTdkhxRzM3aVd2SStiRU1aMGNscCtYajcweFdOcnRVREdVd3kzZFVMMzNXbmhGMFFTZnRjNUptM3Y2dEc3dUI3R0NUcz0tLUtBbERoODFSVWYyZ2lLUkhKSk5Qbmc9PQ%3D%3D--59d3076ea99a3a06fd4b485f4d58a94ee86e2868',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/angular',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
                'x-csrf-token': 'KhLKwMche4UbQEp7L0NlLh4o6KNeCd6vMqSkrNhym9KwL9fFbwLJFC8ZGovSw31HSvWqzSlT0vfWzybm7/lGfQ=='
            }

            response = requests.request(
                "POST", url, headers=headers, data=payload)

            # print(response.text)
            res = json.loads(response.text)
            downloadUrl = res['data']['attributes']['downloadUrl']
            # print(res['data']['attributes']['downloadUrl'])
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
