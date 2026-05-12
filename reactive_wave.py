import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import pyaudio
import time
import sys
import signal

# --- CONFIGURATION ---
CHUNK = 1024          # Samples per frame
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100          # Sampling rate
TARGET_RMS = 0.1      # Target volume level for AGC
P_GAIN = 0.05         # Proportional gain for PID
I_GAIN = 0.01         # Integral gain for PID

# --- PID STATE ---
current_gain = 1.0
integral_error = 0.0

# --- PYAUDIO SETUP ---
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# --- MATPLOTLIB SETUP ---
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, CHUNK)
ax.axis('off')

# Initialize the line segments for rainbow effect
x = np.arange(CHUNK)
y = np.zeros(CHUNK)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Create color map
norm = plt.Normalize(0, CHUNK)
lc = LineCollection(segments, cmap='gist_rainbow', norm=norm, linewidth=2)
ax.add_collection(lc)

def signal_handler(sig, frame):
    print("\nCerrando proceso de forma segura...")
    try:
        stream.stop_stream()
        stream.close()
        p.terminate()
    except:
        pass
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def update(frame):
    global current_gain, integral_error
    
    try:
        # Read audio data
        data = stream.read(CHUNK, exception_on_overflow=False)
        y_data = np.frombuffer(data, dtype=np.int16) / 32768.0  # Normalize to [-1, 1]
        
        # Calculate RMS for Gain Control
        rms = np.sqrt(np.mean(y_data**2))
        if rms < 0.001: rms = 0.001 
        
        # Simple AGC
        target_gain = TARGET_RMS / rms
        current_gain = 0.9 * current_gain + 0.1 * target_gain
        current_gain = np.clip(current_gain, 0.1, 50.0)
        
        processed_y = y_data * current_gain
        
        # Update segments for the rainbow line
        new_points = np.array([x, processed_y]).T.reshape(-1, 1, 2)
        new_segments = np.concatenate([new_points[:-1], new_points[1:]], axis=1)
        
        lc.set_segments(new_segments)
        
        # Shift colors
        shift = (time.time() * 100) % CHUNK
        lc.set_array(np.roll(np.arange(CHUNK), int(shift))[:-1])
        
    except Exception as e:
        pass
        
    return lc,

ani = FuncAnimation(fig, update, interval=20, blit=True, save_count=100)

print("Iniciando visualización reactiva... (Cierra la ventana para salir)")
plt.show()
