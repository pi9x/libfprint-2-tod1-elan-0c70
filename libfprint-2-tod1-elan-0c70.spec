%global debug_package %{nil}
%global udevrulesdir /usr/lib/udev/rules.d

Name:           libfprint-2-tod1-elan-0c70
Version:        0.1.0
Release:        1%{?dist}
Summary:        Repackaged Elan TOD driver for 04f3:0c70 fingerprint reader

License:        GPL-3.0
URL:            https://support.lenovo.com/us/en/downloads/ds560935-elan-fingerprint-driver-for-linux-thinkpad-e14-gen-4-thinkpad-e15-gen-4
Source0:        %{name}-%{version}.tar.gz

ExclusiveArch:  x86_64
Requires:       libfprint-tod
Requires(post): systemd-udev
Requires(postun): systemd-udev
Conflicts:      libfprint-2-tod1-elan-0c4b

%description
Repackaged Elan TOD driver module patched for the 04f3:0c70 fingerprint reader.
The binary was modified from the 04f3:0c4b package by changing byte 0x4b to 0x70 at file offset 218672.

%prep
%autosetup

%install
install -p -d -m 0755 %{buildroot}%{_libdir}/libfprint-2/tod-1
install -p -d -m 0755 %{buildroot}%{_libdir}
install -p -d -m 0755 %{buildroot}%{udevrulesdir}

install -m 0755 usr/lib64/libfprint-2/tod-1/libfprint-2-tod1-elan.so \
  %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod1-elan.so

install -m 0755 usr/lib64/libcrypto.so.1.1 \
  %{buildroot}%{_libdir}/libcrypto.so.1.1

install -m 0644 usr/lib/udev/rules.d/60-libfprint-2-tod1-elan.rules \
  %{buildroot}%{udevrulesdir}/60-libfprint-2-tod1-elan.rules

%post
udevadm control --reload-rules || :

%postun
udevadm control --reload-rules || :

%files
%{_libdir}/libfprint-2/tod-1/libfprint-2-tod1-elan.so
%{_libdir}/libcrypto.so.1.1
%{udevrulesdir}/60-libfprint-2-tod1-elan.rules

%changelog
* Mon May 04 2026 Nguyen Hai Dang <hi@haidang.dev> - 0.1.0-1
- Add repackaged Elan TOD plugin variant for 04f3:0c70
