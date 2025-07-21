import random
from datetime import datetime, timedelta

# Liste des user_ids disponibles (d'après ta liste)
user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 47]

# Types de machines pour varier les noms
machine_types = ['PC', 'LAPTOP', 'DESKTOP', 'WORKSTATION', 'NOTEBOOK']

def random_ip():
    # Génère une IP privée aléatoire (classe A, B ou C)
    classe = random.choice(['10', '172', '192'])
    if classe == '10':
        return f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    elif classe == '172':
        # Plage 172.16.0.0 - 172.31.255.255
        return f"172.{random.randint(16,31)}.{random.randint(0,255)}.{random.randint(1,254)}"
    else:
        # Classe C
        return f"192.168.{random.randint(0,255)}.{random.randint(1,254)}"

def random_login_time():
    # Date aléatoire dans les 7 derniers jours
    now = datetime.now()
    delta_days = random.randint(0, 6)
    delta_seconds = random.randint(0, 86399)
    return now - timedelta(days=delta_days, seconds=delta_seconds)

def generate_sql(filename="fake_user_logs.sql"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("INSERT INTO user_logs (user_id, machine_name, ip, login_time, logout_time) VALUES\n")
        lines = []
        for _ in range(500):
            user_id = random.choice(user_ids)
            machine_name = f"{user_id}-{random.choice(machine_types)}"
            ip = random_ip()
            login = random_login_time()
            logout = login + timedelta(hours=1)
            login_str = login.strftime("%Y-%m-%d %H:%M:%S")
            logout_str = logout.strftime("%Y-%m-%d %H:%M:%S")
            lines.append(f"({user_id}, '{machine_name}', '{ip}', '{login_str}', '{logout_str}')")
        f.write(",\n".join(lines) + ";\n")
    print(f"Fichier '{filename}' généré avec 100 entrées.")

if __name__ == "__main__":
    generate_sql()
