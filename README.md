# 🎮 Tres en Raya - Python con IA

&lt;p align="center"&gt;
  &lt;img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"&gt;
  &lt;img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"&gt;
  &lt;img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"&gt;
&lt;/p&gt;

&lt;p align="center"&gt;
  &lt;b&gt;Juego clásico de Tres en Raya (Tic-Tac-Toe) con Inteligencia Artificial en Python&lt;/b&gt;&lt;br&gt;
  🧠 IA Estratégica | 👤 1 Jugador vs 🤖 PC | ⚡ Sin dependencias externas
&lt;/p&gt;

---

## 📸 Vista Previa

| Menú Principal | Partida en Curso | Victoria |
|:---:|:---:|:---:|
| ![Menú](screenshots/menu.png) | ![Juego](screenshots/juego.png) | ![Victoria](screenshots/victoria.png) |

*(Añade tus capturas de pantalla en la carpeta `/screenshots` o reemplaza las URLs)*

## ✨ Características

- 🎯 **IA Inteligente**: La computadora no juega al azar, usa estrategias ofensivas y defensivas
- 👤 **Personalización**: Elige tu nombre y símbolo (X o O)
- 🏆 **Detección automática**: Identifica ganadores y empates al instante  
- 🎨 **Interfaz limpia**: Diseño visual en terminal con emojis y colores
- ⚡ **Rápido**: Sin dependencias externas, solo Python puro
- 🔄 **Rejugable**: Sistema de revancha integrado

## 🧠 Algoritmo de la IA

La inteligencia artificial utiliza un sistema de **prioridades heurísticas**:

1. 🥇 **Ganar**: Si puede ganar en el siguiente movimiento, lo hace
2. 🛡️ **Bloquear**: Si el jugador va a ganar, lo bloquea  
3. 🎯 **Centro**: Prioriza ocupar la casilla central (mejor posición estratégica)
4. 🏗️ **Esquinas**: Toma esquinas disponibles para crear bifurcaciones
5. 🎲 **Aleatorio**: Cualquier casilla libre si no hay opciones estratégicas

## 🚀 Instalación y Uso

### Requisitos
- [Python 3.8+](https://www.python.org/downloads/)

### Librerías Utilizadas

| Librería | Documentación Oficial | Uso en el proyecto |
|----------|----------------------|-------------------|
| **random** | [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html) | Selección aleatoria de esquinas cuando no hay jugada óptima |
| **time** | [docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html) | Pausa dramática (`time.sleep`) para simular "pensamiento" de la IA |

*Nota: Ambas son librerías built-in de Python. No requieren instalación con pip.*

### Clonar y Ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/tres-en-raya-python.git

# Entrar al directorio
cd tres-en-raya-python

# Ejecutar el juego
python tres_en_raya.py
