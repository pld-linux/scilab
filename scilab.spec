# TODO:
# - added bcond with atlas
#
Summary:	Program for scientifical and technical computations, compatible with Matlab
Summary(pl):	Program do obliczeñ naukowo-in¿ynierskich, zgodny ze s³ynnym Matlabem
Summary(pt_BR):	Linguagem de alto-nível para computação numérica
Name:		scilab
Version:	3.0
Release:	3.2
License:	distributable
Group:		Applications/Math
Source0:	ftp://ftp.inria.fr/INRIA/Scilab/distributions/%{name}-%{version}.src.tar.gz
# Source0-md5:	d6fc5fe12519f99ccdd492c4ba96935a
Source1:	%{name}.desktop
Patch0:		%{name}-configure.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-sh5.patch
Patch3:		%{name}-amd64.patch
URL:		http://www-rocq.inria.fr/scilab/
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	libgtkhtml-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libzvt-devel >= 2.0
BuildRequires:	ncurses-devel
BuildRequires:	sablotron
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Program for scientifical and technical computations, compatible with
Matlab.

%description -l pl
Program do obliczeñ naukowo-in¿ynierskich, zgodny ze s³ynnym Matlabem.

%description -l pt_BR
Linguagem de alto-nível para computação numérica.

%package doc
Summary:	Scilab documentation
Summary(pl):	Dokumantacja dla scilab
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation and demos for scilab.

%description -l pl doc
Dokumentacja i pliki demo dla scilab.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# kill precompiled x86 objects
rm -f examples/mex-examples/mexglx/{xtimesy.mexglx,*.so}

head -n 424 aclocal.m4 > acinclude.m4

%build
cp -f /usr/share/automake/config.sub config
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-static \
	--enable-shared \
	--with-tcl-library=%{_libdir} \
	--with-tk \
	--with-tk-library=%{_libdir} \
	--with-xawd3d \
	--with-gtk2
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version}} \
	$RPM_BUILD_ROOT{%{_examplesdir}/scilab,%{_appdefsdir}} \
	$RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/bin \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	X11BASE=$RPM_BUILD_ROOT%{_prefix} \
	BSD_INSTALL_DATA=/usr/bin/install

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
mv -f $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/{X11_defaults,contrib,demos,macros,man,maple,routines,tcl,.binary,scilab*} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

ln -fs %{_datadir}/%{name}-%{version}/contrib $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/contrib
ln -fs %{_datadir}/%{name}-%{version}/demos $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/demos
ln -fs %{_datadir}/%{name}-%{version}/macros $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/macros
ln -fs %{_datadir}/%{name}-%{version}/man $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/man
ln -fs %{_datadir}/%{name}-%{version}/maple $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/maple
ln -fs %{_datadir}/%{name}-%{version}/routines $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/routines
ln -fs %{_datadir}/%{name}-%{version}/scilab.star $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/scilab.star
ln -fs %{_datadir}/%{name}-%{version}/scilab.quit $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/scilab.quit
ln -fs %{_datadir}/%{name}-%{version}/tcl $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/tcl
ln -fs %{_datadir}/%{name}-%{version}/X11_defaults $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/X11_defaults

find $RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/bin -type f | xargs perl -pi -e "s#$RPM_BUILD_ROOT##g"
perl -pi -e 's#PVM_ROOT=\$SCI/pvm3#PVM_ROOT=%{_libdir}/%{name}-%{version}/pvm3#g' \
	$RPM_BUILD_ROOT%{_prefix}/lib/%{name}-%{version}/bin/scilab

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/macros -name Makefile\* -exec rm -f {} \;

mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/examples/ $RPM_BUILD_ROOT%{_examplesdir}/scilab

#Clean if not packing
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS license.txt README_Unix CHANGES
%attr(755,root,root) %{_bindir}/scilab
%dir %{_prefix}/lib/%{name}-%{version}
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/libtool
%dir %{_prefix}/lib/%{name}-%{version}/bin
%dir %{_prefix}/lib/%{name}-%{version}/pvm3
%{_prefix}/lib/%{name}-%{version}/bin/.scicos_pal
%{_prefix}/lib/%{name}-%{version}/bin/Blatdoc
%{_prefix}/lib/%{name}-%{version}/bin/Blatdocs
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/bin/BEpsf
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/bin/Blatexpr*
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/bin/Blpr
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/bin/S*
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/bin/[a-z]*
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/pvm3/*
%{_prefix}/lib/%{name}-%{version}/contrib
%{_prefix}/lib/%{name}-%{version}/imp
%{_prefix}/lib/%{name}-%{version}/macros
%{_prefix}/lib/%{name}-%{version}/man
%{_prefix}/lib/%{name}-%{version}/maple
%{_prefix}/lib/%{name}-%{version}/routines
%{_prefix}/lib/%{name}-%{version}/scilab.quit
%{_prefix}/lib/%{name}-%{version}/scilab.star
%dir %{_prefix}/lib/%{name}-%{version}/tcl
%{_prefix}/lib/%{name}-%{version}/X11_defaults
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/X11_defaults
%{_datadir}/%{name}-%{version}/contrib
%{_datadir}/%{name}-%{version}/demos
%dir %{_datadir}/%{name}-%{version}/macros
%{_datadir}/%{name}-%{version}/macros/[a-z]*
%{_datadir}/%{name}-%{version}/macros/*.c
%{_datadir}/%{name}-%{version}/maple
%{_datadir}/%{name}-%{version}/routines
%dir %{_datadir}/%{name}-%{version}/tcl
#it's binary file
%attr(755,root,root) %{_datadir}/%{name}-%{version}/tcl/browsehelpexe

%{_datadir}/%{name}-%{version}/tcl/*.*
%{_datadir}/%{name}-%{version}/tcl/Makefile
%{_datadir}/%{name}-%{version}/tcl/ged
%{_datadir}/%{name}-%{version}/tcl/sciGUI
%{_datadir}/%{name}-%{version}/tcl/scipadsources
%{_datadir}/%{name}-%{version}/tcl/utils
%{_datadir}/%{name}-%{version}/tcl/words
%{_datadir}/%{name}-%{version}/.binary
%{_datadir}/%{name}-%{version}/scilab*
%dir %{_prefix}/lib/%{name}-%{version}/scripts
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/scripts/B*
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/scripts/sc*
%{_prefix}/lib/%{name}-%{version}/util
%{_desktopdir}/*

%files doc
%defattr(644,root,root,755)
%lang(fr) %doc man/fr
%doc man/eng man/*.dtd
%{_examplesdir}/scilab
%{_prefix}/lib/%{name}-%{version}/demos
%{_prefix}/lib/%{name}-%{version}/tests
%attr(755,root,root) %{_prefix}/lib/%{name}-%{version}/tests/*.sh
