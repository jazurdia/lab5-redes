from tabulate import tabulate

def calculo(mascara, clase):
    print()
    print(f"Calculando subredes para la mascara {mascara} y clase {clase}")
    mascara, numbits  = mascara.split("/")
    
    tipos_clases = {
        "A": 8,
        "B": 16,
        "C": 24
    }

    clase = clase.upper()
    numbits = int(numbits)

    if clase in tipos_clases:
        numclase = tipos_clases[clase]

    # cantidad de subredes:
    subredes = 2**(numbits - numclase)
    print(f"La cantidad de subredes producida por la mascara elegida es {subredes}")

    # cantidad de ip validas por subred. 

    bits_hosts = 32 - numbits
    total_ips = 2**bits_hosts
    ips_validas = total_ips - 2
    print(f"La cantidad de ips validas por subred es {ips_validas}")

    # Calcular las subredes válidas y direcciones de broadcast
    subredes_validas = []
    for i in range(subredes):
        # Calcular el valor inicial de la subred
        base_subred = (int(mascara.split('.')[3]) // (2 ** bits_hosts)) * (2 ** bits_hosts)
        nueva_subred = f"{mascara.split('.')[0]}.{mascara.split('.')[1]}.{mascara.split('.')[2]}.{base_subred + i * (2 ** bits_hosts)}/{numbits}"

        # Calcular la dirección de broadcast
        broadcast = f"{mascara.split('.')[0]}.{mascara.split('.')[1]}.{mascara.split('.')[2]}.{base_subred + (i + 1) * (2 ** bits_hosts) - 1}"

        # Calcular las IPs válidas por subred
        primera_ip = base_subred + i * (2 ** bits_hosts) + 1
        ultima_ip = base_subred + (i + 1) * (2 ** bits_hosts) - 2

        # Guardar la subred, broadcast y el rango de IPs válidas
        subredes_validas.append((nueva_subred, broadcast, primera_ip, ultima_ip))

    # Imprimir resultados
    #for subred, broadcast, primera_ip, ultima_ip in subredes_validas:
        #print(f"Subred válida (CIDR): {subred}, direccion de broadcast: {broadcast}, rango de ips validas: {primera_ip} - {ultima_ip}")

    # Imprimir resultados en una tabla
    headers = ["Subred válida (CIDR)", "Dirección de broadcast", "Rango de IPs válidas"]
    table = [[subred, broadcast, f"{primera_ip} - {ultima_ip}"] for subred, broadcast, primera_ip, ultima_ip in subredes_validas]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()

subredes_clases = [
    ["10.100.0.0/27", "C"],
    ["192.168.56.0/30", "C"],
    ["192.168.56.0/30", "B"],
    ["172.16.0.0/24", "C"],
    ["172.16.0.0/24", "B"],
    ["10.0.0.0/12", "A"]
]

print()

print("Calculando subredes válidas y direcciones de broadcast")
pos = 3
calculo(subredes_clases[pos][0], subredes_clases[pos][1])