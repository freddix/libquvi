Summary:	A cross-platform library for parsing flash media stream
Name:		libquvi
Version:	0.9.4
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
# Source0-md5:	8e3f2134a6b3376934bd884b07dcdac5
URL:		http://quvi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libquvi-scripts >= 0.9
BuildRequires:	libtool
BuildRequires:	lua-devel
BuildRequires:	pkg-config
Requires:	libquvi-scripts >= 0.9
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libquvi-0.9-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquvi-0.9.so
%{_mandir}/man[37]/*
%{_includedir}/quvi-0.9
%{_pkgconfigdir}/libquvi-0.9.pc

