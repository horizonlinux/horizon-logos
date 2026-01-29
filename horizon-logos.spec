Name:       horizon-logos
Version:    100.4
Release:    1%{?dist}
Summary:    Horizon-related icons and pictures

Group:      System Environment/Base
License:    GPLv3 AND CC-BY-2.0
URL:        https://github.com/horizonlinux/horizon-logos
Source0:    https://github.com/horizonlinux/horizon-logos/archive/refs/tags/100.4.tar.gz
Source1:    fedora-logo.ico

Obsoletes:  centos-logos < 90.4-1
Provides:   system-logos = %{version}-%{release}
Provides:   redhat-logos = %{version}-%{release}
Provides:   centos-logos = %{version}-%{release}

Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
Conflicts:  centos-artwork <= 5.0.5

Requires(post): coreutils
BuildRequires: hardlink
BuildRequires: make
BuildRequires: python3

%description
Horizon-related icons and pictures

%package httpd
Summary: Horizon-related icons and pictures used by httpd
Provides: system-logos-httpd = %{version}-%{release}
Provides: redhat-logos-httpd = %{version}-%{release}
Provides: centos-logos-httpd = %{version}-%{release}
Provides: system-logos(httpd-logo-ng)
BuildArch: noarch

%description httpd
Horizon-related icons and pictures used by httpd

%package ipa
Summary: Horizon-related icons and pictures used by ipa
Provides: system-logos-ipa = %{version}-%{release}
Provides: redhat-logos-ipa = %{version}-%{release}
Provides: centos-logos-ipa = %{version}-%{release}
BuildArch: noarch

%description ipa
Horizon-related icons and pictures used by ipa

%package -n horizon-backgrounds
Summary: Horizon-related desktop backgrounds
BuildArch: noarch

Obsoletes: centos-logos < 80.1-2
Obsoletes: desktop-backgrounds-compat < %{version}-%{release}
Obsoletes: desktop-backgrounds-gnome < %{version}-%{release}
Obsoletes: desktop-backgrounds-kde < %{version}-%{release}
Provides:  desktop-backgrounds-compat = %{version}-%{release}
Provides:  desktop-backgrounds-gnome = %{version}-%{release}
Provides:  desktop-backgrounds-kde = %{version}-%{release}
Provides:  system-backgrounds = %{version}-%{release}
Provides:  system-backgrounds-compat = %{version}-%{release}
Provides:  system-backgrounds-gnome = %{version}-%{release}
Provides:  system-backgrounds-kde = %{version}-%{release}
Requires:  horizon-logos = %{version}-%{release}

%description -n horizon-backgrounds
Horizon-related desktop backgrounds


%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/ZlataPraha/
for i in backgrounds/ZlataPraha/*.jpg; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/ZlataPraha/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/WarsawBlueHour/
for i in backgrounds/WarsawBlueHour/*.jpg; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/WarsawBlueHour/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wallpapers/ZlataPraha/
for i in wallpapers/ZlataPraha/*.json; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/wallpapers/ZlataPraha/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wallpapers/WarsawBlueHour/
for i in wallpapers/WarsawBlueHour/*.json; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/wallpapers/WarsawBlueHour/
done


mkdir -p $RPM_BUILD_ROOT%{_datadir}/wallpapers/ZlataPraha/contents/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wallpapers/WarsawBlueHour/contents/
install -p -m 644 wallpapers/ZlataPraha/contents/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/wallpapers/ZlataPraha/contents/
install -p -m 644 wallpapers/WarsawBlueHour/contents/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/wallpapers/WarsawBlueHour/contents/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/wallpapers/ZlataPraha/contents/images/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wallpapers/WarsawBlueHour/contents/images/
for i in backgrounds/ZlataPraha/*.jpg; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/wallpapers/ZlataPraha/contents/images/5755x3369.jpg
done
for i in backgrounds/WarsawBlueHour/*.jpg; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/wallpapers/WarsawBlueHour/contents/images/4725x2658.jpg
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.background.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.screensaver.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/ZlataPraha/ZlataPraha.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/WarsawBlueHour/WarsawBlueHour.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
for i in bootloader/*; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
for i in plymouth/charge/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
done

# The Plymoth spinner theme Fedora logo bits
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/spinner
install -p -m 644 pixmaps/fedora-gdm-logo.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/spinner/watermark.png

for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  done
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
pushd $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_datadir}/icons/hicolor/16x16/apps/fedora-logo-icon.png favicon.png
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/fedora-logo-icon.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/start-here.svg
install -p -m 644 icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/xfce4_xicon1.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
ln -s ../apps/start-here.svg .
popd

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a fedora/*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.png $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.jpg $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ipa/modern-ui/assets/images
cp -a ipa/modern-ui/*.png $RPM_BUILD_ROOT%{_datadir}/ipa/modern-ui/assets/images
cp -a ipa/modern-ui/*.jpg $RPM_BUILD_ROOT%{_datadir}/ipa/modern-ui/assets/images

mkdir -p $RPM_BUILD_ROOT%{_datadir}/testpage
install -p -m 644 testpage/index.html $RPM_BUILD_ROOT%{_datadir}/testpage

# save some dup'd icons
# Except in /boot. Because some people think it is fun to use VFAT for /boot.
hardlink -v %{buildroot}/usr

%ifnarch x86_64 i686
rm -f $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/splash.lss
%endif

%post
touch --no-create %{_datadir}/icons/hicolor || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING CC-BY-2.0 GPLv3
%config(noreplace) %{_sysconfdir}/favicon.png
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/firstboot/themes/fedora-%{codename}/
%{_datadir}/plymouth/themes/charge/
%{_datadir}/plymouth/themes/spinner/

%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/anaconda/pixmaps/*
%ifarch x86_64 i686
%{_datadir}/anaconda/boot/splash.lss
%endif
%{_datadir}/anaconda/boot/syslinux-splash.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/%{name}/

# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/backgrounds/
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/22x22/apps/
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/36x36/
%dir %{_datadir}/icons/hicolor/36x36/apps/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%dir %{_datadir}/icons/hicolor/96x96/
%dir %{_datadir}/icons/hicolor/96x96/apps/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%dir %{_datadir}/icons/hicolor/scalable/places/
%dir %{_datadir}/anaconda
%dir %{_datadir}/anaconda/boot/
%dir %{_datadir}/anaconda/pixmaps
%dir %{_datadir}/firstboot/
%dir %{_datadir}/firstboot/themes/
%dir %{_datadir}/plymouth/
%dir %{_datadir}/plymouth/themes/
%dir %{_datadir}/wallpapers/
%dir %{_datadir}/wallpapers/ZlataPraha/
%dir %{_datadir}/wallpapers/ZlataPraha/contents
%dir %{_datadir}/wallpapers/WarsawBlueHour/
%dir %{_datadir}/wallpapers/WarsawBlueHour/contents

%files httpd
%license COPYING CC-BY-2.0 GPLv3
%{_datadir}/pixmaps/poweredby.png
%{_datadir}/testpage
%{_datadir}/testpage/index.html

%files ipa
%license COPYING CC-BY-2.0 GPLv3
%{_datadir}/ipa/ui/images/*
# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/ipa
%dir %{_datadir}/ipa/ui
%dir %{_datadir}/ipa/ui/images

# The same for modern-ui
%{_datadir}/ipa/modern-ui/assets/images/*
# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/ipa/modern-ui
%dir %{_datadir}/ipa/modern-ui/assets
%dir %{_datadir}/ipa/modern-ui/assets/images

%files -n horizon-backgrounds
%license COPYING CC-BY-2.0 GPLv3
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/*
%{_datadir}/wallpapers/*


%changelog
* Thu Jan 29 2026 Marcel Mrówka <micro.mail88@gmail.com>
- package created, based off centos-logos
