# MODUPAD

**MODUPAD** is a compact **3×3 programmable macropad with a rotary encoder** designed with a **macro‑first, learning‑driven philosophy**.  
Rather than copying a numpad or keyboard block, every key and interaction is intentionally designed around **custom macros, system actions, and workflow automation**.

This project represents a **from‑scratch learning journey** covering electronics, schematic design, PCB layout, firmware architecture, and documentation—while still resulting in a practical, daily‑use device.

---

## Device Identity

> **MODUPAD** is a **3×3 macropad + rotary encoder** with layered keymaps, encoder‑driven system control, and an event‑based OLED interface.

The identity of MODUPAD evolved during development and directly reflects lessons learned, simplifications made, and constraints discovered during real design work.

---

## Project Goals

- Learn electronics **from near zero** through hands‑on design
- Design a complete keyboard matrix with diodes
- Integrate a microcontroller, rotary encoder, and OLED display
- Build a full PCB in KiCad (schematic → layout → DRC‑clean)
- Design firmware architecture before hardware arrival
- Practice clean documentation and GitHub‑based version control
- Produce a focused, usable macropad without feature creep

This project prioritizes **learning clarity, reasoning, and correctness** over visual complexity.

---

## Final Key Features (As Built)

- **3×3 key matrix (9 keys)** dedicated entirely to macros
- **Multiple firmware layers**
  - Layer 0 (Default)
  - Layer 1 (Fn layer)
  - Layer 2 (planned / future)
- **EC11 rotary encoder**
  - Rotation: system volume control
  - Button: OLED mode control
- **0.91” 128×32 I²C OLED**
  - Animation mode
  - Text mode
  - Status mode
  - Full OFF state
- **USB‑C connectivity**
- **Windows‑focused macro design** (Windows 10 & 11)
- **No RGB lighting** (removed during redesign to reduce complexity)

---

## What Changed (And Why)

### ❌ Removed Features
- **RGB LEDs**
  - Caused routing complexity
  - Conflicted with encoder placement
  - Added firmware overhead
  - Reduced learning clarity

### ❌ Removed VIA Support
- Added unnecessary abstraction
- KMK firmware was sufficient and clearer
- Manual firmware control improved understanding

### ✅ Adopted Instead
- Simpler, more reliable firmware logic
- OS‑level automation via `.bat` files
- OLED behavior focused on usability, not decoration

These changes significantly improved **learning efficiency and project completion speed**.

---

## Hardware Overview (Final)

- **Microcontroller:** Seeed Studio XIAO RP2040
- **Keys:** 9 × MX‑style switches
- **Diodes:** 1N4148 (matrix isolation)
- **Encoder:** EC11 rotary encoder with push button
- **Display:** 0.91” I²C OLED (128×32)
- **Connectivity:** USB‑C
- **Case:** Custom‑designed in Fusion 360, 3D‑printed

All hardware choices prioritize **documentation availability, beginner accessibility, and reliability**.

---

## Firmware Overview (Final)

- **Firmware Framework:** KMK (Python‑based)
- **Reason for KMK**
  - Python readability
  - Clear firmware structure
  - No dependency on VIA
  - Easier reasoning without hardware in hand

Firmware was designed **before physical assembly**, allowing logic review and iteration in advance.

---

## Encoder Behavior (Final)

### Encoder Rotation
- Controls **system volume only**
- Small step size for precision
- Works across **Windows 10 & 11**

### Encoder Button
- **Press:** Cycle OLED animations
- **Fn + Press:** Cycle text/status modes
- **Fn + Hold (3s):** OLED ON / OFF toggle

---

## OLED System (Final)

### OLED Modes
1. **Animation Mode**
   - Plays one full animation per `animation_xx.py`
   - Firmware auto‑detects all animation files
   - No hard limit on number of animations
2. **Text Mode**
   - Displays:
     - Creator name
     - Date & time
3. **Status Mode**
   - Displays system states (e.g. mute status)
4. **OFF Mode**
   - OLED fully powered down (true blank state)

OLED behavior is **event‑driven**, not continuously animated.

---

## Key Layout & Functions

### Physical Layout
Keys are numbered **bottom‑left → top‑right**.

### Layer 0 — Default

| Key | Function |
|---|---|
| 1 | Fn (momentary) |
| 2 | Screenshot (Win + Fn + Print) |
| 3 | Redo (Ctrl + Shift + Z) |
| 4 | Copy (Ctrl + C) |
| 5 | Paste (Ctrl + V) |
| 6 | Undo (Ctrl + Z) |
| 7 | Open Photoshop (`App1.exe`) |
| 8 | Open Browser |
| 9 | Open File Explorer |

---

### Layer 1 — Fn Held

| Key | Function |
|---|---|
| 1 | --- |
| 2 | Global Mic Mute / Unmute |
| 3 | Window Switch (Alt + Tab) |
| 4 | Task Manager (Ctrl + Shift + Esc) |
| 5 | Toggle Speaker Mute |
| 6 | Open Game (`Game.exe`) |
| 7 | Windows Sleep |
| 8 | Windows Restart |
| 9 | Windows Shutdown |

---

### Layer 2 — *Planned (Future)*

> **Not implemented in current firmware**

- Activated by pressing **Fn five times rapidly**
- Pressing Fn five times again returns to Layer 0
- Intended for advanced or experimental macros
- Included as a **future expansion concept**, not finalized behavior

---

## Windows Macro Strategy

Instead of complex key combinations, MODUPAD uses **Windows `.bat` files** for critical system actions:

### Why `.bat` Files?
- OS‑wide reliability
- No dependency on active application
- User‑editable without firmware changes
- Clear separation between hardware and OS logic

### Directory Structure

> ModuPad/
> ├── Apps_Macros/
> ├── Windows_BootOptions/
> ├── Utilities/
> ├── OLED_ANIMATIONS/
> └── README.md

---

## Development Status (Current)

- [x] Concept defined
- [x] Schematic completed
- [x] PCB layout completed
- [x] DRC‑clean board
- [x] Case designed
- [x] Firmware architecture finalized
- [x] Firmware written
- [x] Project uploaded to GitHub
- [ ] Hardware fabrication & assembly
- [ ] Flashing & physical testing

---

## What This Project Is Not

MODUPAD intentionally avoids:
- RGB lighting
- Wireless connectivity
- VIA configuration
- Host‑side companion apps
- Feature‑driven design without learning value

---

## What Was Learned

- Simplification accelerates learning
- Firmware clarity matters more than features
- OS‑level automation is more reliable than app‑specific shortcuts
- Hardware constraints should guide firmware decisions
- Documentation is part of engineering, not an afterthought

---

## Why MODUPAD?

**MODUPAD** stands for:
- **MODU** — Modular, adaptable, intentional
- **PAD** — A focused input device

Every decision made in this project supports **clarity, control, and learning**.

---
## BOM:
- **Microcontroller:** Seeed Studio XIAO RP2040
- **Keys:** 9 × MX‑style switches
- **Diodes:** 10 1N4148 Diodes (matrix isolation)
- **Encoder:** EC11 rotary encoder with push button
- **Display:** 0.91” I²C OLED (128×32)
- **Connectivity:** USB‑C
- **Case:** Custom‑designed in Fusion 360, 3D‑printed

---
| Schematic | PCB | Case |
|---|---|
| <img width="1818" height="879" alt="01_KiCad_Schematic" src="https://github.com/user-attachments/assets/f3e017b2-80b7-48d1-9e30-7a34b8d917aa" /> | <img width="1920" height="1080" alt="02_KiCad_PCB" src="https://github.com/user-attachments/assets/1682921c-09cf-4254-99f6-64b99035cbf7" /> | <img width="1920" height="906" alt="Screenshot 2026-01-02 214436" src="https://github.com/user-attachments/assets/2018dd81-1d8e-40cc-a252-7573122f007c" /> |




## License

This project is open‑source and intended for **educational and personal use**.  
License details will be added as the project evolves.
