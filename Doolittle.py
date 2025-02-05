
import streamlit as st
import numpy as np

def doolittle_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))#Matrices inicializadas con 0
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            U[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        L[i][i] = 1
        for j in range(i + 1, n):
            L[j][i] = (matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

# Título de la aplicación
st.title("Método Doolittle - Descomposición LU")

# Entrada para el tamaño de la matriz
n = st.number_input("Tamaño de la matriz (n x n):", min_value=2, max_value=10, step=1, value=3)

# Espacio para los datos de la matriz en formato visual
st.write(f"Ingrese los valores para una matriz de tamaño {n}x{n}:")

# Crear una matriz dinámica para la entrada
matrix = []
error_flag = False
diagonal_zero_flag = False

for i in range(n):
    row = []
    cols = st.columns(n)  # Crear columnas para simular filas de la matriz
    for j in range(n):
        with cols[j]:
            value = st.number_input(f"[{i+1}, {j+1}]", key=f"matrix-{i}-{j}", value=0.0)
            row.append(value)
    matrix.append(row)

# Convertir la lista de listas a un arreglo NumPy
matrix = np.array(matrix)

# Validar la diagonal principal
for i in range(n):
    if matrix[i, i] == 0:
        diagonal_zero_flag = True
        break

# Mostrar error si la diagonal principal tiene ceros
if diagonal_zero_flag:
    st.error("Error: Ningún elemento de la diagonal principal puede ser 0.")

# Botón para calcular L y U
if st.button("Calcular L y U"):
    if diagonal_zero_flag:
        st.error("Corrige los valores en la diagonal principal antes de continuar.")
    else:
        try:
            matrix = np.array(matrix)  # Convertir a matriz NumPy
            L, U = doolittle_decomposition(matrix)

            st.write("Matriz L:")
            st.write(L)

            st.write("Matriz U:")
            st.write(U)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

