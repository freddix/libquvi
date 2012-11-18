Summary:	A cross-platform library for parsing flash media stream
Name:		libquvi
Version:	0.4.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	acc5a5da25a7f89c6ff5338d00eaaf58
Patch0:		%{name}-am.patch
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libquvi-scripts
BuildRequires:	libtool
BuildRequires:	lua-devel
BuildRequires:	pkg-config
Requires:	libquvi-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libquvi is a cross-platform library for parsing flash media stream.

%package devel
Summary:	Header files for libquvi library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libquvi library.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libquvi.so.7
%attr(755,root,root) %{_libdir}/libquvi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquvi.so
%{_libdir}/libquvi.la
%{_mandir}/man3/libquvi.3*
%{_includedir}/quvi
%{_pkgconfigdir}/libquvi.pc

