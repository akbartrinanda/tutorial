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
                '_clsk': '1stsb41|1649596168716|5|0|d.clarity.ms/collect',
                '_elements_session_4': 'NnVIQmEyZ2hlbXU5YlZTSjMwY01ZUzRMOWpNOFlBNS9LbzhlUUFZK0pGSDNoOUxWek12MzNwWUlyYVVIRENuSTVVUlBSbUZrZk1yMkNHVUNHMmhiYkROQ1orSTBKTzBGTnUwS3NvT0tZNEJZbElyR2xTai9XeURwdS8rY2hXWnJrVXZBeVUxS0ljMUtPTU9kZ0YrbTFCenJiZTlsdEE2RFJQVnVLUXg1dTY0K1hNVTZ1dWl4a3BFRmhQYlRHWWVOL1FDb2VjWm9rK2JaRVdETHFSU0ROcE5LYzh2TUl0dWVrM05XakRqNmNjbz0tLXl4b0RxWDZYM2NnOVMzbUNERXpoVVE9PQ%3D%3D--f6bc35a6b4daddf554c165877543dc73a1a84af1',
                '_gat_elements': '1',
            }

            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                'captcha-type': 'checkbox',
                'captcha-value': '03AGdBq24S4ObquRBpCvjiqfJB236FyIn4L-3Q3bUIhrbfio1PtNtxsqJH5b37YNTyr9pzHQP0To2o9Sj_bYOGXek0xlaMbTsHXquFHJroM_NN5tfU5vZ7L-5U_4MiLHgXx-MlcKge8PgMtjgTcfBeg3EBbCTPw4HeSwWhpaSPLQpmX-2ef949gvR9EfPRwWdOweglrEtwiwW7S1arDZm1aN90TY1_dqjweD9E8MoxU0xVo1SbRTkDpJsoaH4VHA1Qhk6SDaThnSYWithEfp8H7uWsi5V7duGzq2Wj0Cz1SCUBsNGhx72BvdxfFLduUykpl_FZTJKz7qOjJxdUi9KS3i-QbMgnN9Q9pC-MjvzDTF_X0z53gEe_PbBabbG3LXQ_Y5ka-MDBuuXAeHdqq5OKRIHE1AqRjlrKk0WW6a3pH9kRmX1UikXgcc41vxraG_tM6kUy99yOvsG35mBW77jGWI5GpGF0AKVbNTlh4wzl7bJA9PFMQFfA4-jVibP2cTDEUc2gjk5Rv06SP3yPhPsAsOAxFwxtAwI5Hv4CV7KRubeLBaKbng4AbxofnolCryvc70D-DvxNHVj7gZ3qLfWOtfSm9l2L-Ge3hU1XaB2sqAnwmDBSkBXlRyMRhi-_n2K2XY-XbkQNCnhcG7Ra1d2Ed2Z0Y_vzsI-xmOJs_rsYAsXbLz5MOGGl5OLExR3c1v4qKY4KDF-iFnwKJyq4sN-hI66W_Qy31S6oQAr1A64ixRKjgeRllzraChyfKDrN6DQaxsF8pYTLbDC3vLimCAw1317BhcxQnZu-EZmq3PaOy8Q8cFRNVQ_VTTWa5Dolk7lNZXUW8TVno33i_4T0Bsp_LIdGZ0xJtnME283R1XCj-VytKG9FC2C2G4c7kJDgaezdL1jZSHCrQeGRMRjqUZOsw0uBunwRnwfQc3bFU-F4xReUyxJ4tu1Dvjh6xOLlyFitGSo3NSCMTjdMMaczNfBHaUVyIKWFONde2oIRaambYji5NI4069bwMF1nWSXGZ78Ne68XYJyTqSDssLiSjLRZYlJq6leJMKdyBMzW8gcjQcEhP0x3_nODvn5-aIT_xUUh-VvzE5qjS5U1gS8uUmSHydKuveMemwZOnu57oyZemgcUlG_jtI-FGLi1_LPeoGUPVqsO3SLDsGJllMC2HM3bU2fO28sEw8fP8jtjGCVw9jJ9e_Lr9O7TELku7X-eX8vRYkXWDbGpZm0pt7yQzGJw0Oq_3B_JekJAnUxbpW7Ub0JisPvCjuH0dcY',
                # Already added when you pass json=
                'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _clck=1hs85ru|1|f0i|0; __cf_bm=CnReH6KUkBwEd9LVSSqJAtvH.cGqaeKqUTrgyeGz0_k-1649596140-0-AcskE3Mby0HJhiCI+E0L+MGrfSghWNpCgsz+UCb7mjyCGSwzlywj8Y+AQ0i2/zFNZ4LTEDonoCWcp8kbYRbjLGw=; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=1stsb41|1649596168716|5|0|d.clarity.ms/collect; _elements_session_4=NnVIQmEyZ2hlbXU5YlZTSjMwY01ZUzRMOWpNOFlBNS9LbzhlUUFZK0pGSDNoOUxWek12MzNwWUlyYVVIRENuSTVVUlBSbUZrZk1yMkNHVUNHMmhiYkROQ1orSTBKTzBGTnUwS3NvT0tZNEJZbElyR2xTai9XeURwdS8rY2hXWnJrVXZBeVUxS0ljMUtPTU9kZ0YrbTFCenJiZTlsdEE2RFJQVnVLUXg1dTY0K1hNVTZ1dWl4a3BFRmhQYlRHWWVOL1FDb2VjWm9rK2JaRVdETHFSU0ROcE5LYzh2TUl0dWVrM05XakRqNmNjbz0tLXl4b0RxWDZYM2NnOVMzbUNERXpoVVE9PQ%3D%3D--f6bc35a6b4daddf554c165877543dc73a1a84af1; _gat_elements=1',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/laravel',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'referer': 'https://www.google.com/',
                'x-csrf-token': 'mZOliXPpFsO2n4dXAT751xL+lIwt3dyWYoC+a7dq1v2+1CVLwniqpXvxQawBxJodOgZZFbOg4HHgcYMVNQ0Wtg==',
            }

            json_data = {
                'itemId': '9WTCSST',
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
                '_clsk': '1stsb41|1649596168716|5|0|d.clarity.ms/collect',
                '_gat_elements': '1',
                '_elements_session_4': 'cW0zTHlRcFJQL05LWDB2NzdBcmloc1hwUFBQK0gxS05QV2gyUHp6aVUzeHFmR3ZNYVJnNzh5bW9iMExMUlFGZTIyY2k1SVl6N1pEUGZzaGpsOXdZWXpVNzNCdmE2SXpXZVFLd3N5d0svREtJYVM4dlNxM0YzWWV6T01iZFFSRGVZaHcxcUtkQitpVFRObHNjNm1jOWNnaWFPR2lyWUYzL2hweW54MUk0aVptWnNBNlU5R3ovNkZ5QmVJTTQxOEJJVmJVVTBPRHZXWmp2cHFLbnpKVU1ldW1haUpkbGxoTlhxbG1udVBWV3Q5UT0tLWJnb0ttM3lJQVAyai8vVGFVK1JFdXc9PQ%3D%3D--b3839c63e7244511bf87737ba25905b301f8e291',
            }

            headers = {
                'authority': 'elements.envato.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
                # Already added when you pass json=
                'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                'cookie': 'original_landing_page_url=https://elements.envato.com/?irgwc=1&clickid=xym3ZsRrFxyITQGx1W2KXyvAUkGWVkzmf0zjSI0&iradid=298927&utm_campaign=elements_af_2530871&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&utm_medium=affiliate&utm_source=impact_radius&mp=Shisham%2520Digital%2520Media%2520Pvt%2520Ltd; _ga=GA1.2.643892078.1646084923; _gcl_au=1.1.1157069484.1646084924; _pin_unauth=dWlkPU1tSmxPV05sTkRRdFltSmhOeTAwTTJKakxUaGhNakV0T0RFMk4yVTJOVGt6TWpSaA; _gid=GA1.2.212558826.1649497515; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1649497515387%2Cregion:%27ID%27}; GO_EXP=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; G_ENABLED_IDPS=google; psi={%22previouslySignedIn%22:true}; free_account_first_visit_dashboard=1; GO_EXP_STOREFRONT=acDRkPbsSg6ejqGlTTHslg=0&FTr-7_qaRO-UzNOru4HW1Q=0&4C6lkqcfQZ2cNG-QhjT7yA=0; cebs=1; _ce.s=v~facc3dda67f714d0f4250c59bc06f5e06bab66d5~vpv~1; _clck=1hs85ru|1|f0i|0; __cf_bm=CnReH6KUkBwEd9LVSSqJAtvH.cGqaeKqUTrgyeGz0_k-1649596140-0-AcskE3Mby0HJhiCI+E0L+MGrfSghWNpCgsz+UCb7mjyCGSwzlywj8Y+AQ0i2/zFNZ4LTEDonoCWcp8kbYRbjLGw=; _uetsid=c3cb7180b7e911ecb517c58e771d6bb0; _uetvid=c3cb9150b7e911eca8349bf83307445f; _clsk=1stsb41|1649596168716|5|0|d.clarity.ms/collect; _gat_elements=1; _elements_session_4=cW0zTHlRcFJQL05LWDB2NzdBcmloc1hwUFBQK0gxS05QV2gyUHp6aVUzeHFmR3ZNYVJnNzh5bW9iMExMUlFGZTIyY2k1SVl6N1pEUGZzaGpsOXdZWXpVNzNCdmE2SXpXZVFLd3N5d0svREtJYVM4dlNxM0YzWWV6T01iZFFSRGVZaHcxcUtkQitpVFRObHNjNm1jOWNnaWFPR2lyWUYzL2hweW54MUk0aVptWnNBNlU5R3ovNkZ5QmVJTTQxOEJJVmJVVTBPRHZXWmp2cHFLbnpKVU1ldW1haUpkbGxoTlhxbG1udVBWV3Q5UT0tLWJnb0ttM3lJQVAyai8vVGFVK1JFdXc9PQ%3D%3D--b3839c63e7244511bf87737ba25905b301f8e291',
                'origin': 'https://elements.envato.com',
                'referer': 'https://elements.envato.com/web-templates/laravel',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'referer': 'https://www.google.com/',
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
