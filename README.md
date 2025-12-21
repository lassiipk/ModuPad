# MODUPAD

**MODUPAD** is a compact **4×4 programmable macropad** designed with a macro-first philosophy.  
Instead of replicating a traditional numpad, every key is intentionally reserved for **custom macros, shortcuts, and system actions**, making the device highly modular, adaptable, and workflow-focused.

This project is built as a **beginner-friendly, from-scratch hardware project** for learning electronics, PCB design, firmware planning, and documentation—while still resulting in a practical daily-use device.

---

## Device Identity

> **MODUPAD** is a 4×4 programmable macropad with layered functionality, encoder-driven mode control, per-key RGB feedback, and an event-driven OLED user interface.

This identity defines the project’s scope and design decisions.

---

## Project Goals

- Design and build a custom macropad from scratch
- Learn keyboard matrix design, diodes, and microcontroller integration
- Integrate a rotary encoder, OLED display, and RGB lighting
- Practice clean documentation and version control using GitHub
- Create a modular input device usable across different workflows

This project prioritizes **learning, clarity, and intentional design** over feature bloat.

---

## Key Features

- **4×4 key grid (16 keys)** dedicated entirely to macros
- **1–2 programmable layers** for flexible workflows
- **Rotary encoder** for mode switching and interaction
- **OLED display** for status, modes, and visual feedback
- **Per-key RGB lighting** using addressable LEDs
- **USB-C connectivity**
- Cross-platform target support (Windows, Linux, macOS)

---

## Layer Design (High Level)

- **Primary Layer**  
  The default macro layer, intended for the most frequently used actions.

- **Secondary Layer (Optional)**  
  Accessed via a hold or mode mechanism, providing extended functionality without adding more physical keys.

> Specific key assignments are intentionally left undefined at this stage to preserve modularity and allow iteration.

---

## Encoder & Interaction Model

- **Rotary Encoder**
  - Used to switch modes or interact with the device dynamically
  - Encoder press is used to cycle or access OLED display modes

- **OLED Access**
  - OLED operates in an **event-driven** manner
  - Information and animations are triggered by interactions (e.g., layer change, encoder input)
  - No continuous or always-on animations

- **RGB Control**
  - Per-key RGB lighting provides visual context
  - RGB modes and behavior are controlled through a secondary encoder interaction
  - RGB is used as functional feedback, not decorative lighting

---

## Display (OLED)

The OLED display is used to provide meaningful feedback without unnecessary complexity:

- Active layer indication
- Encoder mode/status
- System indicators (e.g., lock states)
- Event-based animations
- Minimal idle display to reduce distraction and power usage

CPU or host-side metrics are intentionally excluded to keep the firmware simple and standalone.

---

## Hardware Overview

- **Microcontroller:** RP2040-based controller (Seeed XIAO RP2040 or equivalent)
- **Keys:** 16 × MX-style switches
- **Encoder:** EC11 rotary encoder
- **Display:** 0.91" I²C OLED
- **Lighting:** SK6812 MINI-E addressable RGB LEDs
- **Case:** 3D-printed enclosure (no acrylic)
- **Connectivity:** USB-C

All hardware choices prioritize availability, documentation, and beginner accessibility.

---

## Firmware (Planned)

Firmware will be implemented using **QMK** due to:

- Open-source ecosystem
- Strong community support
- Native support for:
  - Layered keymaps
  - Rotary encoders
  - OLED displays
  - Addressable RGB LEDs

Firmware implementation is planned after hardware design and documentation are finalized.

---

## What This Project Is Not

To maintain focus and feasibility, MODUPAD intentionally avoids:

- Numeric keypad replication
- Wireless or Bluetooth support
- Host-side companion software
- Continuous OLED animations
- Feature creep beyond the defined scope

---

## Development Status

- [x] Project concept and scope defined
- [x] Feature set locked
- [ ] Keymap layout finalized
- [ ] PCB schematic
- [ ] PCB layout
- [ ] Case design
- [ ] Firmware implementation
- [ ] Assembly and testing

---

## Why MODUPAD?

The name **MODUPAD** reflects the core idea behind the project:

- **MODU** – Modular, adaptable, flexible  
- **PAD** – A compact input device built for intentional interaction

Every design choice supports modularity, clarity, and learning.

---

## License

This project is open-source and intended for educational and personal use.  
License details will be added as the project matures.
