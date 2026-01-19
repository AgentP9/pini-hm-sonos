# HomeMatic Sonos Player Addon

![Version](https://img.shields.io/badge/version-3.0.7-blue.svg)
![License](https://img.shields.io/badge/license-GPL-green.svg)

A HomeMatic CCU addon for controlling Sonos audio players directly from your smart home system. This addon enables seamless integration between HomeMatic CCU devices and Sonos speakers, allowing you to control playback, volume, and more through the WebUI interface.

## Features

- **Sonos Device Discovery**: Automatic discovery of Sonos players on your network
- **Playback Control**: Play, pause, stop, next/previous track
- **Volume Management**: Control volume with race condition protection for smooth operation
- **Group Management**: Control Sonos groups and zones
- **WebUI Integration**: Easy-to-use web interface for configuration and control
- **Multiple Platform Support**: Works across all HomeMatic CCU platforms

## Supported CCU Models

* [HomeMatic CCU3](https://www.eq-3.de/produkte/homematic/zentralen-und-gateways/smart-home-zentrale-ccu3.html)
* [RaspberryMatic](http://raspberrymatic.de/)
* [HomeMatic CCU2](https://www.eq-3.de/produkt-detail-zentralen-und-gateways/items/homematic-zentrale-ccu-2.html)
* HomeMatic CCU1

## Installation

1. Download the latest addon release from the [releases page](https://github.com/AgentP9/pini-hm-sonos/releases)
2. Log in to your HomeMatic WebUI
3. Navigate to System Settings → Control Panel → Additional Software
4. Click "Install" and upload the downloaded `.tar.gz` file
5. After installation, configure the Sonos Player Addon through the WebUI

## Configuration

1. After installation, navigate to the Sonos Player Addon settings
2. The addon will automatically discover Sonos players on your network
3. Configure player names and preferences as needed
4. Save your configuration

## Development

### Building from Source

The addon uses a Makefile-based build system with platform-specific builds:

```bash
# Build for all platforms
make

# Build for specific platform
make ccu3    # For CCU3/RaspberryMatic
make ccu2    # For CCU2
make ccu1    # For CCU1
```

### Project Structure

- `src/newudp/` - UDP discovery tool for finding Sonos devices
- `sonos2/` - Main addon scripts and configuration
- `www/` - Web interface and CGI scripts
- `rc.d/` - Init scripts for addon startup

## Support

- **Issues**: For bug reports and feature requests, please create an issue in the [issue tracker](https://github.com/AgentP9/pini-hm-sonos/issues)
- **Forum**: Join the German-speaking discussion at [HomeMatic Forum](http://homematic-forum.de/forum/viewtopic.php?f=41&t=26531)

## Technical Documentation

- [Volume Lock Implementation](VOLUME_LOCK_IMPLEMENTATION.md) - Details on the race condition prevention mechanism

## License

This project is licensed under the GPL License. See the LICENSE file for details.

## Authors

* **fiveyears** - Main developer
* **Jens Maus** - Build environment and CCU1/RaspberryMatic ports
* **AgentP9** - Current maintainer

## Acknowledgments

Special thanks to the HomeMatic community and Sonos for their excellent products that make this integration possible.
