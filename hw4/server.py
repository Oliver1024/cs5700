# Kejian Tong

import socket
import requests
from bs4 import BeautifulSoup

def get_title(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/99 Safari/537'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1').get_text()
    return title

HOST = "127.0.0.1" 
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT)) 
    s.listen() 
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}") 
        data = conn.recv(1024) 
        url = data.decode('utf-8').strip()
        title = get_title(url)
        conn.sendall(title.encode('utf-8'))

