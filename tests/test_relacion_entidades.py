import requests

API_PRODUCTS_URL = "http://localhost:8080/api/products"

# -----------------------------
# Función auxiliar para pruebas
# -----------------------------
def ejecutar_prueba(endpoint_url, titulo_prueba, codigos_esperados=[200]):
    print(f"\n[TEST] {titulo_prueba}")
    try:
        respuesta = requests.get(endpoint_url)
        if respuesta.status_code in codigos_esperados:
            print(f"[OK] Código {respuesta.status_code}")
            try:
                datos = respuesta.json()
                if isinstance(datos, dict):
                    print(f"  Campos: {list(datos.keys())}")
                elif isinstance(datos, list):
                    print(f"  Total registros: {len(datos)}")
            except:
                print("  Respuesta sin formato JSON")
        else:
            print(f"[ERROR] Código {respuesta.status_code}")
            print(respuesta.text[:200])
    except Exception as error:
        print(f"[ERROR] {str(error)}")


# -----------------------------
# Casos de prueba individuales
# -----------------------------

def prueba_paginacion_simple():
    endpoint = f"{API_PRODUCTS_URL}?page=0&size=5"
    ejecutar_prueba(endpoint, "1. Paginación básica")


def prueba_paginacion_ordenada():
    endpoint = f"{API_PRODUCTS_URL}?page=1&size=10&sort=price,desc"
    ejecutar_prueba(endpoint, "2. Paginación con ordenamiento por precio descendente")


def prueba_ordenamiento_multiple():
    endpoint = f"{API_PRODUCTS_URL}?page=0&size=5&sort=categories.name,asc&sort=price,desc"
    ejecutar_prueba(endpoint, "3. Ordenamiento múltiple por categoría y precio")


def prueba_slice_rendimiento():
    endpoint = f"{API_PRODUCTS_URL}/slice?page=0&size=10&sort=createdAt,desc"
    ejecutar_prueba(endpoint, "4. Consulta tipo Slice para performance")


def prueba_busqueda_con_filtros():
    endpoint = f"{API_PRODUCTS_URL}/search?name=gaming&minPrice=500&page=0&size=3"
    ejecutar_prueba(endpoint, "5. Búsqueda filtrada con paginación")


def prueba_productos_por_usuario():
    id_usuario = 1
    endpoint = f"{API_PRODUCTS_URL}/user/{id_usuario}?page=0&size=5&sort=name,asc"
    ejecutar_prueba(endpoint, "6. Productos por usuario con paginación")


def prueba_error_validacion():
    endpoint = f"{API_PRODUCTS_URL}?page=-1&size=0"
    ejecutar_prueba(endpoint, "7.1 Validación de parámetros inválidos", codigos_esperados=[400])


def prueba_campo_ordenamiento_invalido():
    endpoint = f"{API_PRODUCTS_URL}?sort=invalidField,asc"
    ejecutar_prueba(endpoint, "7.2 Campo de ordenamiento inválido", codigos_esperados=[400])


# -----------------------------
# Ejecución principal del script
# -----------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBAS DE ENDPOINTS PAGINADOS - PRODUCTCONTROLLER")
    print("=" * 60)

    prueba_paginacion_simple()
    prueba_paginacion_ordenada()
    prueba_ordenamiento_multiple()
    prueba_slice_rendimiento()
    prueba_busqueda_con_filtros()
    prueba_productos_por_usuario()
    prueba_error_validacion()
    prueba_campo_ordenamiento_invalido()

    print("\nProceso de pruebas finalizado")