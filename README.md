# Detector de Movimiento y Personas en Tiempo Real

## Descripción

Este proyecto utiliza la cámara web para detectar movimiento en tiempo real y, además, identifica si hay personas presentes usando un detector preentrenado de OpenCV. Cuando se detecta movimiento junto con la presencia de personas, guarda automáticamente una imagen con la fecha y hora en una carpeta llamada `capturas`.

Es una solución sencilla, liviana y que no requiere entrenar modelos adicionales. Ideal para vigilancia básica, monitoreo en el hogar o proyectos educativos de visión artificial.

---

## Funcionalidades principales

- Detecta movimiento comparando cuadros consecutivos de video.
- Detecta personas usando el detector HOG + SVM de OpenCV.
- Guarda imágenes automáticamente con sello de fecha y hora cuando detecta movimiento con personas.
- Muestra en pantalla rectángulos verdes para movimiento y rectángulos azules para personas detectadas.
- Espera un tiempo configurable (por defecto 5 minutos) antes de guardar otra captura para evitar múltiples archivos similares.

---

## Requisitos

- Python 3.8 a 3.11 (recomendado Python 3.10)
- Librerías Python:
  - opencv-python

---

## Instalación y uso

1. **Clonar o descargar el repositorio**

   ```bash
   git clone <url-del-repositorio>
   cd <carpeta-del-proyecto>
## Crear entorno virtual

