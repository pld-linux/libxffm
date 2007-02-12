Summary:	Filemanagement library for the xffm applications
Summary(pl.UTF-8):   Biblioteka zarządzania plików dla aplikacji xffm
Name:		libxffm
Version:	4.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xffm/%{name}-%{version}.tar.gz
# Source0-md5:	9496e945c1d8bc85906b1d28a5edd6a2
URL:		http://xffm.sourceforge.net/libxffm.html
Patch0:		%{name}-pc.patch
Patch1:		%{name}-asneeded.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbh-devel >= 4.5.0
BuildRequires:	gnome-icon-theme >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	libtubo-devel >= 4.5.0
BuildRequires:	xfce4-icon-theme >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxffm is the basic filemanagement library used by xffm applications.

%description -l pl.UTF-8
libxffm jest podstawową biblioteką zarządzania plików używaną przez
aplikacje xffm.

%package devel
Summary:	Header files for libxffm library
Summary(pl.UTF-8):   Pliki nagłówkowe dla biblioteki libxffm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbh-devel >= 4.5.0
Requires:	libtubo-devel >= 4.5.0

%description devel
Header files for libxffm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki libxffm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOTs

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libxffm_actions.so.*.*.*
%attr(755,root,root) %{_libdir}/libxffm_primary.so.*.*.*
%attr(755,root,root) %{_libdir}/libxffm_secondary.so.*.*.*
# libraries needed by other apps, so aren't in devel subpackage
%attr(755,root,root) %{_libdir}/libxffm_applications.so
%attr(755,root,root) %{_libdir}/libxffm_combo.so
%attr(755,root,root) %{_libdir}/libxffm_find.so
%attr(755,root,root) %{_libdir}/libxffm_icons.so
%attr(755,root,root) %{_libdir}/libxffm_prop.so
%{_datadir}/xffm
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxffm_actions.so
%attr(755,root,root) %{_libdir}/libxffm_primary.so
%attr(755,root,root) %{_libdir}/libxffm_secondary.so
%{_libdir}/libxffm_actions.la
%{_libdir}/libxffm_primary.la
%{_libdir}/libxffm_secondary.la
%{_libdir}/libxffm_applications.la
%{_libdir}/libxffm_combo.la
%{_libdir}/libxffm_find.la
%{_libdir}/libxffm_icons.la
%{_libdir}/libxffm_prop.la
%{_pkgconfigdir}/libxffm.pc
%{_includedir}/xffm/*.h
