Summary:	Utilities for managing the f2fs filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików f2fs
Name:		f2fs-tools
Version:	1.7.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	9db22274264f0c88dbee012f257917b1
URL:		http://f2fs-tools.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NAND flash memory-based storage devices, such as SSD, and SD cards,
have been widely being used for ranging from mobile to server systems.
Since they are known to have different characteristics from the
conventional rotational disks,a file system, an upper layer to the
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
Pakiet ten zawiera narzędzia do tworzenia systemów plików f2fs.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the libraries needed to develop applications
that use f2fs-tools

%prep
%setup -q

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
%attr(755,root,root) %ghost %{_libdir}/libf2fs.so.1
%attr(755,root,root) %{_libdir}/libf2fs_format.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libf2fs_format.so.0
%attr(755,root,root) %{_sbindir}/defrag.f2fs
%attr(755,root,root) %{_sbindir}/dump.f2fs
%attr(755,root,root) %{_sbindir}/f2fstat
%attr(755,root,root) %{_sbindir}/fibmap.f2fs
%attr(755,root,root) %{_sbindir}/fsck.f2fs
%attr(755,root,root) %{_sbindir}/mkfs.f2fs
%attr(755,root,root) %{_sbindir}/parse.f2fs
%attr(755,root,root) %{_sbindir}/resize.f2fs
%attr(755,root,root) %{_sbindir}/sload.f2fs
%{_mandir}/man8/defrag.f2fs.8*
%{_mandir}/man8/dump.f2fs.8*
%{_mandir}/man8/fsck.f2fs.8*
%{_mandir}/man8/mkfs.f2fs.8*
%{_mandir}/man8/resize.f2fs.8*
%{_mandir}/man8/sload.f2fs.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libf2fs.la
%{_libdir}/libf2fs.so
%{_libdir}/libf2fs_format.la
%{_libdir}/libf2fs_format.so
%{_includedir}/f2fs_format_utils.h
%{_includedir}/f2fs_fs.h
