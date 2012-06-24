Summary:	GNU libtool, a shared library generation tool
Summary(es):	GNU libtool, una herramienta de creaci�n de bibliotecas compartidas
Summary(pl):	GNU libtool - narz�dzie do generowania bibliotek wsp�dzielonych
Summary(pt_BR):	GNU libtool, uma ferramenta de gera��o de bibliotecas compartilhadas
Summary(ru):	GNU libtool, ����� ������ ��� ��������� ����������� ���������
Summary(uk):	GNU libtool, ��¦� ���̦� ��� ������æ� ����ͦ���� ¦�̦����
Name:		libtool
Version:	1.4.2
Release:	13
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-mktemp.patch
Patch2:		%{name}-test.patch
Patch3:		%{name}-relink.patch
Patch4:		%{name}-ac253.patch
Patch5:		%{name}-new-ac.patch
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

%description -l ru
GNU libtool - ��� ����� �������� ��� �������������� ���������
������������ ����������� ��������� �� ��������� ������������ UNIX.

%description -l uk
GNU libtool - �� ��¦� �����Ԧ� ��� ����������ϧ ������æ� ����ͦ����
¦�̦���� �� Ҧ���� ��Ȧ�������� UNIX.

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
Summary(ru):	����� ��� ���������� �������� � libltdl
Summary(uk):	����� ��� �������� ������� � libltdl
Group:		Development/Libraries
Requires:	libltdl = %{version}

%description -n libltdl-devel
System independent dlopen wrapper for GNU libtool - development part.
Install this package if you want to develop for libltdl.

%description -n libltdl-devel -l pl
Biblioteka og�lnych wywo�a� dlopen - cz�� dla programist�w.

%description -n libltdl-devel -l pt_BR
Instale este pacote se voc� deseja desenvolver para a libltdl.

%description -n libltdl-devel -l uk
����� ��� �������� ������� � libltdl.

%description -n libltdl-devel -l ru
����� ��� ���������� �������� � libltdl.

%package -n libltdl-static
Summary:	Static system independent dlopen wrapper for GNU libtool
Summary(pl):	Statyczna biblioteka og�lnych wywo�a� dlopen
Summary(pt_BR):	Componentes de desenvolvimento para a libltdl
Summary(ru):	����������� ���������� libltdl �� libltdl
Summary(uk):	�������� ¦�̦����� libltdl � libltdl
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

%description -n libltdl-static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � libltdl.

%description -n libltdl-static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �� ¦���� �� ������� ��
������ libltdl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
rm -f missing
aclocal
autoupdate
%{__automake}
%{__autoconf}
cd libltdl
rm -f missing
cp -f ../ltmain.sh .
aclocal -I ..
autoupdate
%{__automake}
%{__autoconf}
cd ..

%configure
%{__make} -C doc -k
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
%doc AUTHORS NEWS README THANKS TODO ChangeLog demo
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/libtool
%attr(755,root,root) %{_datadir}/libtool/config.guess
%attr(755,root,root) %{_datadir}/libtool/config.sub
%attr(755,root,root) %{_datadir}/libtool/ltmain.sh

%{_infodir}/libtool.info*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
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

%files -n libltdl-static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
