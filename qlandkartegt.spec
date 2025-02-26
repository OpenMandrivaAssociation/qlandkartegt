Name:		qlandkartegt
Summary:	GPS device mapping tool
Version:	1.8.1
Release:	3
Source0:	http://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
Patch0:		qlandkartegt-1.3.0-fedora-glu.patch
URL:		https://www.qlandkarte.org/
License:	GPLv2+
Group:		Communications
Requires:	garmindev(interface) = 1.18
Requires:	gpsbabel
Suggests:	gdal
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gdal-devel
BuildRequires:	pkgconfig(proj)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgpsd)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:  jpeg-devel

Obsoletes:	qlandkarte < %{version}
Provides:	qlandkarte = %{version}

%description
QLandkarte GT is the ultimate outdoor aficionado's tool for GPS maps in
GeoTiff format as well as Garmin's img vector map format. Additional it is
the PC side frontend to QLandkarte M, a moving map application for mobile
devices. And it fills the gap Garmin leaves in refusing to support Linux.
QLandkarte GT is the proof that writing portable applications for Unix,
Windows and OSX is feasible with a minimum of overhead. No excuses!

QLandkarte GT does replace the original QLandkarte with a much more
flexible architecture. It's not limited to a map format or device. Thus
if you think your Magellan GPS or other should be supported, join the team.

Additionally it is a front end to the GDAL tools, to make georeferencing
scanned maps feasible for the normal user. Compared to similar tools like
QGis, it's target users are more on the consumer side than on the scientific
one. QLandkarte GT might not let you select every possible feature of the
GDAL tools, but it will simplify their use to the demands of most users.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DGPX_EXTENSIONS=ON
%make VERBOSE=1

%install
%makeinstall_std -C build
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc copying changelog.txt
%{_bindir}/%{name}
%{_bindir}/map2gcm
%{_bindir}/map2jnx
%{_bindir}/map2rmap
%{_bindir}/map2rmp
%{_bindir}/cache2gtiff
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*
