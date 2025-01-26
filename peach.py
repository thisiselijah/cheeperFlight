import requests
from bs4 import BeautifulSoup
import os
import config


class Peach:
    def __init__(self):
        print('Starting extraction...')
    def get_search(self):
        try:
            session = requests.Session()
            # print('url: ', config.url1)
            # print('payload: ', payload1)
            response1 = requests.get(url=config.url1, headers=config.headers1, params=config.payload1, allow_redirects=False)
            response1.raise_for_status()
            print(response1.status_code)
            # print('Cookies after response1:', session.cookies)
            
            if 'Location' in response1.headers:
                # print(response1.headers['Location'])
                payload2 = config.payload2
                payload2['t'] = response1.url
                response2 = session.get(url=config.url2, params=payload2, headers=config.headers2, cookies=session.cookies, allow_redirects=False)
                response2.raise_for_status()
                print(response2.status_code)
                # print('Cookies after response2:', session.cookies)

                if 'Location' in response2.headers:
                    url3 = response2.headers['Location']
                    # print('url: ', url3)
                    # print('\n')
                    
                    response3 = session.get(url=response2.headers['Location'], headers=config.headers3, cookies=session.cookies, allow_redirects=False)
                    response3.raise_for_status()
                    print(response3.status_code)
                    # print('Cookies after response3:', session.cookies)
                    if 'Location' in response3.headers:
                        # print(response3.headers['Location'])
                        response4 = session.get(url=config.url1, headers=config.headers4, params=config.payload1, allow_redirects=False)
                        response4.raise_for_status()
                        print(response4.status_code)
                        # print('Cookies after response4:', session.cookies)
                        if 'Location' in response4.headers:
                            # print(response4.headers['Location'])
                            response5 = session.get(url=response4.headers['Location'], headers=config.headers5, cookies=session.cookies, allow_redirects=False)
                            print(response5.status_code)
                            with open('response.txt', 'w', encoding='utf-8') as file:
                                file.write(response5.text)
                            
                        else:
                            print("No redirect Location found.")
                            
                else:
                    print("No redirect Location found.")
            else:
                print("No redirect Location found.")
        except Exception as e:
            print(e)
    def parse_search(self):
        pass
        

    
    
