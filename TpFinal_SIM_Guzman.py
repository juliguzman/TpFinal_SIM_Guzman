import math
import tkinter as tk
from tkinter import ttk, messagebox, font
import random


def validar_numeros_coma(event):
    char = event.char
    if not (char.isdigit() or char == '.' or char == '\b'):
        return 'break'


def validar_numeros_entero(event):
    char = event.char
    if not (char.isdigit() or char == '\b'):
        return 'break'


def inicializar_pantalla():
    ventana = tk.Tk()
    ventana.geometry("520x535")
    ventana.title("TP5 - Simulación - Grupo 6")
    ventana.resizable(False, False)

    variabley = 5
    variablex = 375
    incremento = 30

    etiqueta1 = tk.Label(ventana, text="Ingrese la cantidad de tiempo a simular (X)(milisegundos): ")
    etiqueta1.place(x=5, y=5)
    tiempo = tk.Entry(ventana)
    tiempo.place(x=variablex, y=5)
    tiempo.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta2 = tk.Label(ventana, text="Ingrese la cantidad de iteraciones a mostrar (i): ")
    etiqueta2.place(x=5, y=variabley)
    mostrar = tk.Entry(ventana)
    mostrar.place(x=variablex, y=variabley)
    mostrar.bind('<Key>', validar_numeros_entero)

    variabley += incremento

    etiqueta3 = tk.Label(ventana, text="Ingrese el tiempo de iteración a partir del cual mostrar (j): ")
    etiqueta3.place(x=5, y=variabley)
    apartir = tk.Entry(ventana)
    apartir.place(x=variablex, y=variabley)
    apartir.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta4 = tk.Label(ventana, text="Ingrese la Media para la llegada de Paquetes: ")
    etiqueta4.place(x=5, y=variabley)
    media = tk.Entry(ventana)
    media.config(bg="lightblue")
    media.insert(0, "0.5")
    media.place(x=variablex, y=variabley)
    media.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta5 = tk.Label(ventana, text="Ingrese la Desviacion Estandar para la llegada de paquetes: ")
    etiqueta5.place(x=5, y=variabley)
    desviacion = tk.Entry(ventana)
    desviacion.config(bg="lightblue")
    desviacion.insert(0, "0.1")
    desviacion.place(x=variablex, y=variabley)
    desviacion.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta6 = tk.Label(ventana, text="Ingrese el valor de la probabilidad1: ")
    etiqueta6.place(x=5, y=variabley)
    valor1 = tk.Entry(ventana)
    valor1.config(bg="lightgreen")
    valor1.insert(0, "1.3")
    valor1.place(x=variablex, y=variabley)
    valor1.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta7 = tk.Label(ventana, text="Ingrese el valor de la probabilidad2: ")
    etiqueta7.place(x=5, y=variabley)
    valor2 = tk.Entry(ventana)
    valor2.config(bg="lightgreen")
    valor2.insert(0, "2.5")
    valor2.place(x=variablex, y=variabley)
    valor2.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta8 = tk.Label(ventana, text="Ingrese la media de exp neg de la probabilidad3: ")
    etiqueta8.place(x=5, y=variabley)
    valor3 = tk.Entry(ventana)
    valor3.config(bg="lightgreen")
    valor3.insert(0, "2")
    valor3.place(x=variablex, y=variabley)
    valor3.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta9 = tk.Label(ventana, text="Ingrese la probabilidad1: ")
    etiqueta9.place(x=5, y=variabley)
    prob1 = tk.Entry(ventana)
    prob1.config(bg="lightpink")
    prob1.insert(0, "0.35")
    prob1.place(x=variablex, y=variabley)
    prob1.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta10 = tk.Label(ventana, text="Ingrese la probabilidad2: ")
    etiqueta10.place(x=5, y=variabley)
    prob2 = tk.Entry(ventana)
    prob2.config(bg="lightpink")
    prob2.insert(0, "0.30")
    prob2.place(x=variablex, y=variabley)
    prob2.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta11 = tk.Label(ventana, text="Ingrese la probabilidad3: ")
    etiqueta11.place(x=5, y=variabley)
    prob3 = tk.Entry(ventana)
    prob3.config(bg="lightpink")
    prob3.insert(0, "0.35")
    prob3.place(x=variablex, y=variabley)
    prob3.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    boton_generar = tk.Button(ventana,
                              text="Simular",
                              command=lambda: simular(tiempo, mostrar, apartir, media, desviacion, valor1, valor2,
                                                      valor3, prob1, prob2, prob3),
                              width=10, height=2)
    boton_generar.place(x=200, y=variabley)

    ventana.mainloop()


def tablaTiempoBuffer(rnd, probabilidades, valor):
    if rnd >= 1:
        rnd = rnd - 0.1
    if rnd < probabilidades[0]:
        return valor[0]

    elif rnd < probabilidades[0] + probabilidades[1]:
        return valor[1]

    elif rnd <= probabilidades[0] + probabilidades[1] + probabilidades[2]:
        exponencial = (-valor[2]) * math.log(1 - rnd)
        return round(exponencial, 2)



def simular(tiempo, mostrar, apartir, media, desviacion, valor1, valor2, valor3, prob1, prob2, prob3):
    if not valida_entradas(tiempo, mostrar, apartir, media, desviacion, valor1, valor2, valor3, prob1, prob2, prob3):
        return

    tiempo_a_simular = float(tiempo.get())
    apartir_de_fila_j = int(apartir.get())
    cantidad_filas_mostrar_i = int(mostrar.get())

    media_paquetes = float(media.get())
    desviacion_paquetes = float(desviacion.get())

    probabilidades = [float(prob1.get()), float(prob2.get()), float(prob3.get())]

    valor_probabilidades = [float(valor1.get()), float(valor2.get()), float(valor3.get())]

    filas = [["",  # Evento
              0,  # Reloj
              0,  # rnd1
              0,  # rnd2
              0,  # n1
              0,  # n2
              0,  # Llegada Paquete
              0,  # rnd
              0,  # tiempo
              0,  # fin analizador buffer 1 1
              0,  # fin analizador buffer 1 2
              0,  # fin analizador buffer 2 1
              0,  # fin analizador buffer 2 2
              0,  # fin analizador buffer 3 1
              0,  # fin analizador buffer 3 2
              "", "", "",  # estados de bufers
              0, 0, 0, 0],
             ["",
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0,
              "", "", "",
              0, 0, 0, 0]]

    temporalPaquetes = []

    no_se_paso_de_x = True
    iteraciones = 0

    j = 0
    eventos_proximos = []
    contador_filas_agregadas = 0
    ultimo_indice_simulacion = 0

    cantidad_ocupados = 0

    root = tk.Tk()
    root.geometry("520x450")
    root.title("Tabla simulación")
    table = ttk.Treeview(root)
    headers = ["Evento", "Reloj(miliseg)", "RND1", "RND2", "Valor N1", "Valor N2",
               "LlegadaPaquete", "RND", "Tiempo", "Buffer1_1", "Buffer1_2", "Buffer2_1", "Buffer2_2", "Buffer3_1",
               "Buffer3_2", "Estado1.", "Estado2", "Estado3", "Ac Paquetes Analizados",
               "AcPaquetes No Aalizados", "Probabilida", "FinSimulacion",
               "EstadoPaquete1", "EstadoPaquete2", "EstadoPaquete3", "EstadoPaquete4", "EstadoPaquete5",
               "EstadoPaquete6", "EstadoPaquete7", "EstadoPaquete8"]
    table["columns"] = headers
    table["show"] = "headings"
    for header in headers:
        table.heading(header, text=header)

    while no_se_paso_de_x and iteraciones <= 100000:  # Para recorrer cada iteración

        if j % 2 == 0:
            indice = 0
        else:
            indice = 1

        for m in range(len(filas[indice])):
            if m != len(filas[indice]) - 1:
                filas[indice][m] = "-"

        if iteraciones == 0:
            filas[indice][0] = "Inicialización"
            filas[indice][1] = 0
            filas[indice][2] = round(random_excluyendo_extremos(), 5)
            filas[indice][3] = round(random_excluyendo_extremos(), 5)
            filas[indice][4] = round(valor_n1_n2(float(filas[indice][2]), float(filas[indice][3]), desviacion_paquetes,
                                                 media_paquetes, primerValor=True), 2)
            filas[indice][5] = round(valor_n1_n2(float(filas[indice][2]), float(filas[indice][3]), desviacion_paquetes,
                                                 media_paquetes, primerValor=False), 2)
            filas[indice][6] = round(filas[indice][1] + filas[indice][4], 2)  # reloj + valor de n1
            eventos_proximos.append((filas[indice][6], "LlegadaPaquete"))

            for i in range(7, 15):
                filas[indice][i] = 0
            filas[indice][15] = "Libre"
            filas[indice][16] = "Libre"
            filas[indice][17] = "Libre"
            filas[indice][18] = 0
            filas[indice][19] = 0
            filas[indice][20] = 0
            filas[indice][21] = tiempo_a_simular
            eventos_proximos.append((filas[indice][21], "FinSimulacion"))

        else:

            proximo_evento = seleccionar_proximo_evento(eventos_proximos)
            eventos_proximos.remove(proximo_evento)
            filas[indice][0] = proximo_evento[1]
            filas[indice][1] = proximo_evento[0]

            if proximo_evento[1] == "LlegadaPaquete":

                filas[indice][18] = filas[indice - 1][18] + 1

                filas[indice][8] = filas[indice - 1][8]

                if filas[indice - 1][5] == "-" or filas[indice - 1][4] == "-":
                    filas[indice][2] = round(random_excluyendo_extremos(), 5)
                    filas[indice][3] = round(random_excluyendo_extremos(), 5)

                    filas[indice][4] = round(valor_n1_n2(float(filas[indice][2]), float(filas[indice][3]),
                                                         desviacion_paquetes, media_paquetes, primerValor=True), 2)
                    filas[indice][5] = round(valor_n1_n2(float(filas[indice][2]), float(filas[indice][3]),
                                                         desviacion_paquetes, media_paquetes, primerValor=False), 2)
                    filas[indice][6] = round(filas[indice][1] + filas[indice][4], 2)  # reloj + valor de n1

                else:
                    filas[indice][5] = filas[indice - 1][5]
                    filas[indice][6] = round(filas[indice][1] + filas[indice][5], 2)

                eventos_proximos.append((filas[indice][6], "LlegadaPaquete"))

                if cantidad_ocupados < 6:
                    cantidad_ocupados += 1
                    filas[indice][7] = round(random_excluyendo_extremos(), 2)
                    filas[indice][8] = tablaTiempoBuffer(filas[indice][7], probabilidades, valor_probabilidades)
                    filas[indice][19] = filas[indice - 1][19]
                    se_ocupo = False

                    for i in range(9, 15):  # Buscamos primer lugar libre
                        if (filas[indice - 1][i] == "-" or filas[indice - 1][i] == 0) and not se_ocupo:
                            filas[indice][i] = round(filas[indice][1] + filas[indice][8], 2)  # Prox finAnalizador
                            eventos_proximos.append((filas[indice][i], "FinAnalizador"))
                            se_ocupo = True
                            temporalPaquetes.append(["EnAnalisis", filas[indice][i]])  # Agregar objeto temporal

                        else:
                            filas[indice][i] = filas[indice - 1][i]
                else:
                    temporalPaquetes.append(["SinAnalisis", 0])  # Agregar objeto temporal

                filas[indice][15] = determinar_estado(filas[indice][9], filas[indice][10])
                filas[indice][16] = determinar_estado(filas[indice][11], filas[indice][12])
                filas[indice][17] = determinar_estado(filas[indice][13], filas[indice][14])

                if filas[indice][15] == "Ocupado" and filas[indice][16] == "Ocupado" and filas[indice][17] == "Ocupado":
                    filas[indice][19] = filas[indice - 1][19] + 1

                    for i in range(9, 15):
                        filas[indice][i] = filas[indice - 1][i]

                if filas[indice][18] != 0:
                    filas[indice][20] = round(filas[indice][19] / filas[indice][18], 5)
                else:
                    filas[indice][20] = None

                filas[indice][21] = filas[indice - 1][21]

            elif proximo_evento[1] == "FinSimulacion":
                ultimo_indice_simulacion = indice

                no_se_paso_de_x = False
                filas[indice][5] = filas[indice - 1][5]
                filas[indice][6] = filas[indice - 1][6]
                for i in range(9, 15):
                    filas[indice][i] = filas[indice - 1][i]
                for i in range(15, 18):  # Bajar estados
                    filas[indice][i] = filas[indice - 1][i]

                filas[indice][18] = filas[indice - 1][18]
                filas[indice][19] = filas[indice - 1][19]
                filas[indice][20] = filas[indice - 1][20]

            elif proximo_evento[1] == "FinAnalizador":
                cantidad_ocupados -= 1
                filas[indice][8] = 0

                valores = [filas[indice - 1][9], filas[indice - 1][10], filas[indice - 1][11],
                           filas[indice - 1][12], filas[indice - 1][13], filas[indice - 1][14]]

                filas[indice][5] = filas[indice - 1][5]
                filas[indice][6] = filas[indice - 1][6]  # Bajar próxima llegada

                for i in range(9, 15):
                    if filas[indice - 1][i] == filas[indice][1]:  # Eliminar el que acaba de ocurrir
                        filas[indice][i] = 0
                    else:
                        filas[indice][i] = filas[indice - 1][i]  # Bajar otros finAnalizadores

                filas[indice][15] = determinar_estado(filas[indice][9], filas[indice][10])
                filas[indice][16] = determinar_estado(filas[indice][11], filas[indice][12])
                filas[indice][17] = determinar_estado(filas[indice][13], filas[indice][14])

                filas[indice][18] = filas[indice - 1][18]
                filas[indice][19] = filas[indice - 1][19]
                filas[indice][20] = filas[indice - 1][20]
                filas[indice][21] = tiempo_a_simular  # Bajar fin_simulación

                cambiar_estado_paquetes(temporalPaquetes, filas[indice][1], "FinAnalizador")

        j += 1
        iteraciones += 1
        if iteraciones >= apartir_de_fila_j:
            if cantidad_filas_mostrar_i > contador_filas_agregadas:
                contador_filas_agregadas += 1
                paquetes = [sublist[0] for sublist in temporalPaquetes]
                table.insert("", "end", values=filas[indice] + paquetes)

    table.insert("", "end", values=filas[ultimo_indice_simulacion])

    for header in headers:
        table.column(header, anchor="center", width=75)
    scrollbar1 = ttk.Scrollbar(table, orient="horizontal", command=table.xview)
    scrollbar2 = ttk.Scrollbar(table, orient="vertical", command=table.yview)
    table.configure(xscrollcommand=scrollbar1.set)
    table.configure(yscrollcommand=scrollbar2.set)
    table.pack(side="top", fill="both", expand=True)
    scrollbar1.pack(side="bottom", fill="x")
    scrollbar2.pack(side="right", fill="y")
    etiqueta_resultado = tk.Label(root, text="El promedio final es de: " +
                                             str(filas[ultimo_indice_simulacion][20]),
                                  font=font.Font(weight="bold", size=20))
    etiqueta_resultado.pack(side="bottom")


def random_excluyendo_extremos():
    while True:
        num = random.random()
        if 0 < num < 1:
            return num


def seleccionar_proximo_evento(proximos_eventos):
    j = 0
    prox = ()
    for i in proximos_eventos:
        if j == 0:
            prox = i
        else:
            if prox[0] >= i[0]:
                prox = i
        j += 1
    return prox


def valor_n1_n2(rnd1, rnd2, desviacion, media, primerValor):
    if primerValor:
        n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
        return n1
    else:
        n2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * math.pi * rnd2)) * desviacion + media
        return n2


def valida_entradas(text_box_tiempo, text_box_iteraciones_mostrar, text_box_tiempo_apartir, media, desviacion, valor1,
                    valor2, valor3, prob1, prob2, prob3):
    mensaje_error = "Por favor, ingrese números válidos en los campos."
    res = True

    try:
        tiempo_simular = int(text_box_tiempo.get())
        param_i = int(text_box_iteraciones_mostrar.get())
        param_j = int(text_box_tiempo_apartir.get())

        media_paquetes = float(media.get())
        desviacion_paquetes = float(desviacion.get())

        valor1_prob = float(valor1.get())
        valor2_prob = float(valor2.get())
        valor3_prob = float(valor3.get())

        probabilidad1 = float(prob1.get())
        probabilidad2 = float(prob2.get())
        probabilidad3 = float(prob3.get())

        if param_j < 0 or param_j > 100000:
            mensaje_error = "Se puede mostrar a partir de la iteración 0, hasta la iteración 100000."
            raise ValueError()

        if param_i <= 0:
            mensaje_error = "i debe ser mayor o igual a 1."
            raise ValueError()

        tolerancia = 1e-6

        if abs((probabilidad1 + probabilidad2 + probabilidad3) - 1) > tolerancia:
            mensaje_error = "Error con las probabilidades."
            raise ValueError(mensaje_error)

        if media_paquetes > 1 or desviacion_paquetes > 1:
            mensaje_error = "la media y la desviacion estandar deben estar entre 0 y 1."
            raise ValueError()

        if valor1_prob < 0 or valor2_prob < 0 or valor3_prob < 0:
            mensaje_error = "Los valores de las probabilidades no pueden ser negativas."
            raise ValueError()

        if tiempo_simular <= 0:
            mensaje_error = "No puede haber tiempos negativos o 0."
            raise ValueError()

        return res

    except ValueError:
        messagebox.showerror("Error", mensaje_error)
        res = False
        return res


def cambiar_estado_paquetes(paquetes, reloj_actual, evento):
    if evento == "FinAnalizador":
        for i in paquetes:   # Busca el auto con menor fin_estacionamiento para cobrarle
            if i[1] == reloj_actual:
                i[0] = "-"


def determinar_estado(estado1, estado2):
    if estado1 != 0 and estado2 == 0 or estado1 == 0 and estado2 != 0:
        return "Analizando 1 Paquete"
    elif estado1 != 0 and estado2 != 0:
        return "Ocupado"
    elif estado1 == 0 and estado2 == 0:
        return "Libre"


if __name__ == '__main__':
    inicializar_pantalla()
