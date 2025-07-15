import platform
import subprocess
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor
from openpyxl import Workbook
from datetime import datetime

def get_local_ip():
    """Récupère l'adresse IP locale de l'ordinateur."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def ping(ip):
    """Teste le ping d'une adresse IP. Retourne (ip, True) si actif, sinon (ip, False)."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        subprocess.check_output(['ping', param, '1', ip], stderr=subprocess.DEVNULL)
        return ip, True
    except subprocess.CalledProcessError:
        return ip, False


def get_hostname(ip):
    """Tente d’obtenir le nom de la machine via reverse DNS. Sinon retourne 'Inconnu'."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Inconnu"

def scan_network(ip_range):
    """Scanne un réseau donné et retourne une liste de tuples (hostname, ip)."""
    print(f"🔍 Scan du réseau {ip_range} en cours...\n")
    active_hosts = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(ping, str(ip)) for ip in ip_range.hosts()]
        for future in futures:
            ip, is_up = future.result()
            if is_up:
                hostname = get_hostname(ip)
                active_hosts.append((hostname, ip))
                print(f"✅ {hostname} ({ip}) est actif")

    print(f"\n🎯 Total des hôtes actifs : {len(active_hosts)}")
    return active_hosts

def export_to_excel(hosts_list, filename="active_hosts.xlsx"):
    """Exporte la liste (hostname, ip) dans un fichier Excel."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Hôtes Actifs"

    ws.append(["Nom de machine", "Adresse IP", "Date / Heure"])

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for hostname, ip in hosts_list:
        ws.append([hostname, ip, now])

    wb.save(filename)
    print(f"\n📁 Résultats exportés dans le fichier : {filename}")

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"📡 Adresse IP locale détectée : {local_ip}")

    network = ipaddress.ip_network(local_ip + '/24', strict=False)

    active_hosts = scan_network(network)

    export_to_excel(active_hosts)
