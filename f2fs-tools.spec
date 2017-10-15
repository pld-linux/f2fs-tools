Summary:	Utilities for managing the f2fs filesystem
Summary(pl.UTF-8):	Narzędzia do zarządzania systemem plików f2fs
Name:		f2fs-tools
Version:	1.9.0
Release:	1
License:	GPL v2 (tools), GPL v2 or LGPL v2.1 (libraries)
Group:		Applications/System
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	f35cfdee1dc616f226fff96a56974d8c
Patch0:		blkid.patch
URL:		http://f2fs-tools.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libblkid-devel
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NAND flash memory-based storage devices, such as SSD, and SD cards,
have been widely being used for ranging from mobile to server systems.
Since they are known to have different characteristics from the
conventional rotational disks, a file system, an upper layer to the
storage device, should adapt to the changes from the sketch.

F2FS is a new file system carefully designed for the NAND flash
memory-based storage devices. We chose a log structure file system
approach, but we tried to adapt it to the new form of storage. Also we
remedy some known issues of the very old log structured file system,
such as snowball effect of wandering tree and high cleaning overhead.

Because a NAND-based storage device shows different characteristics
according to its internal geometry or flash memory management scheme
aka FTL, we add various parameters not only for configuring on-disk
layout, but also for selecting allocation and cleaning algorithms.

%description -l pl.UTF-8
Urządzenia przechowujące ane oparte na pamięci flash NAND, takie jak
dyski SSD i karty SD, mają szerokie zastosowanie od systemów
przenośnych po serwerowe. Ponieważ mają inną charakterystykę od
klasycznych dysków obrotowych, system plików, będący wyższą warstwą
przechowywania danych, powinien być do niej dostosowany.

F2FS to nowy system plików zaprojektowany z troską o urządzenia oparte
na pamięci flash NAND. Wykorzystuje podejście oparte na strukturze
logu, ale zaadaptowanej do nowego rodzaju pamięci.

Ponieważ urządzenia oparte na pamięci NAND mają różną charakterystykę
w zależności od wewnętrznej geometrii lub schematu zarządzania
pamięcią (FTL), dodane zostały różne parametry nie tylko do
konfigurowania ułożenia systemu na dysku, ale także wyboru algorytmów
przydzielania i czyszczenia.

%package devel
Summary:	Header files for f2fs libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek f2fs
License:	GPL v2 or LGPL v2.1
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop applications
that use f2fs libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia aplikacji
wykorzystujących biblioteki f2fs.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	CP="cp -p" \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
cp -p include/f2fs_fs.h $RPM_BUILD_ROOT%{_includedir}
cp -p mkfs/f2fs_format_utils.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libf2fs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libf2fs.so.3
%attr(755,root,root) %{_libdir}/libf2fs_format.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libf2fs_format.so.2
%attr(755,root,root) %{_sbindir}/defrag.f2fs
%attr(755,root,root) %{_sbindir}/dump.f2fs
%attr(755,root,root) %{_sbindir}/f2fscrypt
%attr(755,root,root) %{_sbindir}/f2fstat
%attr(755,root,root) %{_sbindir}/fibmap.f2fs
%attr(755,root,root) %{_sbindir}/fsck.f2fs
%attr(755,root,root) %{_sbindir}/mkfs.f2fs
%attr(755,root,root) %{_sbindir}/parse.f2fs
%attr(755,root,root) %{_sbindir}/resize.f2fs
%attr(755,root,root) %{_sbindir}/sload.f2fs
%{_mandir}/man8/defrag.f2fs.8*
%{_mandir}/man8/dump.f2fs.8*
%{_mandir}/man8/f2fscrypt.8*
%{_mandir}/man8/fsck.f2fs.8*
%{_mandir}/man8/mkfs.f2fs.8*
%{_mandir}/man8/resize.f2fs.8*
%{_mandir}/man8/sload.f2fs.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libf2fs.so
%attr(755,root,root) %{_libdir}/libf2fs_format.so
%{_libdir}/libf2fs.la
%{_libdir}/libf2fs_format.la
%{_includedir}/f2fs_format_utils.h
%{_includedir}/f2fs_fs.h
