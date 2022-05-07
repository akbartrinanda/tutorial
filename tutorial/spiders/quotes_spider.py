import json
import os.path

import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        file_path = "tutorial/spiders/download/wedding/"
        f = open('data/wedding-pg1.json')

        def createLicense(id):
            print("Create license")
            cookies = {
                'original_landing_page_url': 'https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd',
                '_ga': 'GA1.2.643892078.1646084923',
                '_gcl_au': '1.1.1157069484.1646084924',
                '_pin_unauth': 'dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA',
                'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}',
                'G_ENABLED_IDPS': 'google',
                'psi': '{%22previouslySignedIn%22:true}',
                'free_account_first_visit_dashboard': '1',
                'GO_EXP': 'acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0',
                '_rdt_uuid': '1649942090834.9414f348-dbbc-4af7-a182-140034c0bc7d',
                'GO_EXP_STOREFRONT': 'acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0',
                'cebs': '1',
                '_ce.s': 'v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~10',
                '_clck': '1hs85ru|1|f19|0',
                '__cf_bm': 'svwcF6hIZ4CRkbj0F5xb6Z5NS5Xk4Y.HYUVMdZiCzFY-1651893489-0-AYNHQkkwoeLdogYJEHnmrX21/NDfP8MDtyZMXVYfB88tAdskdqvqdOiwxWie0Pn4NrsTbiDXWb0eF4mBY0as5AA=',
                '_uetsid': '5f691320cc5e11eca155190cf8c03841',
                '_uetvid': 'c3cb9150b7e911eca8349bf83307445f',
                '_clsk': 'zbkege|1651893991628|6|0|j.clarity.ms/collect',
                '_gat_elements': '1',
                '_elements_session_4': 'REtYUEd3OXNRZWFldXMxR2kyc04xczEvRnR0QUJPakUrd2hiYjg3STNQVEp6ZEhHZTIwZUpVMnFiU3pJVDRqK3JYRWltYkNUbE1iLzhSbWpkZVN3cGJJN3RLUEtSMnpaWVRtYjlLOWhDYjBSR09ReFo4Lys3TzJLU3Z3OWcxYzZDZlNrRy8vcTlGWUxwdXJtQzlEMEJCZVRNWnR4SW1ObGhsa05jSm1aMFNNTmlTaFFsWkJmN0RnTDZEQkFXOEhrbGIxMk04OHNORkdmaEZaNEc3NUt2QzY5ZjZqQzhxZEdodDN6Ynd5MXd0WjF6T0Z2RVZQU0xKRzZuZGd5Mnp1b1VNM25FQXpOK2crRWhsTXo0T3JwVnJnR3kzaEdwSlFlUzYwWHRhYllaL05WYjA5QXR4M1hQM0s5eEdNMVo3dU9EZjc3eWdlWmpqbElBUnBvellFSFBtUWxveVIyenhweFpTS0hLTDN6NHVoSTlHVWRBekw5dXduYVFSdDRjbFVLTEltdkQvaDNYeW51ZFJhQTZjaHRqUT09LS1tQXpieS9BcnhPMWZhMWxVNVZWdFhBPT0%3D--639ad52947003d7783ebf3afd0b3a09e89c9869d',
            }

            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0; _rdt_uuid=1649942090834.9414f348-dbbc-4af7-a182-140034c0bc7d; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~10; _clck=1hs85ru|1|f19|0; __cf_bm=svwcF6hIZ4CRkbj0F5xb6Z5NS5Xk4Y.HYUVMdZiCzFY-1651893489-0-AYNHQkkwoeLdogYJEHnmrX21/NDfP8MDtyZMXVYfB88tAdskdqvqdOiwxWie0Pn4NrsTbiDXWb0eF4mBY0as5AA=; _uetsid=5f691320cc5e11eca155190cf8c03841; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=zbkege|1651893991628|6|0|j.clarity.ms/collect; _gat_elements=1; _elements_session_4=REtYUEd3OXNRZWFldXMxR2kyc04xczEvRnR0QUJPakUrd2hiYjg3STNQVEp6ZEhHZTIwZUpVMnFiU3pJVDRqK3JYRWltYkNUbE1iLzhSbWpkZVN3cGJJN3RLUEtSMnpaWVRtYjlLOWhDYjBSR09ReFo4Lys3TzJLU3Z3OWcxYzZDZlNrRy8vcTlGWUxwdXJtQzlEMEJCZVRNWnR4SW1ObGhsa05jSm1aMFNNTmlTaFFsWkJmN0RnTDZEQkFXOEhrbGIxMk04OHNORkdmaEZaNEc3NUt2QzY5ZjZqQzhxZEdodDN6Ynd5MXd0WjF6T0Z2RVZQU0xKRzZuZGd5Mnp1b1VNM25FQXpOK2crRWhsTXo0T3JwVnJnR3kzaEdwSlFlUzYwWHRhYllaL05WYjA5QXR4M1hQM0s5eEdNMVo3dU9EZjc3eWdlWmpqbElBUnBvellFSFBtUWxveVIyenhweFpTS0hLTDN6NHVoSTlHVWRBekw5dXduYVFSdDRjbFVLTEltdkQvaDNYeW51ZFJhQTZjaHRqUT09LS1tQXpieS9BcnhPMWZhMWxVNVZWdFhBPT0%3D--639ad52947003d7783ebf3afd0b3a09e89c9869d',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/wedding',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                'x-csrf-token': 'LNhkIg3mtbPwKi1lp6tROzZp2bgGwo5zHru5eqdDT3v8zMVZx608Ov3uPxW1qFz0KvQ-lDnYFBlc8L2wzQ10sA',
            }

            json_data = {
                'itemId': 'PNDVXH9',
                'searchCorrelationId': '421379a7-a084-4fbd-b685-9fa120a6da0c',
                'licenseType': 'trial',
            }


            response = requests.post('https://elements.envato.com/api/v1/items/'+id+'/license.json',
                                     headers=headers, cookies=cookies, json=json_data)

            # print(response.text)
            return createDownload(id)

        def createDownload(id):
            print("Start Download")

            cookies = {
                'original_landing_page_url': 'https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd',
                '_ga': 'GA1.2.643892078.1646084923',
                '_gcl_au': '1.1.1157069484.1646084924',
                '_pin_unauth': 'dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA',
                'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}',
                'G_ENABLED_IDPS': 'google',
                'psi': '{%22previouslySignedIn%22:true}',
                'free_account_first_visit_dashboard': '1',
                'GO_EXP': 'acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0',
                '_rdt_uuid': '1649942090834.9414f348-dbbc-4af7-a182-140034c0bc7d',
                'GO_EXP_STOREFRONT': 'acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0',
                'cebs': '1',
                '_ce.s': 'v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~10',
                '_clck': '1hs85ru|1|f19|0',
                '__cf_bm': 'svwcF6hIZ4CRkbj0F5xb6Z5NS5Xk4Y.HYUVMdZiCzFY-1651893489-0-AYNHQkkwoeLdogYJEHnmrX21/NDfP8MDtyZMXVYfB88tAdskdqvqdOiwxWie0Pn4NrsTbiDXWb0eF4mBY0as5AA=',
                '_uetsid': '5f691320cc5e11eca155190cf8c03841',
                '_uetvid': 'c3cb9150b7e911eca8349bf83307445f',
                '_clsk': 'zbkege|1651893991628|6|0|j.clarity.ms/collect',
                '_gat_elements': '1',
                '_elements_session_4': 'Zlkva2wrSmZjNlFIKzZ3ZjlJajNmWnlLak9CZFp0YWNDRThoWFBUTXN4eVp1RktjaTlMdUpqQkxPWTl3L3BndE5JdEg4OWhSZit3dUFoY1N2OWZzR0E3MjVjRm15NmZ5VzFMVWNaL1dIOGsxanh0N0VoZGlaZGtYZFFERGFidk9BVFk5K1BmaXFTN0sxcVpwbk9tOUw0NXJuVG1WdU5wOXdjNkFUS0N3UVAxSXR4V1lVWUw2WHZKMmVaMXg4dTlOMnp3bW00dXJxbkZWOE92ejMrN1lPWEhvT1ZuWXhTMld0a3l0R29VNmVOQWJYNldnY2YzQmtibUtDZjkyTkVxRlFSNjAzekZvWlBhQWJEMmVCUHFhMVdSSFE5MHRqdGNBNzJOVnBsTGthSkg2NVV4d0VqYnJVTnEzdFdwblNvMTJwZzJySmZrcG1ISDh1aWdsbWo1M1Y5aGtFZVN0LzJTNngvcTZSamszMDdNdU9BQ2VOdGEvQ1FwYXJ6RkJlU3Erc3RDamN0aU5paStlaGQzNnBCLzFIUT09LS1ZSGxBSDErWkNya1pKRDk3QVdhTyt3PT0%3D--9458634f9096e83ddf82c51e206a26ccc773a78e',
            }

            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0; _rdt_uuid=1649942090834.9414f348-dbbc-4af7-a182-140034c0bc7d; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&gZewu4I5QzaajQXxKH_iEg=2&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~10; _clck=1hs85ru|1|f19|0; __cf_bm=svwcF6hIZ4CRkbj0F5xb6Z5NS5Xk4Y.HYUVMdZiCzFY-1651893489-0-AYNHQkkwoeLdogYJEHnmrX21/NDfP8MDtyZMXVYfB88tAdskdqvqdOiwxWie0Pn4NrsTbiDXWb0eF4mBY0as5AA=; _uetsid=5f691320cc5e11eca155190cf8c03841; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=zbkege|1651893991628|6|0|j.clarity.ms/collect; _gat_elements=1; _elements_session_4=Zlkva2wrSmZjNlFIKzZ3ZjlJajNmWnlLak9CZFp0YWNDRThoWFBUTXN4eVp1RktjaTlMdUpqQkxPWTl3L3BndE5JdEg4OWhSZit3dUFoY1N2OWZzR0E3MjVjRm15NmZ5VzFMVWNaL1dIOGsxanh0N0VoZGlaZGtYZFFERGFidk9BVFk5K1BmaXFTN0sxcVpwbk9tOUw0NXJuVG1WdU5wOXdjNkFUS0N3UVAxSXR4V1lVWUw2WHZKMmVaMXg4dTlOMnp3bW00dXJxbkZWOE92ejMrN1lPWEhvT1ZuWXhTMld0a3l0R29VNmVOQWJYNldnY2YzQmtibUtDZjkyTkVxRlFSNjAzekZvWlBhQWJEMmVCUHFhMVdSSFE5MHRqdGNBNzJOVnBsTGthSkg2NVV4d0VqYnJVTnEzdFdwblNvMTJwZzJySmZrcG1ISDh1aWdsbWo1M1Y5aGtFZVN0LzJTNngvcTZSamszMDdNdU9BQ2VOdGEvQ1FwYXJ6RkJlU3Erc3RDamN0aU5paStlaGQzNnBCLzFIUT09LS1ZSGxBSDErWkNya1pKRDk3QVdhTyt3PT0%3D--9458634f9096e83ddf82c51e206a26ccc773a78e',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/wedding',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                'x-csrf-token': 'LNhkIg3mtbPwKi1lp6tROzZp2bgGwo5zHru5eqdDT3v8zMVZx608Ov3uPxW1qFz0KvQ-lDnYFBlc8L2wzQ10sA',
            }

            json_data = {
                'licenseType': 'trial',
                'searchCorrelationId': '421379a7-a084-4fbd-b685-9fa120a6da0c',
            }

            response = requests.post('https://elements.envato.com/api/v1/items/' +
                                     id+'/download.json', headers=headers, cookies=cookies, json=json_data)

            # print(response.text)
            res = json.loads(response.text)
            downloadUrl = res['data']['attributes']['downloadUrl']
            # print("\t" + res['data']['attributes']['downloadUrl'])
            return downloadUrl

        data = json.load(f)
        x = 0
        for i in data['data']['items']:
            x = x + 1
            id = i['id']
            imageUrl = i['coverImage']['w2740']
            fileName = i['title']
            print("\n")
            print(x, ": \t", id, "\n\t", imageUrl, "\n\t", fileName)

            # Download image
            if os.path.exists(file_path + "preview/" + id + ' | ' + fileName + ".jpg"):
                print("Image already exists")
            else:
                print("Download image")
                yield scrapy.Request(url=imageUrl, callback=self.parse, cb_kwargs={'id': id, 'fileName': fileName, 'ext': 'jpg', 'file_path': file_path})

            # Download file
            if os.path.exists(file_path + id + ' | ' + fileName + ".zip"):
                print("File already exists")
            else:
                downloadUrl = createLicense(id)
                print("Download file: ")
                yield scrapy.Request(url=downloadUrl, callback=self.parse, cb_kwargs={'id': id, 'fileName': fileName, 'ext': 'zip', 'file_path': file_path})
        f.close()

    def parse(self, response, id, fileName, ext, file_path):
        if ext == 'jpg':
            with open(file_path + "preview/" + id + ' | ' + fileName + "." + ext, 'wb') as f:
                f.write(response.body)
        else:
            with open(file_path + id + ' | ' + fileName + "." + ext, 'wb') as f:
                f.write(response.body)
        self.log(f'Saved file {fileName}')
