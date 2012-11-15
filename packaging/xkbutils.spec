Name:           xkbutils
Version:        1.0.3
Release:        0
License:        MIT
Summary:        Collection of small utilities utilizing the X11 XKeyboard extension
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)

%description
xkbutils is a collection of small utilities utilizing the XKeyboard
(XKB) extension to the X11 protocol.

It includes:
 xkbbell  - generate XKB bell events
 xkbvleds - display the state of LEDs on an XKB keyboard in a window
 xkbwatch - reports changes in the XKB keyboard state

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/xkbbell
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch

%changelog
