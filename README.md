# HomeMatic Sonos Player Addon

This repository hosts the development of a HomeMatic CCU addon that enables your CCU to control Sonos audio players (www.sonos.com) directly from the WebUI user interface.

## Features

- **Full Sonos Control**: Play, pause, skip, volume control, and playlist management
- **Volume Lock Mechanism**: Prevents race conditions during rapid volume changes (e.g., when using HmIP-WRCR wheel controls)
- **Multi-Zone Support**: Control multiple Sonos players independently
- **WebUI Integration**: Seamless integration with HomeMatic's web interface
- **Stable Operation**: File-based locking ensures reliable concurrent operations

## Supported CCU Models

* [HomeMatic CCU3](https://www.eq-3.de/produkte/homematic/zentralen-und-gateways/smart-home-zentrale-ccu3.html) / [RaspberryMatic](http://raspberrymatic.de/)
* [HomeMatic CCU2](https://www.eq-3.de/produkt-detail-zentralen-und-gateways/items/homematic-zentrale-ccu-2.html)
* HomeMatic CCU1

## Installation

1. Download the latest addon release from [GitHub Releases](https://github.com/homematic-community/hm-sonos/releases)
2. In your HomeMatic WebUI, navigate to **Settings** → **Control Panel** → **Additional Software**
3. Click **Install** and upload the downloaded `.tar.gz` file
4. After installation, the CCU will reboot automatically
5. Configure your Sonos players in the addon settings

## Configuration

After installation, configure the addon through the WebUI:

1. Navigate to the **Sonos** section in your HomeMatic WebUI
2. Add your Sonos player IP addresses
3. Configure default volume settings
4. Set up message storage location for announcements

## Volume Lock Implementation

The addon includes a sophisticated file-based locking mechanism that prevents race conditions when multiple instances try to change the volume simultaneously (e.g., during rapid wheel rotations on HmIP-WRCR devices).

### How It Works

- **Per-player locking**: Each Sonos player has its own lock file, allowing concurrent control of different players
- **Lock location**: `/usr/local/etc/config/addons/www/sonos2/.locks/volume_{IP_ADDRESS}.lock`
- **Timeout**: 2 seconds with automatic retry
- **Stale lock cleanup**: Locks older than 10 seconds are automatically removed
- **Minimal overhead**: Adds only 10-50ms per volume operation

### What Problem Does It Solve?

Previously, rapid volume changes could result in lost updates because multiple CGI instances would:
1. Read the same current volume
2. Calculate new volume independently
3. Overwrite each other's changes

The lock mechanism ensures that volume operations are serialized per player, preventing any lost updates.

## Troubleshooting

### Check Logs
Log files are stored in the addon directory. Check `sonos.log` for operational messages and errors:
```bash
cat /usr/local/etc/config/addons/www/sonos2/sonos.log
```

### Volume Lock Issues
If you experience problems with volume changes, check for stale lock files:
```bash
ls -la /usr/local/etc/config/addons/www/sonos2/.locks/
```

Lock files are automatically cleaned up, but you can manually remove them if needed:
```bash
rm -f /usr/local/etc/config/addons/www/sonos2/.locks/volume_*.lock
```

### Compatibility
The addon is compatible with TCL 8.2+ and has been tested on:
- CCU1 (TCL 8.2)
- CCU2 (TCL 8.4)
- CCU3 (TCL 8.6)
- RaspberryMatic (various TCL versions)

## Support

If you encounter any problems or have ideas for enhancements, please:
- Create an issue at the [GitHub issue tracker](https://github.com/homematic-community/hm-sonos/issues)
- Join the German-speaking discussion forum: [HomeMatic Forum](http://homematic-forum.de/forum/viewtopic.php?f=41&t=26531)

## Development

### Building the Addon

To build the addon package, run:
```bash
./generate_img.sh
```

This creates `sonos2-addon-{VERSION}.tar.gz` in the repository root.

### Version Information

The current version is stored in the `VERSION` file and is automatically included in the build.

## Contributing

Contributions to this project are welcome! This repository is part of the HomeMatic community ecosystem. 

For bug reports, feature requests, and contributions, please visit the main community repository:
**[https://github.com/homematic-community/hm-sonos](https://github.com/homematic-community/hm-sonos)**

When contributing, please:
- Check existing issues and pull requests before creating new ones
- Follow the existing code style and conventions
- Test your changes on supported CCU platforms when possible
- Provide clear descriptions of changes and their purpose

## Technical Details

For detailed technical documentation about the volume lock implementation, see [VOLUME_LOCK_IMPLEMENTATION.md](VOLUME_LOCK_IMPLEMENTATION.md).

## License

The Sonos CCU Addon as published in this GitHub repository is provided under the GPL license.

## Authors

* **fiveyears**: Main developer of the addon
* **Jens Maus**: Build environment and ports to CCU1 and RaspberryMatic platform
* **Community contributors**: Various improvements and bug fixes
