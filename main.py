# -*- coding: utf-8 -*-
#! /usr/bin/python3,11                                                                                                                   import os
import requests
import datetime
import asyncio
import validators
from urllib.parse import urlparse
from sys import stdout
from colorama import Fore, Style, init
import logging                                                                                                                             
# Inisialisasi Colorama dan Logging                                                                                                        init(autoreset=True)
                                                                                                                                           # Pengaturan Logging yang benar
logging.basicConfig(
    filename='attack.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',  # Perbaiki dari levellevel menjadi levelname                                          datefmt='%Y-%m-%d %H:%M:%S'
)

# Fungsi untuk Logging Informasi Serangan
def log_attack_status(message, level='info', print_to_terminal=True):
    if level == 'info':
        logging.info(message)
        if print_to_terminal:
            print(f"{Fore.CYAN}|    [INFO] {message.ljust(63)}|")
    elif level == 'error':
        logging.error(message)
        if print_to_terminal:
            print(f"{Fore.RED}|    [ERROR] {message.ljust(63)}|")
    elif level == 'warning':
        logging.warning(message)
        if print_to_terminal:
            print(f"{Fore.YELLOW}|    [WARNING] {message.ljust(63)}|")


# Fungsi untuk Menampilkan Header BASE dengan Warna
def display_header():
    header_lines = [
    f"{Fore.GREEN}══════════════════════════════════════════════════════════════════════════",     
    f"{Fore.YELLOW}",
    f"{Fore.YELLOW} ██████▒▒   ██▒▒                 ██████▒▒ ██▒▒   ██▒▒",
    f"{Fore.YELLOW} ██▒▒   ██▒▒██▒▒                ██▒▒      ██▒▒  ██▒▒",
    f"{Fore.YELLOW} ██▒▒   ██▒▒██▒▒                ██▒▒      ██▒▒ ██▒▒",
    f"{Fore.YELLOW} ██▒▒   ██▒▒██▒▒        {Fore.RED}█▒▒     {Fore.YELLOW}██▒▒      ██▒▒██▒▒",
    f"{Fore.YELLOW} █████▒▒    ██▒▒       {Fore.RED}███▒▒    {Fore.YELLOW}██▒▒      ██▒██▒▒",
    f"{Fore.YELLOW} ██▒▒   ██▒▒██▒▒      {Fore.RED}██▒██▒▒   {Fore.YELLOW}██▒▒      ██▒▒██▒▒ ",
    f"{Fore.YELLOW} ██▒▒   ██▒▒██▒▒     {Fore.RED}██▒▒ ██▒▒  {Fore.YELLOW}██▒▒      ██▒▒ ██▒▒",
    f"{Fore.YELLOW} ██████▒▒   ██████▒▒{Fore.RED}██▒▒   ██▒▒  {Fore.YELLOW}██████▒▒ ██▒▒   ██▒▒",
    f"{Fore.RED}                   {Fore.RED}██▒▒     ██▒▒    {Fore.GREEN}███████▒▒  ████▒▒     ████▒██▒▒       ██▒▒",
    f"{Fore.RED}                  {Fore.RED}████████▒▒ ██▒▒   {Fore.GREEN}██▒▒   ██▒▒██▒██▒▒   ██▒██▒▒██▒▒     ██▒▒",
    f"{Fore.RED}                 {Fore.RED}██▒▒         ██▒▒  {Fore.GREEN}██▒▒   ██▒▒██▒▒██▒▒ ██▒▒██▒▒ ██▒▒   ██▒▒",
    f"{Fore.RED}                {Fore.RED}██▒▒           ██▒▒ {Fore.GREEN}██▒▒   ██▒▒██▒▒ ██▒██▒▒ ██▒▒  ██▒▒ ██▒▒",
    f"{Fore.GREEN}               {Fore.RED}██▒▒             ██▒▒{Fore.GREEN}██▒▒   ██▒▒██▒▒  ███▒▒  ██▒▒   ██▒██▒▒",
    f"{Fore.GREEN}                                    ██████▒▒   ██▒▒   ██▒▒  ██▒▒    ███▒▒",
    f"{Fore.GREEN}                                    ██▒▒ ██▒▒  ██▒▒         ██▒▒     ██▒▒",
    f"{Fore.GREEN}                                    ██▒▒   ██▒▒██▒▒         ██▒▒     ██▒▒",
    f"{Fore.GREEN}",
    f"{Fore.GREEN} ",    
    f"{Fore.RED}    █████▒▒  ███▒▒   ██▒▒   ██▒▒ █▒▒  █▒▒ ██▒▒ █▒▒ █▒▒███████▒▒ █▒▒   █▒▒",
    f"{Fore.RED}   █▒▒      █▒▒  █▒▒ █▒█▒▒ █▒█▒▒ █▒▒  █▒▒ █▒█▒▒█▒▒ █▒▒   █▒▒     █▒▒ █▒▒",
    f"{Fore.WHITE}   █▒▒      █▒▒  █▒▒ █▒▒█▒█▒▒█▒▒ █▒▒  █▒▒ █▒▒█▒█▒▒ █▒▒   █▒▒      ██▒▒",
    f"{Fore.WHITE}    ████▒▒   ███▒▒   █▒▒██▒▒ █▒▒  ███▒▒   █▒▒ ██▒▒ █▒▒   █▒▒       █▒▒",
    f"{Fore.WHITE}",      
    f"{Fore.YELLOW}════════════════════════════════════════════════════════════════════════════",     
    ]
# Tampilkan header dengan warna
    for line in header_lines:
        print(line)

    # Versi da n URL
    print(f"{Fore.WHITE}{Style.BRIGHT}{' ' * 57}v.1.0")
    print(f"{Fore.CYAN}{Style.BRIGHT}{' ' * 16}https://kunkaffa@gmail.com")
    print(f"{Fore.CYAN}|{'=' * 74}|")

# Fungsi untuk Meminta Input dari Pengguna dengan Tampilan Rapi
def get_user_input(prompt_message):
    print(f"{Fore.GREEN}|{' ' * 4}[?] {prompt_message.ljust(63)}|")
    print(f"{Fore.GREEN}|{'=' * 74}|")
    return input(f"{Fore.YELLOW}{' ' * 4}> ").strip()

# Fungsi Countdown untuk Menampilkan Waktu Serangan
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 1:
            stdout.flush()
            stdout.write(f"\r{Fore.BLUE}| [*]{Fore.RED} {remaining_time:.2f} {Fore.BLUE} Sec left{' ' * 26}|")
            print(f"\r{Fore.RED} ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ {Fore.CYAN}▒▒ ▒▒ ▒▒ ▒▒ ▒▒")
            print(f"\r{Fore.GREEN}▒BLACK▒ARMY▒{Fore.WHITE}▒INJECT▒ATTACK▒ ▒ ")
        else:
            stdout.flush()
            stdout.write(f"\r{Fore.RED}|▒[÷]▒ {Fore.YELLOW}BLACK-ARMY {Fore.CYAN} Attack has been completed|\n")
            print(f"{Fore.CYAN}|{'=' * 74}|")
            return

# Validasi URL dan Parsing Target
def get_target(url):
    if not validators.url(url):
        log_attack_status(f"URL tidak valid: {url}", level='error')
        raise ValueError(f"URL tidak valid: {url}")

    target = {
        'uri': urlparse(url).path or "/",
        'host': urlparse(url).netloc,
        'scheme': urlparse(url).scheme,
        'port': urlparse(url).netloc.split(":")[1] if ":" in urlparse(url).netloc else ("443" if urlparse(url).scheme == "https" else "80")
    }
    log_attack_status(f"Target acquired: {target['host']} ({target['scheme']}://{target['host']}:{target['port']}{target['uri']})")
    return target

# Fungsi Serangan Utama
def launch_attack(target_url, duration):
    target = get_target(target_url)

    # Inisialisasi Serangan dan Waktu Serangan
    log_attack_status(f"Lounch attack {target['host']} for {duration} second...")
    countdown(duration)

if __name__ == "__main__":
    # Tampilkan Header
    display_header()

    # Prompt untuk input dari pengguna dengan tampilan yang rapi
    target_url = get_user_input("URL TARGET:   ")
    while not validators.url(target_url):
        print(f"{Fore.RED}|    [ERROR] Invalid URL, try again.{' ' * 37}|")
        print(f"{Fore.CYAN}|{'=' * 74}|")
        target_url = get_user_input("URL TARGET:")

    try:
        attack_duration = int(get_user_input("Attack Duration (second):"))
    except ValueError:
        attack_duration = 60  # Default durasi

    # Luncurkan serangan
    launch_attack(target_url, attack_duration)
    
