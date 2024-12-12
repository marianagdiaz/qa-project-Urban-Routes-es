# Urban Routes Project

## Descripción del Proyecto
Urban Routes es un proyecto automatizado para probar una aplicación de solicitud de servicios de taxi. Las pruebas incluyen la interacción con formularios, la selección de opciones de viaje, métodos de pago y características adicionales, garantizando la calidad de las funcionalidades clave de la aplicación.

## Tecnologías y Técnicas Utilizadas
- **Lenguaje de programación**: Python
- **Framework de pruebas**: `pytest`
- **Automatización web**: Selenium WebDriver
- **Diseño estructurado**:
  
  - **Modelo de Objetos de Página (Page Object Model, POM)**: Para separar la lógica de pruebas de los elementos y acciones de las páginas, facilitando la mantenibilidad y escalabilidad.
  - **Páginas de localizadores (Page Objects)**: Para mantener los selectores organizados.
  - **Métodos funcionales**: Para encapsular las acciones relacionadas con los elementos.
  - **Pruebas unitarias y de integración**: Validación del flujo completo de la aplicación.

### Herramientas adicionales
- **Manejo de elementos dinámicos**: Uso de `WebDriverWait` y condiciones esperadas.
- **Extracción de datos dinámicos**: Implementación de logs de rendimiento de Chrome para obtener códigos de confirmación.

## Instrucciones para Ejecutar las Pruebas

### Requisitos previos
1. **Instalar Python y las dependencias**:
   Asegúrate de tener Python instalado en tu sistema. Luego, instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt

Configurar WebDriver: Descarga el ChromeDriver compatible con tu navegador y colócalo en una ubicación accesible por el sistema.

Archivo de configuración: Crea un archivo data.py con las siguientes variables:


- urban_routes_url = "URL_de_la_aplicación"
- address_from = "Dirección inicial"
- address_to = "Dirección final"
- phone_number = "Número_de_teléfono"
- card_number = "Número_de_tarjeta"
- card_code = "Código_de_seguridad"
- message_for_driver = "Mensaje para el conductor"


 ### **Ejecución de las pruebas** 

- Abre una terminal en el directorio raíz del proyecto.

- Activa el entorno virtual en Windows:
`.\venv\Scripts\activate`



 **Ejecuta las pruebas con el siguiente comando:**

    *pytest*


### **Opciones adicionales**

- Para ejecutar un archivo de prueba específico:

`pytest test_nombre_archivo.py`
- Para obtener un informe detallado:

`pytest -v`