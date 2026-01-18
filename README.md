# HomeMatic Sonos Player Addon

[![Version](https://img.shields.io/badge/version-3.0-blue.svg)](VERSION)
[![License](https://img.shields.io/badge/license-GPL-green.svg)](#license)

This repository hosts the development of a HomeMatic CCU addon that enables your CCU to control Sonos audio players ([www.sonos.com](https://www.sonos.com)) directly from the WebUI interface.

## Features

- 🎵 **Complete Sonos Control**: Control your Sonos speakers directly from HomeMatic WebUI
- 🔍 **Automatic Discovery**: Automatically discovers Sonos players on your network
- 🏠 **Multi-Room Support**: Manage multiple Sonos zones and rooms
- 🔄 **Real-time Status**: Live updates of playback status and zone information
- 📱 **Responsive UI**: Modern Bootstrap-based interface that works on all devices
- ⚙️ **Easy Configuration**: Simple setup and configuration through web interface

## Supported CCU Models

- ✅ [HomeMatic CCU3](https://www.eq-3.de/produkte/homematic/zentralen-und-gateways/smart-home-zentrale-ccu3.html)
- ✅ [RaspberryMatic](https://raspberrymatic.de/)
- ✅ [HomeMatic CCU2](https://www.eq-3.de/produkt-detail-zentralen-und-gateways/items/homematic-zentrale-ccu-2.html)
- ✅ HomeMatic CCU1

## Prerequisites

- HomeMatic CCU (CCU1, CCU2, CCU3, or RaspberryMatic)
- One or more Sonos speakers connected to the same network
- Network connectivity between CCU and Sonos devices

## Installation

1. **Download the Addon**
   - Navigate to the [Releases page](https://github.com/AgentP9/pini-hm-sonos/releases)
   - Download the latest `sonos2-addon-X.X.tar.gz` file

2. **Upload the Addon**
   - Log in to your HomeMatic CCU WebUI
   - Navigate to **Settings** → **Control Panel** → **Additional Software**
   - Click on **Install** and select the downloaded `.tar.gz` file
   - Wait for the installation to complete

3. **Configure the Addon**
   - After installation, the CCU will reboot automatically
   - Navigate to the Sonos addon in the WebUI
   - The system will automatically discover Sonos players on your network
   - Configure your preferred settings in the **Settings** menu

## Usage

After successful installation, you can:

- **View Status**: See all discovered Sonos players and their current status
- **Control Playback**: Play, pause, and control volume
- **Manage Zones**: Switch between different Sonos zones/rooms
- **Configure Settings**: Adjust network topology and addon settings

Access the addon through the HomeMatic WebUI by navigating to the Sonos menu item.

## Building from Source

To build the addon from source:

```bash
# Build the addon package
./generate_img.sh

# This will create: sonos2-addon-X.X.tar.gz
```

## Support

### Issue Tracker
If you encounter any problems or have ideas for enhancements, please:
- Create an issue at the [GitHub Issue Tracker](https://github.com/AgentP9/pini-hm-sonos/issues)
- Provide detailed information about your setup and the issue

### Community Support
For direct help and discussions (German language):
- Visit the [HomeMatic Forum Discussion Thread](http://homematic-forum.de/forum/viewtopic.php?f=41&t=26531)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the **GNU General Public License (GPL)**. See the LICENSE file for details.

The Sonos CCU Addon as published in this GitHub repository is provided under the GPL license, ensuring it remains free and open source.

## Authors

- **fiveyears** - Main developer of the addon
- **Jens Maus** - Build environment and ports to CCU1 and RaspberryMatic platform

## Changelog

### Version 3.0
- Current release with improved stability and features

For detailed version history, see the [Releases page](https://github.com/AgentP9/pini-hm-sonos/releases).

---

**Note**: Sonos is a registered trademark of Sonos, Inc. This project is not affiliated with or endorsed by Sonos, Inc.
