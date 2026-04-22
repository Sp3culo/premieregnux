<img src="icons/aegnux.png" width="128" />

# Premieregnux 

A convenient way to install Adobe Premiere Pro on Linux using Wine. A mod/port of [Aegnux](https://github.com/relativemodder/aegnux) by Relative.

**SOFTWARE IS NOT IN THE RELEASE STATE**

<div align="center">

### Premieregnux community

[![Reddit Badge](https://img.shields.io/badge/reddit-orange?style=for-the-badge&logoColor=%23ff4500&label=Aegnux%20Sub&link=https%3A%2F%2Fwww.reddit.com%2Fr%2FAegnux)](https://www.reddit.com/r/Aegnux/)
[![Telegram Badge](https://img.shields.io/badge/telegram-chat-blue?style=for-the-badge&label=Telegram&link=https%3A%2F%2Ft.me%2FAegnux)](https://t.me/Aegnux)

</div>

*Based on the amazing work of Relative. This project aims to bring the same simplicity to Premiere Pro users on GNU/Linux.*

## License disclaimer

**This project is licensed under GNU GENERAL PUBLIC LICENSE V3.**

This project is intended for educational and experimental use only. Please respect software licensing agreements and use responsibly. The primary objective is to explore Linux compatibility for creative applications. Adobe Premiere Pro is a commercial software developed by Adobe.

## Known downsides

- **Dynamic Link** - NOT DEVELOPED YET. Inter-app communication between Premiere and After Effects is currently not supported.
- **Hardware Acceleration** - Limited support, mostly stable on NVIDIA GPUs with NVENC.
- **Timeline Performance** - May vary depending on the video codecs used (ProRes/DNxHR recommended).
- **Audio Latency** - Occasional desync issues depending on the Wine/Pipewire configuration.
- **Media Encoder** - Integration is still experimental.

## How to install natively

Native installation: the primary tested environment is Arch Linux on KDE Plasma Wayland.

**Manual installation is currently recommended during early stages.**

## Manual installation

### Clone the repository
```bash
git clone https://github.com/Sp3culo/premieregnux
cd aegnux
```

### Download binaries for workarounds to work
```bash
./prepare.sh
```

### Run
```bash
./run.sh
```
