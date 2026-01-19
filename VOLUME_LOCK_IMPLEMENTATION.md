# Volume Lock Implementation

## Overview
This implementation adds a file-based locking mechanism to prevent race conditions when multiple sonos2.cgi instances execute concurrently during rapid volume changes (e.g., when quickly turning the HmIP-WRCR wheel).

## Problem Solved
Previously, when the wheel was turned rapidly, multiple CGI instances would:
1. Read the current volume
2. Calculate the new volume (current + increment)
3. Set the new volume

This caused a race condition where multiple instances could read the same volume before any of them updated it, resulting in lost volume changes.

## Solution
The implementation adds locking around the critical section of VolumeUp and VolumeDown operations:
- Lock acquisition before reading volume
- Read current volume
- Calculate new volume
- Set new volume
- Lock release

## Technical Details

### Lock Files
- **Location**: `/usr/local/etc/config/addons/www/sonos2/.locks/volume_{IP_ADDRESS}.lock`
- **Per-player locking**: Different Sonos players can be controlled concurrently
- **Timeout**: 2 seconds (reduced from 5 seconds for better responsiveness)
- **Stale lock detection**: Locks older than 10 seconds are automatically removed

### Lock Acquisition
The `acquireVolumeLock` function:
1. Creates a unique lock file per Sonos player IP in the addon's `.locks/` directory
2. Uses simple file creation with proper error handling
3. Retries with 100ms intervals until timeout
4. Returns 1 on success, 0 on timeout

### Lock Release
The `releaseVolumeLock` function:
- Deletes the lock file
- Uses catch to handle errors gracefully

### Error Handling
- Locks are always released, even if errors occur during volume operations
- If lock cannot be acquired within timeout, the operation is aborted and logged
- No operation proceeds without acquiring the lock first

## Recent Fixes (v2 - CCU3 Compatibility)

### Issue 1: Permission Problems on CCU3
**Problem**: Lock files in `/tmp` may have permission restrictions on CCU3 systems.

**Solution**: Changed lock file location to the addon's own directory:
- Old: `/tmp/sonos2_volume_{IP}.lock`
- New: `/usr/local/etc/config/addons/www/sonos2/.locks/volume_{IP}.lock`

### Issue 2: TCL Catch Block Bug
**Problem**: Using `return` inside a catch block caused the catch to report an error (return code 1), making lock acquisition always fail.

**Solution**: Changed to use a flag variable:
```tcl
# Old (broken):
if {[catch {
  set fd [open $lockfile w]
  ...
  return 1  # This causes catch to return 1 (error)
}]} { ... }

# New (fixed):
set created 0
if {[catch {
  set fd [open $lockfile w]
  ...
  set created 1
}] == 0 && $created} {
  return 1
}
```

### Issue 3: Compatibility and Performance
**Changes**:
- Switched from `clock clicks -milliseconds` to `clock seconds` for better TCL 8.2 compatibility
- Reduced timeout from 5 seconds to 2 seconds for better responsiveness
- Increased retry interval from 50ms to 100ms to reduce CPU usage

## Functions Added

### `acquireVolumeLock {array timeout}`
Acquires an exclusive lock for volume operations.
- **Parameters:**
  - `array`: Sonos array (default: "sonosArray")
  - `timeout`: Timeout in milliseconds (default: 5000)
- **Returns:** 1 if lock acquired, 0 on timeout

### `releaseVolumeLock {array}`
Releases the volume lock.
- **Parameters:**
  - `array`: Sonos array (default: "sonosArray")

### `executeVolumeChangeWithLock {operation array}`
Helper function that executes volume operations with lock protection.
- **Parameters:**
  - `operation`: "Up" or "Down"
  - `array`: Sonos array (default: "sonosArray")

## Functions Modified

### `VolumeUp {array}`
Now uses locking via `executeVolumeChangeWithLock`

### `VolumeDown {array}`
Now uses locking via `executeVolumeChangeWithLock`

## Testing
A comprehensive test suite was created to verify:
1. Basic lock acquire/release operations
2. Sequential locking behavior
3. VolumeUp with locking
4. VolumeDown with locking
5. Simulated concurrent access

All tests passed successfully.

## Compatibility
- Compatible with TCL 8.2+ (CCU1, CCU2, CCU3, RaspberryMatic)
- Uses EXCL flag for atomic file creation on TCL 8.3+
- Falls back to mtime-based verification on older versions

## Performance Impact
- Minimal: Lock operations add approximately 10-50ms overhead per volume change
- Only affects VolumeUp and VolumeDown operations
- No impact on other Sonos operations

## Monitoring
Lock failures are logged to `sonos.log` with format:
```
[timestamp]: Up volume operation: Failed to acquire lock for [IP], operation aborted
```

## Maintenance
Lock files are automatically cleaned up:
- On successful operation completion
- On error during operation (via catch)
- Via stale lock detection (locks older than 10 seconds)

Manual cleanup if needed:
```bash
rm -f /tmp/sonos2_volume_*.lock
```
