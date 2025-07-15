# TODO:
# - many things to check, more to do
# - added bcond with atlas
# - make demos works (doesn't see SCI path)
# - use system pvm
# - amd64 version(problem with -fPIC)
# - find xorg* BRs
#
# Conditional build:
%bcond_with	gtk2		# with gtk2
%bcond_with	xawd3d		# with xawd3d
%bcond_with	x		# with x
%bcond_with	f2c		# with f2c
%bcond_without	pvm		# without pvm
%bcond_without	ocaml		# without ocaml

Summary:	Program for scientifical and technical computations, compatible with Matlab
Summary(pl.UTF-8):	Program do obliczeń naukowo-inżynierskich, zgodny ze słynnym Matlabem
Summary(pt_BR.UTF-8):	Linguagem de alto-nível para computação numérica
Name:		scilab
Version:	4.1.1
Release:	0.1
License:	distributable
Group:		Applications/Math
Source0:        http://www.scilab.org/download/%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	0b603c8e40334d0be97eb4ac104926bf
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-sh5.patch
Patch2:		%{name}-lib64.patch
Patch3:		%{name}-docbasedir.patch
Patch4:		%{name}-cflags.patch
URL:		http://www.scilab.org/
BuildRequires:	xorg-lib-libX11-devel
%{?with_xawd3d:BuildRequires:	Xaw3d-devel}
%{?with_f2c:BuildRequires:	f2c}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-fortran
BuildRequires:	libgtkhtml-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libzvt-devel >= 2.0
BuildRequires:	ncurses-devel
%{?with_ocaml:BuildRequires:	ocaml}
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
%{?with_pvm:BuildRequires:	pvm-devel}
BuildRequires:	readline-devel
BuildRequires:	sablotron
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	vte-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults
%define		_noautocompressdoc *.xml *.xsl *hh? *dtd

%description
Program for scientifical and technical computations, compatible with
Matlab.

%description -l pl.UTF-8
Program do obliczeń naukowo-inżynierskich, zgodny ze słynnym Matlabem.

%description -l pt_BR.UTF-8
Linguagem de alto-nível para computação numérica.

%package doc
Summary:	Scilab documentation
Summary(pl.UTF-8):	Dokumantacja dla scilab
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation and demos for scilab.

%description doc -l pl.UTF-8
Dokumentacja i pliki demo dla scilab.

%package examples
Summary:	Scilab examples
Summary(pl.UTF-8):	Przykłady dla scilab
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}

%description examples
Examples and demos for scilab.

%description examples -l pl.UTF-8
Przykłady i pliki demo dla scilab.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%if %{_lib} == "lib64"
    %patch2 -p1
%endif
#%patch3 -p1
%patch -P4 -p0

head -n 438 aclocal.m4 > acinclude.m4
tail -n 68 aclocal.m4 >>acinclude.m4
sed -e 's@-march=athlon64@@g' -i configure.in
sed -e 's@$PVMROOT/lib/pvmgetarch@%{_bindir}/pvmgetarch@g' -i configure.in

%build
#cp -f /usr/share/automake/config.sub config
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
%configure \
	--enable-shared \
	--with-tcl-library=%{_libdir} \
	--with-tcl-include=%{_includedir} \
	--with-tk-library=%{_libdir} \
	--with-tk-include=%{_includedir} \
	--without-java \
	--with-pvm-include=%{_includedir} \
	--with-pvm-library=%{_libdir} \
	%{?with_gtk2:--with-gtk2} \
	%{?with_xawd3d:--with-xawd3d} \
	%{?with_x:--with-x} \
	%{?with_f2c:--with-f2c} \
	%{!?with_pvm:--without-pvm} \
	%{!?with_ocaml:--without-ocaml}

%{__make} -j1 all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version}} \
	$RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_appdefsdir}} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	X11BASE=$RPM_BUILD_ROOT%{_prefix} \
	SCIDIR=$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version} \
	BSD_INSTALL_DATA=%{_bindir}/install

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/{X11_defaults,contrib,demos,macros,man,maple,routines,tcl,.binary,scilab*} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

ln -fs %{_datadir}/%{name}-%{version}/contrib $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/contrib
ln -fs %{_datadir}/%{name}-%{version}/demos $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/demos
ln -fs %{_datadir}/%{name}-%{version}/macros $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/macros
ln -fs %{_docdir}/%{name}-doc-%{version} $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/man
ln -fs %{_datadir}/%{name}-%{version}/maple $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/maple
ln -fs %{_datadir}/%{name}-%{version}/routines $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/routines
ln -fs %{_datadir}/%{name}-%{version}/scilab.star $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/scilab.star
ln -fs %{_datadir}/%{name}-%{version}/scilab.quit $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/scilab.quit
ln -fs %{_datadir}/%{name}-%{version}/tcl $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/tcl
ln -fs %{_datadir}/%{name}-%{version}/X11_defaults $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/X11_defaults

# fix links
ln -fs %{_libdir}/%{name}-%{version}/bin/{%{name},intersci,intersci-n} $RPM_BUILD_ROOT%{_bindir}/

find $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin -type f | xargs perl -pi -e "s#$RPM_BUILD_ROOT##g"
perl -pi -e 's#PVM_ROOT=\$SCI/pvm3#PVM_ROOT=%{_libdir}/%{name}-%{version}/pvm3#g' \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin/scilab

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/macros -name Makefile\* -exec rm -f {} \;
find $RPM_BUILD_ROOT -name .cvsignore -exec rm -f {} \;
find man -name .cvsignore -exec rm -f {} \;

mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/examples/ $RPM_BUILD_ROOT%{_examplesdir}/%{name}

#Clean if not packing
#rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS license.txt README_Unix CHANGES
%lang(fr) %doc licence.txt

%attr(755,root,root) %{_bindir}/scilab

%dir %{_libdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/%{name}-%{version}/libtool

%dir %{_libdir}/%{name}-%{version}/bin
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/BEpsf
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/Blatexpr*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/Blpr
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/S*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/[a-z]*
%{_libdir}/%{name}-%{version}/bin/.scicos_pal
%{_libdir}/%{name}-%{version}/bin/Blatdoc
%{_libdir}/%{name}-%{version}/bin/Blatdocs

%{?with_pvm:%dir %{_libdir}/%{name}-%{version}/pvm3}
%{?with_pvm:%attr(755,root,root) %{_libdir}/%{name}-%{version}/pvm3/*}

### links
%{_libdir}/%{name}-%{version}/imp
%dir %{_libdir}/%{name}-%{version}/macros
%{_libdir}/%{name}-%{version}/man
%{_libdir}/%{name}-%{version}/maple
%{_libdir}/%{name}-%{version}/routines
%{_libdir}/%{name}-%{version}/scilab.quit
%{_libdir}/%{name}-%{version}/scilab.star
%{_libdir}/%{name}-%{version}/util

%dir %{_libdir}/%{name}-%{version}/scripts
%attr(755,root,root) %{_libdir}/%{name}-%{version}/scripts/B*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/scripts/sc*

%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/X11_defaults
%{_datadir}/%{name}-%{version}/contrib
%{_datadir}/%{name}-%{version}/macros
%{_datadir}/%{name}-%{version}/maple
%{_datadir}/%{name}-%{version}/routines
%{_datadir}/%{name}-%{version}/scilab.*

%dir %{_datadir}/%{name}-%{version}/tcl
%attr(755,root,root) %{_datadir}/%{name}-%{version}/tcl/browsehelpexe
%{_datadir}/%{name}-%{version}/tcl/*.*
%{_datadir}/%{name}-%{version}/tcl/Makefile
%{_datadir}/%{name}-%{version}/tcl/ged
%{_datadir}/%{name}-%{version}/tcl/sciGUI
%{_datadir}/%{name}-%{version}/tcl/scipadsources
%{_datadir}/%{name}-%{version}/tcl/utils
%{_datadir}/%{name}-%{version}/tcl/browsehelp
%{_datadir}/%{name}-%{version}/demos
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}.png

%files doc
%defattr(644,root,root,755)
%lang(fr) %doc %{_datadir}/%{name}-%{version}/man/fr
%lang(en) %doc %{_datadir}/%{name}-%{version}/man/eng
%doc %{_datadir}/%{name}-%{version}/man/images
%doc %{_datadir}/%{name}-%{version}/man/BuildChm
%doc %{_datadir}/%{name}-%{version}/man/*.dtd
%doc %{_datadir}/%{name}-%{version}/man/CheckHelp
#%%{_libdir}/%{name}-%{version}/config

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
