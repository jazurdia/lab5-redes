def ip_a_red(ip, mascara):
    # Convertir IP y máscara a binario
    ip_bin = ''.join(f"{int(octeto):08b}" for octeto in ip.split('.'))
    mascara_bin = ''.join(f"{int(octeto):08b}" for octeto in mascara.split('.'))

    # Realizar la operación AND
    red_bin = ''.join('1' if ip_bit == '1' and mask_bit == '1' else '0'
                      for ip_bit, mask_bit in zip(ip_bin, mascara_bin))

    # Convertir de binario a decimal
    red_decimal = '.'.join(str(int(red_bin[i:i + 8], 2)) for i in range(0, 32, 8))
    
    # Calcular el prefijo de la máscara
    prefijo = mascara_bin.count('1')
    
    return red_decimal, prefijo


# Direcciones IP y máscaras
direcciones = [
    ("135.1.1.25", "255.255.248.0"),
    ("222.1.1.20", "255.255.255.192"),
    ("205.11.2.0", "255.192.0.0"),
    ("56.8.95.78", "255.128.0.0"),  # /9
    ("8.9.6.3", "255.224.0.0")       # /11
]

# Cálculo de la red para cada dirección IP
for ip, mascara in direcciones:
    if '/' in mascara:  # Si la máscara es en formato CIDR
        prefijo = int(mascara.split('/')[1])
        mascara_decimal = '.'.join(str((255 << (8 - (prefijo % 8))) & 255) for _ in range(4))
        mascara_decimal = '.'.join(str(255 if prefijo >= 8 * (i + 1) else 0) for i in range(4))
        mascara_decimal = '.'.join(str(255 if prefijo >= 8 * (i + 1) else (255 << (8 - (prefijo - 8 * i))) & 255) for i in range(4))
    else:
        mascara_decimal = mascara
    
    red, prefijo = ip_a_red(ip, mascara_decimal)
    print(f"La dirección IP {ip} con máscara {mascara_decimal} pertenece a la red {red}/{prefijo}.")