#!/bin/sh

# Check if VERSION file exists
if [ ! -f VERSION ]; then
    echo "ERROR: VERSION file not found"
    exit 1
fi

# Read version and validate it's not empty
VERSION=$(tr -d '\n\r' < VERSION)
if [ -z "$VERSION" ]; then
    echo "ERROR: VERSION file is empty"
    exit 1
fi

echo "Building sonos2-addon-${VERSION}.tar.gz"

tar=$(which gtar) # OSX gnu tar
if [ -z "$tar" ]; then
    tar="tar"
fi
mkdir -p tmp
cp -a sonos2 tmp/
cp -a rc.d tmp/
cp -a www tmp/
cp -a ccu1 tmp/
cp -a ccu2 tmp/
cp -a ccu3 tmp/
cp -a ccu3x86 tmp/
cp -a update_script tmp/
cp -a VERSION tmp/sonos2/
cd tmp

$tar --owner=root --group=root --exclude=.DS_Store -czvf ../sonos2-addon-${VERSION}.tar.gz *
cd ..
rm -rf tmp