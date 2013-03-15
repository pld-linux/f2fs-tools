Summary:	Utilities for managing the f2fs filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików f2fs
Name:		f2fs-tools
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	f163f5cff30c3d2bb59a5b002b3141ea
URL:		http://f2fs-tools.sourceforge.net/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libuuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for flash-friendly filesystem (f2fs).

%description -l pl.UTF-8
Pakiet ten zawiera narzędzia do tworzenia systemów plików f2fs.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/mkfs.f2fs
%{_mandir}/man8/mkfs.f2fs.8*
