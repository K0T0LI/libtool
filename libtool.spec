Summary:	GNU libtool, a shared library generation tool
Summary(es):	GNU libtool, una herramienta de creaci�n de bibliotecas compartidas
Summary(pl):	GNU libtool - narz�dzie do generowania bibliotek wsp�dzielonych
Summary(pt_BR):	GNU libtool, uma ferramenta de gera��o de bibliotecas compartilhadas
Name:		libtool
Version:	1.4.2
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-mktemp.patch
Patch2:		%{name}-test.patch
URL:		http://www.gnu.org/software/libtool/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in generic fashion.

%description -l es
GNU libtool es un conjunto de scripts shell para configurar
autom�ticamente la creaci�n de bibliotecas compartidas para varias
arquitecturas UNIX de una manera gen�rica.

%description -l pl
GNU libtool jest zbiorem skrypt�w shellowych do automatycznego
generowania bibliotek wsp�dzielonych niezale�nie od typu platformy
systemowej.

%description -l pt_BR
GNU libtool � um conjunto de scripts shell para configurar
automaticamente a gera��o de bibliotecas compartilhadas para v�rias
arquiteturas UNIX de uma maneira gen�rica.

%package -n libltdl
Summary:	System independent dlopen wrapper for GNU libtool
Summary(pl):	Biblioteka og�lnych wywo�a� dlopen
Summary(pt_BR):	GNU libltdl, um wrapper dlopen para o GNU libtool
Group:		Libraries
Obsoletes:	libtool-libs

%description -n libltdl
System independent dlopen wrapper for GNU libtool.

%description -n libltdl -l pl
Biblioteka og�lnych wywo�a� dlopen.

%description -n libltdl -l pt_BR
GNU libltdl, um wrapper dlopen para o GNU libtool.

%package -n libltdl-devel
Summary:	Development components for libltdl
Summary(pl):	Cz�� libltdl przeznaczona dla programist�w
Summary(pt_BR):	Componentes de desenvolvimento para a libltdl
Group:		Development/Libraries
Requires:	libltdl = %{version}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool - development part.
Install this package if you want to develop for libltdl.

%description -n libltdl-devel -l pl
Biblioteka og�lnych wywo�a� dlopen - cz�� dla programist�w.

%description -n libltdl-devel -l pt_BR
Instale este pacote se voc� deseja desenvolver para a libltdl.

%package -n libltdl-static
Summary:	Static system independent dlopen wrapper for GNU libtool
Summary(pl):	Statyczna biblioteka og�lnych wywo�a� dlopen
Summary(pt_BR):	Componentes de desenvolvimento para a libltdl
Group:		Development/Libraries
Requires:	libltdl-devel = %{version}

%description -n libltdl-static
Static system independent dlopen wrapper for GNU libtool. Install this
package if you want to develop for libltdl, but using static
components (seldom used).

%description -n libltdl-static -l pl
Statyczna biblioteka og�lnych wywo�a� dlopen.

%description -n libltdl-static -l pt_BR
Instale este pacote se voc� deseja desenvolver para a libltdl,
utilizando componentes est�ticos (raramente necess�rio).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
aclocal
autoupdate
automake -a -c
autoconf
(cd libltdl
rm -f missing
aclocal
autoupdate
automake -a -c
autoconf)
%configure
%{__make} -C doc -k
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README THANKS TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   -n libltdl -p /sbin/ldconfig
%postun -n libltdl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz demo
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/libtool
%attr(755,root,root) %{_datadir}/libtool/config.guess
%attr(755,root,root) %{_datadir}/libtool/config.sub
%attr(755,root,root) %{_datadir}/libtool/ltmain.sh

%{_infodir}/libtool.info*
%{_aclocaldir}/libtool.m4

%files -n libltdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files -n libltdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/ltdl.m4

%dir %{_datadir}/libtool/libltdl
%{_datadir}/libtool/libltdl/a*
%{_datadir}/libtool/libltdl/config-h.in
%attr(755,root,root) %{_datadir}/libtool/libltdl/configure
%{_datadir}/libtool/libltdl/configure.in
%{_datadir}/libtool/libltdl/C*
%{_datadir}/libtool/libltdl/l*
%{_datadir}/libtool/libltdl/M*
%{_datadir}/libtool/libltdl/R*
%{_datadir}/libtool/libltdl/s*

%files -n libltdl-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
