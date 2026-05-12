import os
import sys
import subprocess
import shutil

def check_command(cmd):
    return shutil.which(cmd) is not None

def run_doctor():
    print("=== Audio Waveform Doctor ===\n")
    
    # 1. Check Python
    print(f"[*] Python version: {sys.version.split()[0]}")
    
    # 2. Check Virtual Env
    if os.path.exists("env"):
        print("[OK] Entorno virtual 'env' detectado.")
    else:
        print("[!] Error: No se encontró la carpeta 'env'.")
        return
    
    # 3. Check Dependencies
    pip_path = "env/bin/pip"
    if not os.path.exists(pip_path):
        pip_path = "env/Scripts/pip" # Windows support
        
    required = ["numpy", "matplotlib", "pyaudio"]
    print("[*] Verificando dependencias...")
    
    try:
        installed = subprocess.check_output([pip_path, "freeze"]).decode()
        for pkg in required:
            if pkg in installed.lower():
                print(f"  [OK] {pkg} instalado.")
            else:
                print(f"  [!] {pkg} NO encontrado. Intentando instalar...")
                subprocess.run([pip_path, "install", pkg])
    except Exception as e:
        print(f"[!] Error al verificar dependencias: {e}")

    # 4. Check PortAudio (macOS specific)
    if sys.platform == "darwin":
        if check_command("brew"):
            print("[*] Verificando PortAudio vía Homebrew...")
            result = subprocess.run(["brew", "list", "portaudio"], capture_output=True)
            if result.returncode != 0:
                print("  [!] PortAudio no detectado. Instalando...")
                subprocess.run(["brew", "install", "portaudio"])
            else:
                print("  [OK] PortAudio está presente.")
    
    print("\n[FIN] Todo parece estar en orden. ¡Listo para rockear!")

if __name__ == "__main__":
    run_doctor()
