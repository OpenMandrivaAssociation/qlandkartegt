%define name	qlandkartegt
%define oname	QLandkarteGT
%define version	0.20.1
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Views and transfers data to a Garmin GPS receiver
Version: 	%{version}
Release: 	%{release}
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/qlandkartegt/%{name}-%{version}.tar.gz
URL:		http://www.qlandkarte.org/
License:	GPLv2+
Group:		Communications
Requires:	garmindev(interface) = 1.18
Requires:	gpsbabel
BuildRequires:	cmake
BuildRequires:	qt4-devel
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

%build
%cmake_qt4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/qlandkartegt.png
%{_mandir}/man1/*
