
Summary:	Program for scientifical and technical computations, compatible with Matlab
Summary(pl):	Program do obliczeñ naukowo-in¿ynierskich, zgodny ze s³ynnym Matlabem
Summary(pt_BR):	Linguagem de alto-nível para computação numérica
Name:		scilab
Version:	3.0
Release:	0.RC1
License:	distributable
Group:		Applications/Math
Source0:	ftp://ftp.inria.fr/INRIA/Scilab/release_candidate/Scilab-%{version}-RC1.src.tar.gz
# Source0-md5:	698341a25b478649883278a830afab18
Source1:	%{name}.desktop
Patch1:         %{name}-DESTDIR.patch
Patch2:         %{name}-sh5.patch
URL:		http://www-rocq.inria.fr/scilab/
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	autoconf
BuildRequires:	gcc-g77
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRequires:	ncurses-devel
BuildRequires:	ocaml
BuildRequires:	gtk+2-devel
BuildRequires:	libzvt-devel
BuildRequires:	libgtkhtml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for scientifical and technical computations, compatible with
Matlab.

%description -l pl
Program do obliczeñ naukowo-in¿ynierskich, zgodny ze s³ynnym Matlabem.

%description -l pt_BR
Linguagem de alto-nível para computação numérica.

%prep
%setup -q -n Scilab-%{version}-RC1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure \
	--disable-static \
	--enable-shared \
	--with-gtk2 \
	--with-xawd3d \
	--with-x
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
ln -s . scilab-3.0
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/scilab-3.0} \
	$RPM_BUILD_ROOT{%{_examplesdir}/scilab,%{_libdir}/X11/app-defaults} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin \
	$RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics

cd scilab-3.0
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	X11BASE=$RPM_BUILD_ROOT%{_prefix} \
	BSD_INSTALL_DATA=/usr/bin/install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics/%{name}.desktop
mv -f $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/{X11_defaults,contrib,demos,macros,man,maple,routines,tcl,.binary,scilab*} \
	$RPM_BUILD_ROOT%{_datadir}/scilab-3.0

ln -fs %{_datadir}/scilab-3.0/contrib $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/contrib
ln -fs %{_datadir}/scilab-3.0/demos $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/demos
ln -fs %{_datadir}/scilab-3.0/macros $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/macros
ln -fs %{_datadir}/scilab-3.0/man $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/man
ln -fs %{_datadir}/scilab-3.0/maple $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/maple
ln -fs %{_datadir}/scilab-3.0/routines $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/routines
ln -fs %{_datadir}/scilab-3.0/scilab.star $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/scilab.star
ln -fs %{_datadir}/scilab-3.0/scilab.quit $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/scilab.quit
ln -fs %{_datadir}/scilab-3.0/tcl $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/tcl
ln -fs %{_datadir}/scilab-3.0/X11_defaults $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/X11_defaults

find $RPM_BUILD_ROOT%{_libdir}/scilab-3.0/bin -type f | xargs perl -pi -e "s#$RPM_BUILD_ROOT##g"
perl -pi -e 's#PVM_ROOT=\$SCI/pvm3#PVM_ROOT=%{_libdir}/scilab-3.0/pvm3#g' \
	$RPM_BUILD_ROOT%{_libdir}scilab-3.0/bin/scilab

find $RPM_BUILD_ROOT%{_datadir}/scilab-3.0/macros -name Makefile\* -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS license.txt README_Unix
%attr(755,root,root) %{_bindir}/scilab
%dir %{_libdir}/scilab-3.0
%dir %{_libdir}/scilab-3.0/bin
%dir %{_libdir}/scilab-3.0/pvm3
%{_libdir}/scilab-3.0/bin/.scicos_pal
%{_libdir}/scilab-3.0/bin/Blatdoc
%{_libdir}/scilab-3.0/bin/Blatdocs
%attr(755,root,root) %{_libdir}/scilab-3.0/bin/BEpsf
%attr(755,root,root) %{_libdir}/scilab-3.0/bin/Blatexpr*
%attr(755,root,root) %{_libdir}/scilab-3.0/bin/Blpr
%attr(755,root,root) %{_libdir}/scilab-3.0/bin/S*
%attr(755,root,root) %{_libdir}/scilab-3.0/bin/[a-z]*
%attr(755,root,root) %{_libdir}/scilab-3.0/pvm3/*
%{_libdir}/scilab-3.0/contrib
%{_libdir}/scilab-3.0/demos
%{_libdir}/scilab-3.0/macros
%{_libdir}/scilab-3.0/man
%{_libdir}/scilab-3.0/maple
%{_libdir}/scilab-3.0/routines
%{_libdir}/scilab-3.0/scilab.quit
%{_libdir}/scilab-3.0/scilab.star
%dir %{_libdir}/scilab-3.0/tcl
%{_libdir}/scilab-3.0/X11_defaults
%{_datadir}/scilab-3.0/X11_defaults
%{_datadir}/scilab-3.0/contrib
%{_datadir}/scilab-3.0/demos
%dir %{_datadir}/scilab-3.0/macros
%{_datadir}/scilab-3.0/macros/[a-z]*
%{_datadir}/scilab-3.0/macros/*.c
%{_datadir}/scilab-3.0/man
%{_datadir}/scilab-3.0/maple
%{_datadir}/scilab-3.0/routines
%attr(755,root,root) %{_datadir}/scilab-3.0/tcl/browsehelpexe
%{_datadir}/scilab-3.0/tcl/*.*
%{_datadir}/scilab-3.0/tcl/Makefile
%{_datadir}/scilab-3.0/tcl/words
%{_datadir}/scilab-3.0/.binary
%{_datadir}/scilab-3.0/scilab*
%{_examplesdir}/scilab
%{_applnkdir}/Scientific/Numerics/*
