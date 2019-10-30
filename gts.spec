Summary:	GNU Triangulated Surface Library
Summary(pl.UTF-8):	Biblioteka GNU do triangulowanych powierzchni
Name:		gts
Version:	0.7.6
Release:	8
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gts/%{name}-%{version}.tar.gz
# Source0-md5:	9f710aefd2ed9b3cc1b1216171fc5a8a
Patch0:		%{name}-as_needed-fix.patch
Patch1:		%{name}-lib64-gts-config.in.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-netpbm.patch
URL:		http://gts.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	netpbm-devel
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTS stands for the GNU Triangulated Surface Library. It includes a
number of useful functions to deal with triangulated surfaces
including, but not limited to, multi-resolution models, Delaunay and
Constrained Delaunay triangulations, set operations on surfaces
(intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for
fast rendering.

%description -l pl.UTF-8
GTS oznacza bibliotekę GNU do triangulowanych powierzchni. Zawiera
wiele użytecznych funkcji do operacji na triangulowanych
powierzchniach, w tym między innymi modele w wielu rozdzielczościach,
triangulacje Delaunaya i ograniczona Delaunaya, zestaw operacji na
powierzchniach (przecięcia, sumy itd...), drzewa prostopadłościanów
ograniczających do wydajnego wykrywania kolizji i przecięć, szybkie
generowanie pasów trójkątów dla szybkiego renderingu.

%package devel
Summary:	Header files for gts library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0

%description devel
Header files for gts library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gts.

%package static
Summary:	Static gts library
Summary(pl.UTF-8):	Statyczna biblioteka gts
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gts library.

%description static -l pl.UTF-8
Statyczna biblioteka gts.

%prep
%setup -q
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgts.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/delaunay
%attr(755,root,root) %{_bindir}/gts2dxf
%attr(755,root,root) %{_bindir}/gts2oogl
%attr(755,root,root) %{_bindir}/gts2stl
%attr(755,root,root) %{_bindir}/gtscheck
%attr(755,root,root) %{_bindir}/gtscompare
%attr(755,root,root) %{_bindir}/gtstemplate
%attr(755,root,root) %{_bindir}/happrox
%attr(755,root,root) %{_bindir}/stl2gts
%attr(755,root,root) %{_bindir}/transform
%attr(755,root,root) %{_libdir}/libgts-0.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgts-0.7.so.5

%files devel
%defattr(644,root,root,755)
%doc doc/html/*.html
%attr(755,root,root) %{_bindir}/gts-config
%attr(755,root,root) %{_libdir}/libgts.so
%{_includedir}/gts*.h
%{_aclocaldir}/gts.m4
%{_pkgconfigdir}/gts.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgts.a
