%global owner ojuba-org

Name: hijra
Summary: Hijri Islamic Calendar
Summary(ar): التّقويم الهجري الإسلامي
URL: http://ojuba.org
Version: 1.0
Release: 1%{?dist}
Source0: https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: WAQFv2
BuildArch: noarch
Requires: python3
Requires: pygobject3 >= 3.0.2
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Hijra provides Hijri/Islamic Calendar routines and utils in python.

%description -l ar
يقدّم هجرة أدوات التّقويم الهجري الإسلامي في بيثون.

%package -n hijri
Summary: Hijri Terminal
Summary(ar): هجري الطّرفية
BuildArch: noarch

%description -n hijri
Using all Hijra operations in terminal.

%description -n hijri -l ar
جميع خصائص برنامج هجرة في الطّرفية.

%package -n python3-hijra
Summary: Hijri functions for python
Summary(ar): وظائف هجرة لبيثون
BuildArch: noarch
Requires: python3
Requires: setuptool

%description -n python3-hijra
Hijri Islamic Calendar converting functions,
an enhanced algorithm designed by Muayyad
Saleh Alsadi, it can be used to implement apps,
gdesklets or karamba ..etc

%description -n python3-hijra -l ar
الوظائف التّحويلية للتّقويم الهجري الإسلامي بخوارزمية مُحسّنة
مُصمّمة بواسطة مؤيّد صالح السّعدي، يُمكن استخدامها و غرسها في
أدوات سطح المكتب مثل كارامبا .. و غيره.

%package applet
Summary: Hijri Tray Applet
Summary(ar): بريمج هجرة لصينية النّظام
BuildArch: noarch
Requires: python3
Requires: pygtk2
Requires: python3-notify
Requires: desktop-notification-daemon
Requires: python3-hijra
Requires: desktop-file-utils

%description applet
Hijri Tray Applet for GNOME (also works with KDE)
That uses Hijra Algorithm provided by python-hijra.

%description applet -l ar
بريمج هجرة لصينية النّظام لجنوم (ويعمل أيضًا بكدي)
باستعمال خوارزمية هجرة من python-hijra.

%package -n gnome-shell-extension-hijra
Summary: Hijri Gnome-shell extension
Summary(ar): امتداد هجرة لجنوم شل
BuildArch: noarch
Requires: hijra-applet

%description -n gnome-shell-extension-hijra
Hijri Tray Applet as GNOME shell extension.

%description -n gnome-shell-extension-hijra -l ar
بريمج صينية النّظام هجرة كامتداد جنوم شل.

%prep
%autosetup -n %{name}-%{version}

%build
# No thing to Build.

%install
%{__python3} setup.py install \
        --root=%{buildroot} \
        --optimize=2
mkdir %{buildroot}/%{_datadir}/HijriTerminal/
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 755 terminal/hijri %{buildroot}/%{_bindir}
install -m 755 terminal/هجري %{buildroot}/%{_bindir}
install -m 644 hijra.py %{buildroot}/%{_datadir}/HijriTerminal/hijri.py
install -m 644 HijriCal.py %{buildroot}/%{_datadir}/HijriTerminal/
install -m 644 terminal/hijri.1.gz %{buildroot}%{_mandir}/man1

%files -n hijri
%license waqf2-ar.pdf
%{_datadir}/HijriTerminal
%{_bindir}/hijri
%{_bindir}/هجري
%{_mandir}/*/hijri.*

%files -n python3-hijra
%license waqf2-ar.pdf
%{_datadir}/doc/hijra-python/*
%{python3_sitelib}/*

%files applet
%license waqf2-ar.pdf
%doc readme-ar.html
%{_bindir}/HijriApplet
%{_datadir}/hijra/*
/etc/xdg/autostart/*

%files -n gnome-shell-extension-hijra
%{_datadir}/gnome-shell/extensions/HijriApplet@ojuba.org/*

%changelog
- Thu Jan 16 2020 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 1.0-1
- New generation with Python3

* Wed Feb 1 2017 Mosaab Alzoubi <moceap@hotmail.com> - 0.4.1-1
- Support running under Wayland
- Fix Hijri errors
- Fix Python Gi warnings

* Mon Jan 30 2017 Mosaab Alzoubi <moceap@hotmail.com> - 0.4-1
- Update to 0.4
- New way to Github

* Thu Jul 23 2015 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.2-2
- General Revision
- Use %%license
- Remove old Group tag
- Add man pages
- Add Arabic Summaries and Descriptions

* Fri Feb 28 2014 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.2-1
- Disable notify.

* Sat Feb 15 2014 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.1-1
- Almasa Hijri program included into Hijra.
- Full Rivision.
- Fixes.

* Sat Jun 2 2012  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.2-1
- port to gtk3, webkit3

* Fri Jan 13 2012  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.1-1
- update for gnome 3.2 support

* Mon Jul 20 2009  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.2.0-1
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

* Wed Dec 31 2008  Muayyad Saleh AlSadi <alsadi@ojuba.org> - 0.1.12-1
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
