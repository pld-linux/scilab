
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/Scilab-3.0-RC1} \
	$RPM_BUILD_ROOT{%{_examplesdir}/scilab,%{_libdir}/X11/app-defaults} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin \
	$RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	X11BASE=$RPM_BUILD_ROOT%{_prefix} \
	BSD_INSTALL_DATA=/usr/bin/install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics/%{name}.desktop
mv -f $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/{X11_defaults,contrib,demos,macros,man,maple,routines,tcl,.binary,scilab*} \
	$RPM_BUILD_ROOT%{_datadir}/Scilab-3.0-RC1

ln -fs %{_datadir}/Scilab-3.0-RC1/contrib $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/contrib
ln -fs %{_datadir}/Scilab-3.0-RC1/demos $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/demos
ln -fs %{_datadir}/Scilab-3.0-RC1/macros $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/macros
ln -fs %{_datadir}/Scilab-3.0-RC1/man $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/man
ln -fs %{_datadir}/Scilab-3.0-RC1/maple $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/maple
ln -fs %{_datadir}/Scilab-3.0-RC1/routines $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/routines
ln -fs %{_datadir}/Scilab-3.0-RC1/scilab.star $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/scilab.star
ln -fs %{_datadir}/Scilab-3.0-RC1/scilab.quit $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/scilab.quit
ln -fs %{_datadir}/Scilab-3.0-RC1/tcl $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/tcl
ln -fs %{_datadir}/Scilab-3.0-RC1/X11_defaults $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/X11_defaults

find $RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/bin -type f | xargs perl -pi -e "s#$RPM_BUILD_ROOT##g"
perl -pi -e 's#PVM_ROOT=\$SCI/pvm3#PVM_ROOT=%{_libdir}/Scilab-3.0-RC1/pvm3#g' \
	$RPM_BUILD_ROOT%{_libdir}/Scilab-3.0-RC1/bin/scilab

find $RPM_BUILD_ROOT%{_datadir}/Scilab-3.0-RC1/macros -name Makefile\* -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS license.txt README_Unix
%attr(755,root,root) %{_bindir}/scilab
%dir %{_libdir}/Scilab-3.0-RC1
%dir %{_libdir}/Scilab-3.0-RC1/bin
%dir %{_libdir}/Scilab-3.0-RC1/pvm3
%{_libdir}/Scilab-3.0-RC1/bin/.scicos_pal
%{_libdir}/Scilab-3.0-RC1/bin/Blatdoc
%{_libdir}/Scilab-3.0-RC1/bin/Blatdocs
%attr(755,root,root) %{_libdir}/Scilab-3.0-RC1/bin/BEpsf
%attr(755,root,root) %{_libdir}/Scilab-3.0-RC1/bin/Blatexpr*
%attr(755,root,root) %{_libdir}/Scilab-3.0-RC1/bin/Blpr
%attr(755,root,root) %{_libdir}/Scilab-3.0-RC1/bin/S*
%attr(755,root,root) %{_libdir}/Scilab-3.0-RC1/bin/[a-z]*
%attr(755,root,root) %{_libdir}/Scilab-3.0-RC1/pvm3/*
%{_libdir}/Scilab-3.0-RC1/contrib
%{_libdir}/Scilab-3.0-RC1/demos
%{_libdir}/Scilab-3.0-RC1/macros
%{_libdir}/Scilab-3.0-RC1/man
%{_libdir}/Scilab-3.0-RC1/maple
%{_libdir}/Scilab-3.0-RC1/routines
%{_libdir}/Scilab-3.0-RC1/scilab.quit
%{_libdir}/Scilab-3.0-RC1/scilab.star
%dir %{_libdir}/Scilab-3.0-RC1/tcl
%{_libdir}/Scilab-3.0-RC1/X11_defaults
%{_datadir}/Scilab-3.0-RC1/X11_defaults
%{_datadir}/Scilab-3.0-RC1/contrib
%{_datadir}/Scilab-3.0-RC1/demos
%dir %{_datadir}/Scilab-3.0-RC1/macros
%{_datadir}/Scilab-3.0-RC1/macros/[a-z]*
%{_datadir}/Scilab-3.0-RC1/macros/*.c
%{_datadir}/Scilab-3.0-RC1/man
%{_datadir}/Scilab-3.0-RC1/maple
%{_datadir}/Scilab-3.0-RC1/routines
%attr(755,root,root) %{_datadir}/Scilab-3.0-RC1/tcl/browsehelpexe
%{_datadir}/Scilab-3.0-RC1/tcl/*.*
%{_datadir}/Scilab-3.0-RC1/tcl/Makefile
%{_datadir}/Scilab-3.0-RC1/tcl/words
%{_datadir}/Scilab-3.0-RC1/.binary
%{_datadir}/Scilab-3.0-RC1/scilab*
%{_examplesdir}/scilab
%{_applnkdir}/Scientific/Numerics/*
