import json
import os.path

import requests
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        file_path = "tutorial/spiders/download/laravel/"

        def createLicense(id, imageUrl):
            print("Create license")
            cookies = {
                'original_landing_page_url': 'https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd',
                '_ga': 'GA1.2.643892078.1646084923',
                '_gcl_au': '1.1.1157069484.1646084924',
                '_pin_unauth': 'dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA',
                '_gid': 'GA1.2.212558826.1649497515',
                'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}',
                'GO_EXP': 'acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0',
                'G_ENABLED_IDPS': 'google',
                'psi': '{%22previouslySignedIn%22:true}',
                'free_account_first_visit_dashboard': '1',
                'GO_EXP_STOREFRONT': 'acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0',
                'cebs': '1',
                '_ce.s': 'v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1',
                '_clck': '1hs85ru|1|f0i|0',
                '__cf_bm': 'CnReH6KUkBwEd9LVSSqJAtvH.cGqaeKqUTrgyeGz0_k-1649596140-0-AcskE3Mby0HJhiCI+E0L+MGrfSghWNpCgsz+UCb7mjyCGSwzlywj8Y+AQ0i2/zFNZ4LTEDonoCWcp8kbYRbjLGw=',
                '_uetsid': 'c3cb7180b7e911ecb517c58e771d6bb0',
                '_uetvid': 'c3cb9150b7e911eca8349bf83307445f',
                '_clsk': '1stsb41|1649597755232|6|0|d.clarity.ms/collect',
                '_elements_session_4': 'dkdYbjRiNGNpWHdISHlGMTVuR09JRVRIZmdlMWp3UzF2M1NyL1VyaWRqS05aeWEzdy9OOXdmbnBYSnZDVWJWWW80dDM3SUxNSFRiNjNTWnpHayt5VU1BSFQ3cjZuTWNaUUYrSFcwTVQzZi8vR21QanhSZGw3bG8rc0lRaWpXM2ptbm5kOWJhZy9jUkQycEFrL1YzRnBYVjI3bSs1TkNpVXpjckpZMzdJMVB5dXJwZTZBWlNPV212Z2NNb2tFQ0JLcVNXWkhRemVyWlYzQ1l5ZmhEejUySUJKeGZpK1FBUXprNHhVdi9PZTRBdz0tLUNEQ3V4bVlrZ0NzTWQ2MFBlQXl6WEE9PQ%3D%3D--d28255d2895921bcbfe9a7931e7808a9c5ff4d16',
                '_gat_elements': '1',
            }

            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                'captcha-type': 'checkbox',
                'captcha-value': '03AGdBq27wPxpsd6-uxbcEnok0mXrb-yiEfinSFRuWnupnKGeuntqL0qBp8G6SdgE6yJOPI8wY4kRgPEDCyNqMWnaQfKHu8aLKAqwpbmKFPom5Gtk82PqgV3tbysPEeEB6KFTZDE7mUNSh1VgTl-xBODMegqt6rG-GlI0j7ASD_yvBu9DUf3r8C5cPM5qpnL2XwbMhZSvKjiKYW-k7Jah0yOeXWKA8LlD3FoigzHCsxp3bpo6wvQi2rQq6PdLyttv8Um7ZxpLq8Q5eOF9VBGRcZpiISp_UYGlclwj7uXMbNSaKYOxy4S7BiA5DYQz0yXiFcPzmGhGtPhDNoWJ0Df4VV0DsHAxjr0Rfh87Dlbsx6tM6DnCx9VIhKcNv9aKE8YkAHpCulHhcDRVa23-o3S75t-SmXBBS_ytJvEXFIQavxbVQmD0a-fY82d4K0V72do7PWY52OOUQL_tUnqjrkb_RkALoZ_FMI833vBl5P2hdX9CnEdj7_u7y2sxJpYUMvqoKEatmFZzlnpBTDro0JKCEPtS8rq70O7dHo2Fgm0UI_4B0LTrUj1QFMGRkhEbP35RwlbBfM-PC3cbMh1m-KrN8C84eQ19Vo_loe_dJMEn7o6k4z3uVD9tz5E_LbB5rcQOjJ5TrJEvOo3qlbqU-FQT_vlFpJHMhFiSkYAlbmbjTs3dT_liEA5wRib1Q2WYngNxPwmem4PgjR27qwxgBuFfrDtwWDhjs5E7YCguKffRNAXtKjDLVQSOj58uS6-XDbYnkLfA5ssaxXRa3RjnECKENpN49arj5pa80_GW5I1wzU00mh3VdxJF-OUutm044KPWE7jLwI0G3o5jAGwo4Sl6g6Pp1v5CU1Jz1w-WFXZ2p7fNjL1NVcZv76un603YtUy52qQejQyvtQoE2CYAn2HYviqs2jm94G2RTveePm5U67oIkYjgNFsNMRpGy1-3vf11eOiIIPFgrhtbTDwrm9UlFxKuxkeLlppOr9YBfoU65g3zEyrSh47IzfCEhvt2fSYPwY_R-rkrShaGqW3-wmddrUb6UFpLEg7X6qs-bEFdc2-6n7p_YbtnbDVJ9DhUi5ofwqQmzKptAxJJEJf7ePVbcuQ3ye534GAevLeBKF-Hezx7tYA0vXEjZDxQKGlHmsL9vt4Ds_7rPA5NaUbM9PzXbqHUFGwk2bVSRiUCMhqqVRHjtqqcmE4TYEpkVBCbub5ukl-6yQb5kG8AhOZ2u5xHn1Q9EMl1I8YFMMkN4Ln4YbFQxNycIpG2uFzS6fy7TKvB4Kkof0r0uQ-pp61q9TCoqNSPQRjOibtYhHmlEsMSK0JhZrr9koAcrIV0',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _clck=1hs85ru|1|f0i|0; __cf_bm=CnReH6KUkBwEd9LVSSqJAtvH.cGqaeKqUTrgyeGz0_k-1649596140-0-AcskE3Mby0HJhiCI+E0L+MGrfSghWNpCgsz+UCb7mjyCGSwzlywj8Y+AQ0i2/zFNZ4LTEDonoCWcp8kbYRbjLGw=; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=1stsb41|1649597755232|6|0|d.clarity.ms/collect; _elements_session_4=dkdYbjRiNGNpWHdISHlGMTVuR09JRVRIZmdlMWp3UzF2M1NyL1VyaWRqS05aeWEzdy9OOXdmbnBYSnZDVWJWWW80dDM3SUxNSFRiNjNTWnpHayt5VU1BSFQ3cjZuTWNaUUYrSFcwTVQzZi8vR21QanhSZGw3bG8rc0lRaWpXM2ptbm5kOWJhZy9jUkQycEFrL1YzRnBYVjI3bSs1TkNpVXpjckpZMzdJMVB5dXJwZTZBWlNPV212Z2NNb2tFQ0JLcVNXWkhRemVyWlYzQ1l5ZmhEejUySUJKeGZpK1FBUXprNHhVdi9PZTRBdz0tLUNEQ3V4bVlrZ0NzTWQ2MFBlQXl6WEE9PQ%3D%3D--d28255d2895921bcbfe9a7931e7808a9c5ff4d16; _gat_elements=1',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/laravel',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
                'x-csrf-token': 'mZOliXPpFsO2n4dXAT751xL+lIwt3dyWYoC+a7dq1v2+1CVLwniqpXvxQawBxJodOgZZFbOg4HHgcYMVNQ0Wtg==',
            }

            json_data = {
                'itemId': 'JS9C73D',
                'searchCorrelationId': '89fee9a5-d45c-4037-91f1-e27b3a99a3d1',
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
                '_gid': 'GA1.2.212558826.1649497515',
                'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}',
                'GO_EXP': 'acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0',
                'G_ENABLED_IDPS': 'google',
                'psi': '{%22previouslySignedIn%22:true}',
                'free_account_first_visit_dashboard': '1',
                'GO_EXP_STOREFRONT': 'acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0',
                'cebs': '1',
                '_ce.s': 'v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1',
                '_clck': '1hs85ru|1|f0i|0',
                '__cf_bm': 'CnReH6KUkBwEd9LVSSqJAtvH.cGqaeKqUTrgyeGz0_k-1649596140-0-AcskE3Mby0HJhiCI+E0L+MGrfSghWNpCgsz+UCb7mjyCGSwzlywj8Y+AQ0i2/zFNZ4LTEDonoCWcp8kbYRbjLGw=',
                '_uetsid': 'c3cb7180b7e911ecb517c58e771d6bb0',
                '_uetvid': 'c3cb9150b7e911eca8349bf83307445f',
                '_clsk': '1stsb41|1649597755232|6|0|d.clarity.ms/collect',
                '_gat_elements': '1',
                '_elements_session_4': 'SmhSTjBxaWl3Yk02dU9MVURRd0Y4UXc1WERuUzhMbDZvd21WUzlMYTVja3p0clluNUJ1SzFTUkUvZFVpRWxxMzFUeHExbkc1SnFnUHc4aDBVUmZ2V3R4TW1SS1Y0NjZYeUxqbDBIUUVGM0pDaHcyeENjRWNWZXFMSmJzdVlDWTFrL3dLbHo2Ky8yMHRNUTNCS3R3eWoxazFObmZoQ0NVSzFjVTQ3dWdKK1pqWFlhekpMczJzb1NDbWZ2Q1FQSDhHVWZtZXpnaFoxeFFad0plclh2bUFRbHZlMlg1U2p2TWNXcmd1MVBZSVI3OD0tLS81djJqcGk3ZEZBbVE1dTFWbHJXenc9PQ%3D%3D--ca924aa79ff1162df6a1070863959450478c1dd2',
            }

            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _clck=1hs85ru|1|f0i|0; __cf_bm=CnReH6KUkBwEd9LVSSqJAtvH.cGqaeKqUTrgyeGz0_k-1649596140-0-AcskE3Mby0HJhiCI+E0L+MGrfSghWNpCgsz+UCb7mjyCGSwzlywj8Y+AQ0i2/zFNZ4LTEDonoCWcp8kbYRbjLGw=; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=1stsb41|1649597755232|6|0|d.clarity.ms/collect; _gat_elements=1; _elements_session_4=SmhSTjBxaWl3Yk02dU9MVURRd0Y4UXc1WERuUzhMbDZvd21WUzlMYTVja3p0clluNUJ1SzFTUkUvZFVpRWxxMzFUeHExbkc1SnFnUHc4aDBVUmZ2V3R4TW1SS1Y0NjZYeUxqbDBIUUVGM0pDaHcyeENjRWNWZXFMSmJzdVlDWTFrL3dLbHo2Ky8yMHRNUTNCS3R3eWoxazFObmZoQ0NVSzFjVTQ3dWdKK1pqWFlhekpMczJzb1NDbWZ2Q1FQSDhHVWZtZXpnaFoxeFFad0plclh2bUFRbHZlMlg1U2p2TWNXcmd1MVBZSVI3OD0tLS81djJqcGk3ZEZBbVE1dTFWbHJXenc9PQ%3D%3D--ca924aa79ff1162df6a1070863959450478c1dd2',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/laravel',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
                'x-csrf-token': 'mZOliXPpFsO2n4dXAT751xL+lIwt3dyWYoC+a7dq1v2+1CVLwniqpXvxQawBxJodOgZZFbOg4HHgcYMVNQ0Wtg==',
            }

            json_data = {
                'licenseType': 'trial',
                'searchCorrelationId': '89fee9a5-d45c-4037-91f1-e27b3a99a3d1',
            }

            response = requests.post('https://elements.envato.com/api/v1/items/' +
                                     id+'/download.json', headers=headers, cookies=cookies, json=json_data)

            # print(response.text)
            res = json.loads(response.text)
            downloadUrl = res['data']['attributes']['downloadUrl']
            # print("\t" + res['data']['attributes']['downloadUrl'])
            return downloadUrl

        f = open('data.json')
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
            if os.path.exists(file_path + "preview/" + fileName + ".jpg"):
                print("Image already exists")
            else:
                print("Download image")
                yield scrapy.Request(url=imageUrl, callback=self.parse, cb_kwargs={'fileName': fileName, 'ext': 'jpg', 'file_path': file_path})

            # Download file
            if os.path.exists(file_path + fileName + ".zip"):
                print("File already exists")
            else:
                downloadUrl = createLicense(id, imageUrl)
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
