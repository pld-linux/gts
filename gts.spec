Summary:	GNU Triangulated Surface Library
Summary(pl):	Biblioteka triangulowanych powierzchni GNU
Name:		gts
Version:	0.7.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gts/%{name}-%{version}.tar.gz
# Source0-md5:	9f710aefd2ed9b3cc1b1216171fc5a8a
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-as_needed-fix.patch
URL:		http://gts.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTS stands for the GNU Triangulated Surface Library. It includes a
number of useful functions to deal with triangulated surfaces
including, but not limited to, multi-resolution models, Delaunay and
Constrained Delaunay triangulations, set operations on surfaces
(intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for
fast rendering.

%description -l pl
GTS oznacza bibliotekê triangulowanych powierzchni GNU. Zawiera wiele
u¿ytecznych funkcji do operacji na triangulowanych powierzchniach, w
tym miêdzy innymi modele w wielu rozdzielczo¶ciach, triangulacje
Delaunaya i ograniczona Delaunaya, zestaw operacji na powierzchniach
(przeciêcia, sumy itd...), drzewa prostopad³o¶cianów ograniczaj±cych
do wydajnego wykrywania kolizji i przeciêæ, szybkie generowanie pasów
trójk±tów dla szybkiego renderingu.

%package devel
Summary:	Header files for gts library
Summary(pl):	Pliki nag³ówkowe biblioteki gts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gts library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gts.

%package static
Summary:	Static gts library
Summary(pl):	Statyczna biblioteka gts
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gts library.

%description static -l pl
Statyczna biblioteka gts.

%prep
%setup -q
#patch0 -p1
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gts[2ct]*
%attr(755,root,root) %{_bindir}/[st]*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
#%doc doc/html/*
%attr(755,root,root) %{_bindir}/gts-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
