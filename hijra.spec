%global owner ojuba-org
%global commit #Write commit number here

Name:		hijra
Summary:	Hijri Islamic Calendar utils in python
URL:		http://ojuba.org
Version:	0.3.2
Release:	1%{?dist}
Source0:	https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
License:	WAQFv2
Group:		System Environment/Base
BuildArch:	noarch
Requires:	python
Requires:	pygobject3 >= 3.0.2
BuildRequires:	gettext
BuildRequires:	python2-devel
BuildRequires:	python-setuptools


%description
Hijra provides Hijri/Islamic Calendar routines and utils in python

%package -n hijri
Group:		System Environment/Base
Summary:	Hijri Terminal
BuildArch:	noarch

%description -n hijri
Hijri now very easy in Terminal by this tool.

%package -n python-hijra
Group:		System Environment/Base
Summary:	Hijri Islamic Calendar converting functions for python
BuildArch:	noarch
Requires:	python
Requires:	setuptool

%description -n python-hijra
Hijri Islamic Calendar converting functions,
an enhanced algorithm designed by Muayyad Saleh Alsadi<alsadi@gmail.com>
it can be used to implement apps, gdesklets or karamba ..etc

This algorithm is based on integer operations
which that there is no round errors (given accurate coefficients)
the accuracy of this algorithm is based on 3 constants (p,q and a)
where p/q is the full months percentage [ gcd(p,q) must be 1 ]
currently it's set to 191/360 which mean that there is 191 months
having 30 days in a span of 360 years, other months are 29 days.
and a is just a shift.

%package applet
Summary:	Hijri Tray Applet for GNOME (also works with KDE)
Group:		System Environment/Base
BuildArch:	noarch
Requires:	python
Requires:	pygtk2
Requires:	notify-python
Requires:	desktop-notification-daemon
Requires:	python-hijra
Requires:	desktop-file-utils

%description applet
Hijri Tray Applet for GNOME (also works with KDE)
That uses Hijra Algorithm by Muayyad Saleh Alsadi<alsadi@gmail.com>
provided by python-hijra package

%package -n gnome-shell-extension-hijra
Summary:	gnome-shell extension to move hijri calendar
Group:		System Environment/Base
BuildArch:	noarch
Requires:	hijra-applet

%description -n gnome-shell-extension-hijra
Hijri Tray Applet as GNOME shell extension.

%prep
%setup -q -n %{name}-%{commit}

%build
# No thing to Build.

%install
%{__python2} setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2
mkdir $RPM_BUILD_ROOT/%{_datadir}/HijriTerminal/
install -m 755 terminal/hijri $RPM_BUILD_ROOT/%{_bindir}
install -m 755 terminal/هجري $RPM_BUILD_ROOT/%{_bindir}
install -m 644 hijra.py $RPM_BUILD_ROOT/%{_datadir}/HijriTerminal/hijri.py
install -m 644 HijriCal.py $RPM_BUILD_ROOT/%{_datadir}/HijriTerminal/

%files -n hijri
%doc waqf2-ar.pdf
%{_datadir}/HijriTerminal
%{_bindir}/hijri
%{_bindir}/هجري

%files -n python-hijra
%{_datadir}/doc/hijra-python/*
%doc waqf2-ar.pdf
%{python2_sitelib}/*

%files applet
%doc readme-ar.html waqf2-ar.pdf
%{_bindir}/HijriApplet
%{_datadir}/hijra/*
/etc/xdg/autostart/*

%files -n gnome-shell-extension-hijra
%{_datadir}/gnome-shell/extensions/HijriApplet@ojuba.org/*

%changelog
* Fri Feb 28 2014 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.2-1
- Disable notify.

* Sat Feb 15 2014 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.1-1
- Almasa Hijri program included into Hijra.
- Full Rivision.
- Fixes.

* Sun Jun 2 2012  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.2-1
- port to gtk3, webkit3

* Fri Jan 13 2012  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.1-1
- update for gnome 3.2 support

* Wed Jul 20 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.0-1
- gnome 3 support

* Sat Feb 14 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.18-1
- use dbus so that only one applet is running

* Sat Jan 31 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.17-1
- reformatting the license

* Sat Jan 24 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.16-1
- include an initial English translaion of the license

* Thu Jan 22 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.15-1
- don't show then hide if --hidden is passed

* Wed Jan 21 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.14-1
- get colors from theme
- highlight week end

* Sat Jan 3 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.13-1
- add tooltips

* Sat Dec 31 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.12-1
- fix 31 Dec bug

* Sat Dec 20 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.11-2
- add noarch

* Fri Dec 19 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.11-1
- Auto detect direction from pango

* Sun Aug 03 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.10-1
- Auto update date
- Fix consistency bug

* Tue Jul 22 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.9-1
- Auto update date

* Sat Jun 28 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.8-1
- Initial packing
