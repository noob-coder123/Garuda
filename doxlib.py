"""THIS IS THE HEART OF GARUDA"""


"""
 █████████ ███████ ██████ █      █      █ ███████
 █         █     █ █      █      █      █ █     █
 █  ██████ ███████ █      █      █ ██████ ███████
 █       █ █     █ █      █      █ █    █ █     █
 █████████ █     █ █      ████████ ██████ █     █
===================================================
-----TOOL FOR EDUCATIONAL PURPOSES------
Coded by: github.com/Cryptonian007
Name    : Anubhav Kalita
Copy code with credits ^_^
===================================================
"""
import shodan
import sys
import webbrowser as wb
from googlesearch import search
from colorama import Fore, Style, init
from time import sleep
import phonenumbers
import os
import requests
import pickle as p
import random
from phonenumbers import geocoder, carrier, timezone

# colorama esc codes to make stuff colorful
init()
b = Style.BRIGHT
g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
o = Fore.YELLOW
rs = Style.RESET_ALL
plus = g + '[' + w + '+' + g + ']'
minus = g + '[' + w + '-' + g + ']'
ques = g + '[' + w + '?' + g + ']'
warn = g + '[' + r + '!' + g + ']'
info = g + '[' + w + 'i' + g + ']'
asterix = g + '[' + cy + '*' + g + ']'
inp = g + '[' + w + '~' + g + ']'
# user agents
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7',
    'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
    'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
    'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 5.1; U; MRA 5.5 (build 02842); ru) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
    'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00'
]


def g_search(query):
    """
    Objective: Performs a Google search[Top 15 results]
    Input: search query
    Return: None
    """
    lol = []
    results = search(query, tld='co.in', num=15, stop=15, pause=9)
    for i in results:
        lol.append(i)
    if len(lol) == 0:
        print(f'{b}{minus}{r} No results found{g}')
    else:
        for a in lol:
            print(f'{b}{plus}{cy} Retrieved URL: {g}{a}')


def check_root():
    """
    Objective: Checks root access for Linux
    Input: None
    return: None
    """
    print(f'{b}{info} Checking root access..')
    sleep(1)
    os.system('chmod 777 lnx.sh')
    os.system('bash lnx.sh')
    sleep(1)
    with open('root.txt', 'r') as f:
        st = str(f.readline())
        if st == 'rooted':
            pass
        else:
            print(f'{b}{warn}{r} Error: Need root access to launch webbrowser')
            print(f'{b}{info} Run {w}sudo su {g}and retry')
            sys.exit()


def format1(num):
    """a format for phonenumbers"""
    for i in num:
        if i == '-':
            num.remove(i)
    num.reverse()
    newnum = []
    i = 0
    while i != 10:
        newnum.append(num[i])
        i += 1
    newnum.reverse()
    newnum = ''.join(newnum)
    return newnum


def format2(num):
    '''another format for phonenumbers'''
    num.reverse()
    num.insert(4, '-')
    num.insert(8, '-')
    num.reverse()
    return num

# -----------------------------------------------------------------------------------------------------

class NameDox:
    """
    Objective: Performs Name Doxing
    Uses googlesearch to retrieve web results
    Also uses webbrowser to search for results in
    predefined sites
    Suggestions are welcome
    """

    def __init__(self, fname, lname=None):
        self.fname = fname
        if not lname is None:
            self.lname = lname
        else:
            self.lname = ''

    def doxname(self):
        # performs google search using multiple queries
        # Input: self implicit var | Return: None
        if not self.lname == '':
            name = self.fname + ' ' + self.lname
            query = self.fname + '+' + self.lname
        else:
            name = self.fname
            query = self.fname
        # print(f'{b}{info} --- Fetching results from Google(9 queries) ---')
        queries = [str(name) + ' facebook.com', str(name) + ' instagram.com', str(name) + ' twitter.com',
                   str(name) + ' youtube.com', str(name) + ' pipl.com', str(name) + ' linkedin.com',
                   str(name) + ' tumblr.com',
                   str(name) + ' googleplus.com', str(name) + ' myspace.com']
        print(f'{b}{asterix}{cy} Choose an option to get information')
        print(f'''
        {g}[0] Facebook  [3] YouTube  [6] Tumblr      [9] Websites Lookup
        {g}[1] Instagram [4] Pipl     [7] Google Plus
        {g}[2] Twitter   [5] LinkedIn [8] MySpace
            ''')
        argv = int(input(f'{inp}{cy} Enter option: {r}'))
        if argv == 0:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[0]}{g}] ---')
            g_search(queries[0])
        elif argv == 1:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[1]}{g}] ---')
            g_search(queries[1])
        elif argv == 2:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[2]}{g}] ---')
            g_search(queries[2])
        elif argv == 3:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[3]}{g}] ---')
            g_search(queries[3])
        elif argv == 4:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[4]}{g}] ---')
            g_search(queries[4])
        elif argv == 5:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[5]}{g}] ---')
            g_search(queries[5])
        elif argv == 6:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[6]}{g}] ---')
            g_search(queries[6])
        elif argv == 7:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[7]}{g}] ---')
            g_search(queries[7])
        elif argv == 8:
            print(f'{b}{info}--- Fetching info from Google[Query: {w}{queries[0]}{g}] ---')
            g_search(queries[8])
        elif argv == 9:
            if not os.name == 'nt' and sys.platform != 'Darwin':
                check_root()
            print(f'{b}{info}--- Website lookup for available databases ---')
            sleep(1)
            print(f'{b}{plus} URL: https://pipl.com/search/?q={query}')
            sleep(1)
            print(f'{b}{plus} URL: https://www.facebook.com/search/top/?init=quick&q={query}')
            sleep(1)
            print(f'{b}{plus} URL: https://plus.google.com/s/{query}')
            sleep(1)
            print(f'{b}{plus} URL: https://flickr.com/search/people/?username={query}')
            sleep(1)
            print(f'{b}{plus} URL: https://www.linkedin.fr/pub/dir/{query}')
            sleep(1)
            print(f'{b}{plus} URL: https://www.youtube.com/results?search_query={query}')
        else:
            print(f'{warn}{r} Error: Invalid Option')

# -----------------------------------------------------------------------------------------------------

class PhoneDox:
    """
    Performs phonenumber doxing.
    Uses phonenumbers module to get info about
    city, timzone, countryname, etc.
    Also uses Google to fetch more web results.
    Uses webbrowser to launch predefined sites.
    """

    def __init__(self, phonenumber):
        self.phonenumber = phonenumber

    def simple_scan(self, working=True):
        # function to get the basic info about a number (phonenumbers module)
        phone = phonenumbers.parse(self.phonenumber)
        if not phonenumbers.is_valid_number(phone):
            return False
        if phonenumbers.is_possible_number(phone):
            print(f"{b}{plus} The number is valid and possible.")
        else:
            print(f"{b}{warn} The number is valid but not possible.")
        international = phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        countrycode = phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        ).split(" ")[0]
        country = geocoder.country_name_for_number(phone, 'en')
        location = geocoder.description_for_number(phone, 'en')
        carrierr = carrier.name_for_number(phone, 'en')
        # ------------------------------------------------------------------------
        if working:
            print(f'{b}{plus} International Format : {international}')
            print(f'{b}{plus} Country name         : {country} ({countrycode})')
            print(f'{b}{plus} City/Province        : {location}')
            print(f'{b}{plus} Carrier              : {carrierr}')
            for time in timezone.time_zones_for_number(phone):
                print(f'{b}{plus} Timezone             : {time}')
        # ------------------------------------------------------------------------

    def db_scan(self):
        # function to get results from google and launch websites for available databases
        print(f'{b}{info} ---- Fetching relevant data from Google ----')
        g_search(self.phonenumber)
        print(f'{b}{asterix}{cy} Website lookup for available databases{g}')
        pno = list(self.phonenumber)  # formatting number
        pno.reverse()
        pno.insert(4, '-')
        pno.insert(8, '-')
        pno.reverse()
        pno = ''.join(pno)
        print(f'{b}{plus} URL: https://www.truepeoplesearch.com/results?phoneno={pno}')
        sleep(1)
        pno = list(pno)
        for i in pno:  # so stupid such a dumb kid i am :(
            if i == '-':
                pno.remove(i)
        pno = ''.join(pno)
        pno = pno.split('+')[1]
        print(f'{b}{plus} URL: http://www.scamcallfighters.com/search-phone-{pno}')
        sleep(1)
        pno = list(pno)
        pno.reverse()
        pno.insert(4, '-')
        pno.insert(8, '-');
        pno.insert(12, '-')
        pno.reverse()
        pno = ''.join(pno)
        print(f'{b}{plus} URL: https://www.411.com/phone/{pno}')
        sleep(1)
        print(f'{b}{plus} URL: https://www.whitepages.com/phone/{pno}')
        sleep(1)
        pno = list(pno)
        number = format1(pno)
        print(f'{b}{plus} URL: https://www.okcaller.com/{number}')
        sleep(1)
        number = list(number)
        number1 = format2(number)
        number2 = ''.join(number1)
        print(f'{b}{plus} URL: https://www.reverse-lookup.co/{number2}')
        sleep(1)
        print(f'{b}{plus} URL: https://www.revealname.com/{number2}')
        sleep(1)
        prompt = str(input(f'{b}{asterix}{cy} Wanna launch Web Browser?[y/n]: {g}'))
        if prompt == 'y':
            if not os.name == 'nt' and sys.platform != 'Darwin':
                check_root()
            sleep(1)
            wb.open(f'https://www.truepeoplesearch.com/results?phoneno={pno}')
            sleep(1)
            wb.open(f'http://www.scamcallfighters.com/search-phone-{pno}')
            sleep(1)
            wb.open(f'https://www.411.com/phone/{pno}')
            sleep(1)
            wb.open(f'https://www.whitepages.com/phone/{pno}')
            sleep(1)
            wb.open(f'https://www.okcaller.com/{number}')
            sleep(1)
            wb.open(f'https://www.reverse-lookup.co/{number1}')
            sleep(1)
            wb.open(f'https://www.revealname.com/{number1}')
        else:
            print(f'{b}{warn} Aborted.')

# -----------------------------------------------------------------------------------------------------

class Ipdox:
    """
    Objective: Performs Ip doxing
    Extracts geolocation.io database results
    Also fetches google results
    webbrowser to launch predefined sites
    """

    def __init__(self, ip):
        self.ip = ip

    def start_Ip_doxing(self):
        #api = '3d3aa7b39b504b0992df337b4ac74801'
        try:
            with open('core\\geolocation.dat', 'rb') as f:
                api = p.load(f)
        except:
            print(f'{b}{warn}{r} No Geolocation.io API. Run setup.py to store one')
            exit()
        print(f'{b}{info} Fetching information for {w}{self.ip}{g}')
        url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api[0]}&ip={self.ip}&fields=geo'
        try:
            result = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
            data = result.json()  # data in json format
            # retrieving data
            # ------------------------------
            country = data['country_name']
            state = data['state_prov']
            city = data['city']
            dis = data['district']
            zip_code = data['zipcode']
            lat = data['latitude']
            longitude = data['longitude']
            # ------------------------------
            # prints it out in a noice format
            print(f'{b}{asterix}{cy} Results from geolocation.io{g}')
            print(f'{b}{plus} Country   : {cy}{country}')
            print(f'{b}{plus} State     : {cy}{state}')
            print(f'{b}{plus} City      : {cy}{city}')
            print(f'{b}{plus} District  : {cy}{dis}')
            print(f'{b}{plus} Zip Code  : {cy}{zip_code}')
            print(f'{b}{plus} Latitude  : {cy}{lat}')
            print(f'{b}{plus} Longitude : {cy}{longitude}')
        except:
            print(f'{warn}{r} Unable to connect to geolocation.io')
        print(f'{b}{asterix}{cy} Fetching relevant data from Google{g}')
        ip = str(self.ip)
        query = ip + ' locate'
        g_search(query)
        print(f'{b}{asterix}{cy} Website lookup for available databases{g}')
        sleep(1)
        print(f'{b}{plus} URL: https://whatismyipaddress.com/ip/{ip}')
        sleep(1)
        print(f'{b}{plus} URL: https://www.g-force.ca/en/hosting/ip-whois?ip={ip}')
        sleep(1)
        prompt = str(input(f'{b}{asterix}{cy} Wanna launch Web Browser?[y/n]: '))
        if prompt == 'y':
            if not os.name == 'nt' and sys.platform != 'Darwin':
                check_root()
            wb.open(f'https://whatismyipaddress.com/ip/{ip}')
            sleep(1)
            wb.open(f'https://www.g-force.ca/en/hosting/ip-whois?ip={ip}')
        else:
            print(f'{b}{warn} Aborted.')

# -----------------------------------------------------------------------------------------------------

class Maildox:

    def __init__(self, mail):
        self.mail = mail

    def start_mail_dox(self):
        # fetches data using Google search
        # gets data from web dbs using google dorks
        # performs socialscan and h8mail scans
        print(f'{b}{asterix}{cy} Choose an option to scan{g}')
        print(f'{b}{g}[0] Fetch results from Google')
        print(f'{b}{g}[1] Dork for Pastebin databases')
        print(f'{b}{g}[2] Dork for Throwbin databases')
        print(f'{b}{g}[3] Dork for PDF data')
        print(f'{b}{g}[4] Run SocialScan')
        print(f'{b}{g}[5] Run H8Mail Scan')
        a = int(input(f'{b}{inp}{cy} Enter Choice: {r}'))
        if a == 0:
            print(f'{b}{plus} ---- {cy}Fetching relevant data from Google{g} ----')
            g_search(str(self.mail))
        elif a == 1:
            print(f'{b}{asterix}{cy} Dorking for Pastebin.com databases{g}')
            dork1 = 'site:"pastebin.com"' + ' intext:"' + str(self.mail) + '"'
            g_search(dork1)
        elif a == 2:
            print(f'{b}{asterix}{cy} Dorking for Throwbin.io databases{g}')
            dork2 = 'site:"throwbin.io"' + ' intext:"' + str(self.mail) + '"'
            g_search(dork2)
        elif a == 3:
            print(f'{b}{asterix}{cy} Dorking for available data in PDF files{g}')
            site = self.mail.split('@')[1]
            dork3 = 'site:"' + str(site) + '" filetype:PDF intext:"' + str(self.mail) + '"'
            g_search(dork3)
        elif a == 4:
            print(f'{b}{asterix}{cy} Running SocialScan...{g}')
            os.system(f'socialscan {self.mail}')
        elif a == 5:
            print(f'{b}{asterix}{cy} Running H8Mail Scan...{g}')
            os.system(f'h8mail -t {self.mail}')
        else:
            print(f'{warn}{r} Error: Invalid Option{rs}')

# -----------------------------------------------------------------------------------------------------

class UserDox:
    '''
    Objective: Dox using an username
    Searches from websites for results
    '''

    def __init__(self, username):
        self.username = username

    def web_search(self):
        # http response codes
        # --------------------------------------------------------------------------------
        bads = [320, 400, 401, 404, 422, 500, 501, 502, 503, 504, 410, 403]  # error codes
        hits = [201, 200, 202, 203, 204, 205, 206, 207, 208, 226]  # success codes
        # --------------------------------------------------------------------------------
        print(f'{b}{asterix}{cy} Checking in websites...')
        with open('core\\sites.dat', 'rb') as f:  # load sites from core/sites.dat
            sites = p.load(f)
        f.close()
        good = []  # list of good sites
        check = []  # list of sites to be checked manually
        for site in sites:
            a_site = site + str(self.username)
            agent = random.choice(user_agents)  # random user agent for header
            try:
                result = requests.get(a_site, headers={'User-Agent': agent})  # request
                if result.status_code in hits:
                    print(f'{b}{plus} HIT :: {w}{a_site}')  # to mark as a good site
                    good.append(a_site)
                elif result.status_code in bads:
                    print(f'{b}{minus}{o} BAD :: {w}{a_site}')  # to mark as a bad site
                else:
                    print(f'{b}{ques}{cy} TO CHECK :: {w}{a_site}')  # to mark sites tht needa be checked
                    check.append(a_site)
                sleep(2)
            except KeyboardInterrupt:
                print(f'{b}{warn}{r} Error: Task Interrupted(Ctrl+C){g}')  # handler
                break
            except:
                print(f'{b}{warn}{r} ERROR : {w}{a_site}')
        file = str(self.username) + '.txt'
        with open(file, 'w') as f:
            f.write(f'Username: {self.username} | Hits: {len(good)} | To Check: {len(check)}\n')
            f.write(f'---------------HITS----------------\n')
            for s in good:
                f.write(f'{s}\n')
            f.write(f'---------------TO CHECK---------------\n')
            for i in check:
                f.write(f'{i}\n')
        print(f'{info} Results logged to {w}{file}{g}')

# -----------------------------------------------------------------------------------------------------

class Shodan_search:
    """Searches devices on the internet using shodan API"""
    def __init__(self, query):
        self.query = query

    def start(self):
        try:
            with open('core\\shodan.dat', 'rb') as f:
                api = p.load(f)
        except:
            print(f'{b}{warn}{r} No Shodan API. Run setup.py to store one')
            exit()
        rlist = []
        sapi = shodan.Shodan(str(api[0]))
        print(f'{b}{info} Getting Shodan Results...')
        try:
            results = sapi.search(self.query)
            for result in results['matches']:
                rlist.append([str(result['ip_str']), str(result['port'])])
            if not len(rlist) == 0:
                for a in rlist[:100]:
                    print(f'{b}{plus} Retrieved :: {cy}IP : {w}{a[0]} {g}| {cy}Port : {w}{a[1]}')
                    sleep(1)
            else:
                print(f'{b}{minus}{r} No results found')
        except:
            print(f'{b}{warn}{r} Can\'t reach Shodan. Check API key and try again')

# -------------------------------------------------------------------------------------------------------
        
