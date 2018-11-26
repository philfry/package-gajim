Name: gajim
Version: 1.1.0
Release: 1%{?dist}
Summary: a jabber/xmpp client
Group: Applications/Internet
License: GPLv3
URL: https://gajim.org/
Source0: https://gajim.org/downloads/1.0/%{name}-%{version}.tar.bz2
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python3-devel
BuildRequires: python3-setuptools_git
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: hardlink

Requires: hicolor-icon-theme
Requires: gtk-update-icon-cache

Requires: python3 >= 3.4
Requires: python3-gobject-base
Requires: python3-gobject
Requires: gtk3
Requires: python3-nbxmpp >= 0.6.8
Requires: python3-pyOpenSSL >= 0.14
Requires: python3-pyasn1
Requires: python3-pillow
Requires: python3-crypto
Requires: python3-gnupg
Requires: dbus-glib
Requires: python-avahi
Requires: gspell
Requires: hunspell
Requires: libsecret
Requires: python3-dbus >= 1.2.0
Requires: telepathy-farstream >= 0.2
Requires: gstreamer
Requires: gstreamer-plugins-base
Requires: gupnp
#Requires: NetworkManager-glib
#Requires: NetworkManager-libnm
Requires: geoclue2-libs
Requires: python3-idna
Requires: python3-precis_i18n


%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's developers is
to provide a full featured and easy to use xmpp client for the GTK+ users.
Gajim does not require GNOME to run, even though it exists with it nicely.


%prep
%setup -q


%build
%py3_build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
CFLAGS="%{optflags}" python3 setup.py install -O1 --root %{buildroot}
hardlink -vv %{buildroot}%{_bindir}
%find_lang %{name}


%clean
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
[ $1 -eq 0 ] || exit 0
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-history-manager
%{_bindir}/%{name}-remote
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-history-manager.1*
%{_mandir}/man1/%{name}-remote.1*
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/icons/hicolor/*/apps/*.png
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/


%changelog
* Tue May 22 2018 Philippe Kueck <projects@unixadm.org> - 1.0.3-1
- bump to 1.0.3

* Thu May  3 2018 Philippe Kueck <projects@unixadm.org> - 1.0.2-1
- bump to 1.0.2

* Sun Apr  8 2018 Philippe Kueck <projects@unixadm.org> - 1.0.1-1
- bump to 1.0.1

* Fri Mar 23 2018 Philippe Kueck <projects@unixadm.org> - 1.0.0-1
- bump to 1.0.0

* Fri Mar  9 2018 Philippe Kueck <projects@unixadm.org> - 1.0.0-0.1
- initial packaging
