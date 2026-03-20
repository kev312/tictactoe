
# 🎮 Tres en Raya - Python con IA

&lt;p align="center"&gt;
  &lt;img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"&gt;
  &lt;img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"&gt;
&lt;/p&gt;

&lt;p align="center"&gt;
  &lt;b&gt;Juego clásico de Tres en Raya (Tic-Tac-Toe) con Inteligencia Artificial en Python&lt;/b&gt;&lt;br&gt;
  🧠 IA Estratégica | 👤 1 Jugador vs 🤖 PC | ⚡ Sin dependencias externas
&lt;/p&gt;

---

## 📸 Vista Previa

**Menú Principal:**
  
| Menú Principal | Partida en Curso | Victoria |
|:---:|:---:|:---:|
| &lt;img src="https://i.imgur.com/placeholder1.png" width="250" alt="Menú"&gt; | &lt;img src="https://i.imgur.com/placeholder2.png" width="250" alt="Juego"&gt; | &lt;img src="https://i.imgur.com/placeholder3.png" alt="Victoria"&gt; |

&lt;/div&gt;

##  Características

- 🎯 **IA Inteligente**: La computadora no juega al azar, usa estrategias ofensivas y defensivas
- 👤 **Personalización**: Elige tu nombre y símbolo (X o O)
- 🏆 **Detección automática**: Identifica ganadores y empates al instante  
- 🎨 **Interfaz limpia**: Diseño visual en terminal con emojis y colores
- ⚡ **Rápido**: Sin dependencias externas, solo Python puro
- 🔄 **Rejugable**: Sistema de revancha integrado

1. 🥇 **Ganar**: Si puede ganar en el siguiente movimiento, lo hace
2. 🛡️ **Bloquear**: Si el jugador va a ganar, lo bloquea  
3. 🎯 **Centro**: Prioriza ocupar la casilla central (mejor posición estratégica)
4. 🏗️ **Esquinas**: Toma esquinas disponibles para crear bifurcaciones
5. 🎲 **Aleatorio**: Cualquier casilla libre si no hay opciones estratégicas

## 🚀 Instalación y Uso

### Requisitos
- [Python 3.8+](https://www.python.org/downloads/) (Librerías utilizadas: [`random`](https://docs.python.org/3/library/random.html), [`time`](https://docs.python.org/3/library/time.html))

*Nota: Todas las librerías son built-in, no necesitas instalar nada extra*

### Clonar y Ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/tres-en-raya-python.git

# Entrar al directorio
cd tres-en-raya-python

# Ejecutar el juego
python tres_en_raya.py
