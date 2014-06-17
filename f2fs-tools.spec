Summary:	Utilities for managing the f2fs filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików f2fs
Name:		f2fs-tools
Version:	1.3.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	fd5f9cbef72a58f3264f27d72a27b8ae
Patch0:		no_subst.patch
URL:		http://f2fs-tools.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for flash-friendly filesystem (f2fs).

%description -l pl.UTF-8
Pakiet ten zawiera narzędzia do tworzenia systemów plików f2fs.

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
	DESTDIR=$RPM_BUILD_ROOT

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libf2fs.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libf2fs.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libf2fs.so.0
%attr(755,root,root) %{_sbindir}/dump.f2fs
%attr(755,root,root) %{_sbindir}/f2fstat
%attr(755,root,root) %{_sbindir}/fibmap.f2fs
%attr(755,root,root) %{_sbindir}/fsck.f2fs
%attr(755,root,root) %{_sbindir}/mkfs.f2fs
%{_mandir}/man8/mkfs.f2fs.8*
