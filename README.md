# Reactive Audio Waveform

Este proyecto visualiza una onda de audio en tiempo real usando el micrófono, con un efecto de arcoíris y control automático de ganancia (AGC/PID).

## Requisitos
- Python 3
- PortAudio (requerido por `pyaudio` en macOS: `brew install portaudio`)

## Instalación y Ejecución

1. Activa el entorno virtual:
   ```bash
   source env/bin/activate
   ```

2. Ejecuta el script:
   ```bash
   python reactive_wave.py
   ```

## Características
- **Fondo Negro**: Optimizado para estética visual.
- **Línea Rainbow**: La onda cambia de color dinámicamente.
- **Control PID/AGC**: Si hablas bajo, la onda se amplifica. Si hablas fuerte, se regula para no saturar.
- **Reactividad**: Basado en `pyaudio` para baja latencia.
