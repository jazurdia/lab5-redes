def direccion_a_binario(direccion):
    return ''.join(f'{int(octeto):08b}' for octeto in direccion.split('.'))

def binario_a_direccion(binario):
    return '.'.join(str(int(binario[i:i+8], 2)) for i in range(0, 32, 8))

def calcular_subredes(direccion_red, prefijo):
    # Convertir la dirección IP a binario
    red_bin = direccion_a_binario(direccion_red)
    
    # Calcular la cantidad de bits para hosts
    bits_red = prefijo
    bits_host = 32 - bits_red

    # Calcular la cantidad de direcciones y equipos válidos
    total_ips = 2 ** bits_host
    ips_validas = total_ips - 2  # Restamos la dirección de red y la de broadcast

    # Cantidad de subredes producidas por la máscara
    subredes_producidas = 2 ** (bits_red - prefijo)

    # Crear la máscara de subred
    mascara_binaria = '1' * bits_red + '0' * bits_host
    mascara_direccion = binario_a_direccion(mascara_binaria)

    # Subredes válidas
    subredes = []
    for i in range(0, total_ips, 2 ** bits_host):
        subred_bin = red_bin[:bits_red] + f'{i:0{bits_host}b}'
        subredes.append(binario_a_direccion(subred_bin) + f'/{prefijo}')

    # Calcular las IPs válidas, direcciones de broadcast, y el rango de equipos válidos por subred
    for subred in subredes:
        direccion_broadcast = binario_a_direccion(subred_bin[:bits_red] + '1' * bits_host)
        primer_equipo_bin = subred_bin[:bits_red] + '0' * (bits_host - 1) + '1'
        ultimo_equipo_bin = subred_bin[:bits_red] + '1' * (bits_host - 1) + '0'
        primer_equipo = binario_a_direccion(primer_equipo_bin)
        ultimo_equipo = binario_a_direccion(ultimo_equipo_bin)

        print(f"\nSubred válida (CIDR): {subred}")
        print(f"Dirección de broadcast: {direccion_broadcast}")
        print(f"Rango de IPs válidas: {primer_equipo} – {ultimo_equipo}")

    print(f"\nRed: {direccion_red}/{prefijo}")
    print(f"Máscara de subred: {mascara_direccion}")
    print(f"Total de subredes producidas: {subredes_producidas}")
    print(f"IPs válidas por subred: {ips_validas}")


# Ejemplo de uso:
redes = [("10.100.0.0", 27), ("192.168.56.0", 30), ("172.16.0.0", 24), ("10.0.0.0", 12)]

for red, prefijo in redes:
    calcular_subredes(red, prefijo)
