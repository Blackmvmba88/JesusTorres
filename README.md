# 🌈 JesusGabrielTorres: Reactive Audio Waveform

**JesusGabrielTorres** es una visualización de onda sinusoidal reactiva al audio en tiempo real, desarrollada con Python, NumPy y Matplotlib. El sistema incluye un control automático de ganancia (AGC/PID) para normalizar la amplitud visual sin importar el volumen de entrada.

## ✨ Características

- **Visualización Rainbow**: Línea con degradado de colores dinámico que cambia con el tiempo.
- **Fondo Negro Estético**: Optimizado para pantallas de alto contraste y presentaciones.
- **Control Automático de Ganancia (PID/AGC)**: 
  - Sonidos bajos: Se amplifican automáticamente para ser visibles.
  - Sonidos altos: Se regulan para evitar que la onda sature la pantalla.
- **Manejo de Procesos**: Cierre seguro del flujo de audio y procesos del sistema.
- **Sistema de Diagnóstico**: Script "Doctor" incluido para detectar y reparar fallos de dependencias.

## 🛠 Instalación Rápida

Este proyecto utiliza un `Makefile` para simplificar la gestión.

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Blackmvmba88/JesusTorres.git
   cd JesusTorres
   ```

2. **Configurar el entorno e instalar dependencias:**
   ```bash
   make install
   ```
   *(Nota: En macOS, asegúrate de tener PortAudio: `brew install portaudio`)*

## 🚀 Uso (Meta-comandos)

Usa los siguientes comandos `make` para gestionar el proyecto:

- `make run`: Inicia la visualización **JesusGabrielTorres**.
- `make doctor`: Ejecuta el diagnóstico de errores y verifica dependencias.
- `make git-update`: Sube cambios rápidos a GitHub.
- `make clean`: Limpia archivos temporales y el entorno virtual.

## 📁 Estructura del Proyecto

- `reactive_wave.py`: Motor principal de visualización y procesamiento de audio.
- `doctor.py`: Herramienta de mantenimiento y reparación.
- `Makefile`: Automatización de tareas (meta-comandos).
- `env/`: Entorno virtual de Python (ignorado en Git).

## 👤 Autor

**Iyari Cancino Gomez**

---
Desarrollado con ⚡️ y precisión por **Iyari Cancino Gomez** para el sistema **JesusGabrielTorres**.
