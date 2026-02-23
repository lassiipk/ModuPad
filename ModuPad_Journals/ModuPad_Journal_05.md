**8 Feb 2026**

I continued testing the encoder to confirm everything was stable. After that, I moved on to implementing its intended function — controlling Windows volume.

I tried very hard but was unsuccessful.

After multiple failures, I shifted my focus to QMK-based firmware. Again, I faced difficulties. It was written in C, and everything felt very complicated. The reason I originally chose KMK over QMK was exactly this — QMK is very advanced and powerful, probably best suited for my ModuPad, but KMK is Python-based and easier to understand.

One big advantage of KMK was flashing. First, I installed CircuitPython onto the MCU. After that, the board appeared as a USB drive (CIRCUITPY / Seeed-XIAO-RP2040). Making changes was simple — I only had to modify `code.py` directly on the drive.

Despite that convenience, I struggled a lot with functionality. After many failed attempts, I quit for the day and went to sleep.

---

> Journal Entry Written: 11 Feb 2026 | 12:50 - AM

---

> The Image provided is of Compiling statusof  my OMK based Firmware.
>
> Ignore the mess around my Desk and LCD, its always like this!

![733baa89-5d99-4c6c-8100-c8d66cede92e](https://github.com/user-attachments/assets/f2cf72a5-fc7f-4448-8615-f8935c5b9e46)

---
