%define name	qlandkartegt
%define oname	QLandkarteGT
%define version 1.2.4
%define release %mkrel 1

Name:		%{name}
Summary:	Views and transfers data to a Garmin GPS receiver
Version:	%{version}
Release:	%{release}
Source0:	http://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
Patch0:		qlandkartegt-1.1.2-fix-str-fmt.patch
Patch1:		glu_include.patch
URL:		http://www.qlandkarte.org/
License:	GPLv2+
Group:		Communications
Requires:	garmindev(interface) = 1.18
Requires:	gpsbabel
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	zlib-devel
BuildRequires:	gdal-devel
BuildRequires:	proj-devel
BuildRequires:	grass
BuildRequires:	desktop-file-utils
BuildRequires:	libexif-devel
BuildRequires:	gpsd-devel
Obsoletes:	qlandkarte < %version
Provides:	qlandkarte = %version
BuildRoot:	%{_tmppath}/%{name}-buildroot


%description
This is a raster map tool chain to view map sets stored as GeoTiff on a
PC as well as on a portable device such as PPCs.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0

%build
%cmake -DGPX_EXTENSIONS=ON
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%__install -d "%{buildroot}%{_libdir}/%{name}"
cp "build/lib/libSerialPort.so"	"%{buildroot}%{_libdir}/"
cp "build/lib/libqzip.so"	"%{buildroot}%{_libdir}/"
cp "build/lib/libqtexthtmlexporter.so"	"%{buildroot}%{_libdir}/"



%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,-)
%doc copying changelog.txt
%{_bindir}/%{name}
%{_bindir}/map2gcm
%{_libdir}/libqtexthtmlexporter.so
%{_libdir}/libSerialPort.so
%{_libdir}/libqzip.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*
