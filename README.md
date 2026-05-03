# libfprint-2-tod1-elan-0c70

Fedora/COPR repack of the Elan TOD fingerprint driver for devices with USB ID
`04f3:0c70`.

This package is based on the Lenovo/Ubuntu Elan TOD driver package for
`04f3:0c4b`. The driver binary was tested locally on Fedora with
`libfprint-tod` and `fprintd`; after changing the plugin's USB ID table from
`0c4b` to `0c70`, `fprintd-enroll` detects and enrolls the sensor.

## Status

Tested working on:

- Fedora 44
- `fprintd-1.94.5`
- `libfprint-tod-1.94.9`
- USB device: `04f3:0c70 Elan Microelectronics Corp. ELAN:Fingerprint`

## What Changed

The packaged TOD plugin contains a compiled USB ID table. The original `libfprint-2-tod1-elan-0c4b` package registers:

- `04f3:0c42`
- `04f3:0c4b`

For this package, the `04f3:0c4b` entry is changed to `04f3:0c70`.

Binary patch:

```bash
printf '\x70' | dd of=libfprint-2-tod1-elan.so bs=1 seek=218672 count=1 conv=notrunc
```

The package also installs a matching udev rule:

```udev
SUBSYSTEM=="usb", ATTRS{idVendor}=="04f3", ATTRS{idProduct}=="0c70", ATTRS{dev}=="*", TEST=="power/control", ATTR{power/control}="auto", MODE="0660", TAG+="uaccess"
SUBSYSTEM=="usb", ATTRS{idVendor}=="04f3", ATTRS{idProduct}=="0c70", ENV{LIBFPRINT_DRIVER}="Elan Fingerprint Sensor"
```

## Files Installed

- `/usr/lib64/libfprint-2/tod-1/libfprint-2-tod1-elan.so`
- `/usr/lib64/libcrypto.so.1.1`
- `/usr/lib/udev/rules.d/60-libfprint-2-tod1-elan.rules`

## Build Locally

Install RPM build tools:

```bash
sudo dnf install rpm-build make
```

Build a source RPM:

```bash
make srpm
```

Build a binary RPM locally:

```bash
rpmbuild --rebuild libfprint-2-tod1-elan-0c70-*.src.rpm
```

Install the resulting package:

```bash
sudo dnf install ~/rpmbuild/RPMS/x86_64/libfprint-2-tod1-elan-0c70-*.rpm
sudo udevadm control --reload-rules
sudo udevadm trigger --attr-match=idVendor=04f3 --attr-match=idProduct=0c70
sudo systemctl restart fprintd
```

Test:

```bash
fprintd-list "$USER"
fprintd-enroll
```

## Uninstall

```bash
sudo dnf remove libfprint-2-tod1-elan-0c70
sudo systemctl restart fprintd
```
