%define name	qlandkartegt
%define oname	QLandkarteGT
%define version	0.9.1
%define reldate	2008.12.05
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Views and transfers data to a Garmin GPS receiver
Version: 	%{version}
Release: 	%{release}
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/qlandkarte/%{oname}.%{version}.tar.gz
URL:		http://qlandkartegt.sourceforge.net/
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	gdal-devel
BuildRequires:	proj-devel
BuildRequires:	desktop-file-utils
Obsoletes:	qlandkarte < %version
Provides:	qlandkarte = %version

%description
This is a raster map tool chain to view map sets stored as GeoTiff on a
PC as well as on a portable device such as PPCs.

%prep
%setup -q -n %{oname}.%{reldate}

%build
%cmake_qt4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

mkdir -p %buildroot%_libdir/qlandkarte, %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=QLandkarteGT
Exec=qlandkartegt
Icon=qlandkarte
Terminal=false
Type=Application
X-MultipleArgs=false
Categories=Qt;Utility;Geography;DataVisualization;
GenericName=Garmin GPS utility
EOF

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
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/qlandkartegt.png
%{_mandir}/man1/*
