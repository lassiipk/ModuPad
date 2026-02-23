**8 Feb 2026**

I continued testing the encoder to confirm everything was stable. After that, I moved on to implementing its intended function — controlling Windows volume.

I tried very hard but was unsuccessful.

After multiple failures, I shifted my focus to QMK-based firmware. Again, I faced difficulties. It was written in C, and everything felt very complicated. The reason I originally chose KMK over QMK was exactly this — QMK is very advanced and powerful, probably best suited for my ModuPad, but KMK is Python-based and easier to understand.

One big advantage of KMK was flashing. First, I installed CircuitPython onto the MCU. After that, the board appeared as a USB drive (CIRCUITPY / Seeed-XIAO-RP2040). Making changes was simple — I only had to modify `code.py` directly on the drive.

Despite that convenience, I struggled a lot with functionality. After many failed attempts, I quit for the day and went to sleep.

---
