Summary:	Wacom model feature query library
Name:		libwacom
Version:	0.6.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/linuxwacom/%{name}-%{version}.tar.bz2
# Source0-md5:	b1193c0e1e5400b2f1c97cf8fbee3ff3
URL:		http://linuxwacom.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	doxygen
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwacom is a library to identify Wacom tablets and their
model-specific features.

%package devel
Summary:	Header files for libwacom library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libwacom library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_bindir}/libwacom-list-local-devices
%attr(755,root,root) %ghost %{_libdir}/libwacom.so.?
%attr(755,root,root) %{_libdir}/libwacom.so.*.*.*
%{_datadir}/libwacom

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwacom.so
%{_includedir}/libwacom-1.0
%{_pkgconfigdir}/libwacom.pc

