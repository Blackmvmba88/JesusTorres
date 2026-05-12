# Meta-comandos para el proyecto Audio Waveform

.PHONY: help run doctor install clean git-update release

VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

help:
	@echo "Comandos disponibles:"
	@echo "  make run          - Ejecuta la visualización reactiva"
	@echo "  make doctor       - Ejecuta el diagnóstico de errores"
	@echo "  make install      - Instala dependencias y configura el entorno"
	@echo "  make clean        - Borra archivos temporales y el entorno virtual"
	@echo "  make git-update   - Agrega cambios, hace commit y push (pide mensaje)"
	@echo "  make release      - Crea un tag v1.0.0 y hace el release en GitHub"

run:
	$(PYTHON) reactive_wave.py

doctor:
	$(PYTHON) doctor.py

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install numpy matplotlib pyaudio
	@echo "Entorno listo. Prueba con 'make run'"

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -f .DS_Store

git-update:
	@read -p "Mensaje del commit: " msg; \
	git add .; \
	git commit -m "$$msg"; \
	git push origin main

release:
	@echo "Creando release v1.0.0..."
	git tag -a v1.0.0 -m "Versión estable inicial: Rainbow Wave con AGC"
	git push origin v1.0.0
	gh release create v1.0.0 --title "v1.0.0 - Primera Versión Estable" --notes "Visualización de onda sinusoidal reactiva con control automático de ganancia (PID/AGC) y estética rainbow."
