def calcular_equipos (mascara):
    # separar por puntos
    octetos = mascara.split(".")
    print(octetos)

    # convertir a binario manualmente. Por ejemplo, 255 -> 11111111, 64 -> 01000000...
    # Pir ejemplo, 64 -> 01000000 debe ir el 0 al principio. 
    octetos_bin = []
    for octeto in octetos:
        binario = bin(int(octeto))[2:]
        binario = "0"*(8-len(binario)) + binario
        octetos_bin.append(binario)

    print(f"Los octetos en binario son: {octetos_bin}")

    # Unir todos los octetos en una sola cadena
    mascara_bin = "".join(octetos_bin)

    # Encontrar la posición del último '1'
    ultimo_1 = mascara_bin.rfind('1')

    # contar los ceros significativos (los que están después del último '1')
    ceros = len(mascara_bin) - (ultimo_1 + 1)

    print(f"La cantidad de ceros después del último bit significativo es {ceros}")

    # calcular la cantidad de equipos
    equipos = 2**ceros - 2  # restar 2 para excluir la dirección de red y la de broadcast
    if equipos < 0:
        equipos = 0

    print(f"La cantidad de equipos es {equipos}")
    print()



mascaras = ["255.255.255.64", "255.255.255.128", "255.255.255.255"]
for i in mascaras:
    calcular_equipos(i)

