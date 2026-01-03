# MODUPAD
<img width="1920" height="1080" alt="ModuPad_FullProduct_Image" src="https://github.com/user-attachments/assets/18347e8f-02f0-41bc-9357-31d783e794c6" />

**MODUPAD** is a compact **3×3 programmable macropad with a rotary encoder** designed with a **macro‑first, learning‑driven philosophy**.  

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

All hardware choices prioritize **documentation availability, beginner accessibility, and reliability**.

---
| Schematic | PCB | Case |
|-----------|-----|------|
| <img src="https://github.com/user-attachments/assets/f3e017b2-80b7-48d1-9e30-7a34b8d917aa" alt="KiCad Schematic" width="600"> | <img src="https://github.com/user-attachments/assets/1682921c-09cf-4254-99f6-64b99035cbf7" alt="KiCad PCB" width="600"> | <img src="https://github.com/user-attachments/assets/2018dd81-1d8e-40cc-a252-7573122f007c" alt="Case Screenshot" width="600"> |





## License

This project is open‑source and intended for **educational and personal use**.  
License details will be added as the project evolves.
