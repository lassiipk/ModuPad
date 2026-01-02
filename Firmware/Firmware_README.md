# ModuPad – Firmware Documentation

**Author:** M. Saim Ghazanfar  
**Project:** ModuPad  
**Scope:** Firmware only (KMK-based)

---

## Overview

This document describes the **final firmware design** for the ModuPad project.  
Everything written here is based **strictly on real discussion, iteration, approvals, and decisions** made during the ModuPad firmware design process.

No assumptions.  
No features added afterward.  
No undocumented behavior.

This README is intended for:
- GitHub documentation
- Hack Club project submission
- Future maintenance and expansion
- Learning & documentation purpose

---

## Firmware Goals (Initial Plan)

The original firmware goals were:

- Use **KMK Firmware** (Python-based)
- Avoid VIA to keep things simple and controlled
- Support:
  - 3×3 macro keypad
  - Rotary encoder (rotation + button)
  - OLED display (128×32)
- Work on **Windows 10 and Windows 11**
- Be usable and testable **even before hardware arrives**
- Keep macros **OS-level and reliable**

---

## Key Design Changes & Decisions

### Removed Features
- Addressable LEDs  
  **Reason:**  
  - Took too much PCB space  
  - Increased schematic and firmware complexity  
  - Interfered with encoder placement  

### Changed Approach
- **Discord-specific mute removed**  
  Replaced with **Global Mic Mute**, which works system-wide.

- **Key-combo-heavy macros reduced**  
  Replaced with **Windows `.bat` scripts** for:
  - Stability
  - OS-wide behavior
  - Easy customization without firmware edits

---

## Firmware Stack

- **Firmware:** KMK (Python)
- **Architecture Style:** Modular
- **OS Target:** Windows 10 & Windows 11
- **OLED Resolution:** 128×32
- **Encoder:** Single EC11-style rotary encoder

---

## OLED Animation System

### Animation Files
- Each `animation_xx.py` file represents:
  - **One complete animation**
  - **Not individual frames**
> Example:
>
> OLED_ANIMATIONS/  
> ├── animation_01.py  
> ├── animation_02.py  
> ├── animation_03.py  
> └── animation_04.py

---

### Behavior
- Firmware automatically:
- Detects all animation files
- Loads them dynamically
- Cycles through them using the encoder button
- **No hard limit** on number of animations
- Users can:
- Add or remove animation files
- Without changing firmware logic

---

## Encoder Behavior (Final)

### Rotation
- Controls **system volume only**
- Small step size:
- **2 volume steps per tick**
- Works on:
- Windows 10
- Windows 11

### Encoder Button
| Action | Result |
|------|------|
| Press | Switch OLED animation |
| Fn + Press | Switch OLED text / status mode |
| Fn + Hold (3 seconds) | OLED OFF / ON toggle |

- OLED OFF state is **fully blank**
- No dimming or partial display

---

## Key Layout & Functions

### Physical Layout
- **3×3 matrix**
- Numbered **bottom-left → top-right**

> 7 8 9
>
> 4 5 6
>
> 1 2 3

---

### Layer 0 – Default

| Key | Function |
|---|---|
| 1 | Fn (momentary layer switch) |
| 2 | Screenshot (Win + Fn + Print) |
| 3 | Redo (Ctrl + Shift + Z) |
| 4 | Copy (Ctrl + C) |
| 5 | Paste (Ctrl + V) |
| 6 | Undo (Ctrl + Z) |
| 7 | Open Photoshop (`App1.exe`) |
| 8 | Open Browser |
| 9 | Open File Explorer |

---

### Layer 1 – Fn Held

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

### Key Layout & Functions — Layer 2 (Future Planned Feature)

> **Status:** Planning stage only  
> **Not implemented in current firmware**

### Layer Activation Logic (Proposed)
- **Trigger:** Press the **Fn key 5 times consecutively** (within a short time window).
- **Result:** Activates **Layer 2** (third layer, after Layer 0 and Layer 1).
- **Exit:** Press the **Fn key 5 times consecutively again** to return to **Layer 0 (Default)**.
- This design avoids adding extra physical keys and keeps the hardware simple.

### Intended Purpose of Layer 2
- Reserved for **advanced / power-user macros**.
- Experimental features without disturbing daily-use layers.
- Future expansion space for:
  - App-specific macro sets
  - Debug / development shortcuts
  - OLED debug or diagnostic modes
  - User-customizable workflows

### Design Notes
- Layer 2 is **deliberately not finalized**.
- Key assignments will be defined only after real-world usage of Layer 0 and Layer 1.
- Firmware architecture is designed to allow adding this layer **without breaking existing behavior**.

### Rationale
- Prevents accidental activation.
- Keeps Layer 0 and Layer 1 clean and predictable.
- Provides long-term scalability for ModuPad without hardware redesign.

---

## Windows `.bat` Script Philosophy

### Why `.bat` Files?
- More reliable than key combos
- Work regardless of focused application
- OS-wide behavior
- Easy to edit or replace

### Folder Structure Used by Firmware

> ModuPad/
> ├── Apps_Macros/
> │   ├── App1.exe
> │   └── Game.exe
> │
> ├── Windows_BootOptions/
> │   ├── sleep.bat
> │   ├── restart.bat
> │   └── shutdown.bat
> │
> ├── Utilitits/
> │   ├── Volume_toggle.bat
> │   └── mic_toggle.bat
> │
> ├── OLED_ANIMATIONS/
> │   ├── animation_01.py
> │   ├── animation_02.py
> │   └── animation_03.py
> │
> └── README.md

- Users can replace `.exe` or `.bat` files without touching firmware.

---

## Firmware Architecture Summary

The firmware is written entirely in Python using KMK and is split conceptually into:

- Key matrix handling
- Encoder handling
- OLED manager
- Animation loader
- Macro execution system

The firmware is designed so that:
- It can be written and reviewed **without hardware**
- Behavior is deterministic
- Features are easy to extend later

---

## What Was Learned

- Simplifying early saves time later
- Hardware constraints should guide firmware decisions
- OS-level automation is more reliable than app-specific shortcuts
- OLED usability matters more than flashy visuals
- KMK is powerful even without VIA
- Clear documentation prevents future confusion

---

## Final Notes

This firmware is:

- Purpose-built
- Minimal
- Reliable
- Easy to expand
- Fully aligned with the ModuPad hardware

All firmware decisions documented here are based **entirely on real design discussion and iteration**, not assumptions.

---

**ModuPad Project – Firmware**  
**Author:** Muhammad Saim Ghazanfar


