Summary:	Program for scientifical and technical computations, compatible with Matlab
Summary(pl):	Program do obliczeñ naukowo-in¿ynierskich, zgodny ze s³ynnym Matlabem
Summary(pt_BR):	Linguagem de alto-nível para computação numérica
Name:		scilab
Version:	2.7
Release:	4
License:	distributable
Group:		Applications/Math
Source0:	ftp://ftp.inria.fr/INRIA/Projects/Meta2/Scilab/distributions/%{name}-%{version}.src.tar.gz
# Source0-md5:	e8aa1ede5efa20eeced284963d08bebb
Source1:	%{name}.desktop
Patch0:		%{name}-configure.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-sh5.patch
URL:		http://www-rocq.inria.fr/scilab/
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	autoconf
BuildRequires:	gcc-g77
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for scientifical and technical computations, compatible with
Matlab.

%description -l pl
Program do obliczeñ naukowo-in¿ynierskich, zgodny ze s³ynnym Matlabem.

%description -l pt_BR
Linguagem de alto-nível para computação numérica.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure \
	--disable-static \
	--enable-shared \
	--with-tk \
	--with-xawd3d
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version}} \
	$RPM_BUILD_ROOT{%{_examplesdir}/scilab,%{_libdir}/X11/app-defaults} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin \
	$RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	X11BASE=$RPM_BUILD_ROOT%{_prefix} \
	BSD_INSTALL_DATA=/usr/bin/install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics/%{name}.desktop
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/{X11_defaults,contrib,demos,macros,man,maple,routines,tcl,.binary,scilab*} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

ln -fs %{_datadir}/%{name}-%{version}/contrib $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/contrib
ln -fs %{_datadir}/%{name}-%{version}/demos $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/demos
ln -fs %{_datadir}/%{name}-%{version}/macros $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/macros
ln -fs %{_datadir}/%{name}-%{version}/man $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/man
ln -fs %{_datadir}/%{name}-%{version}/maple $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/maple
ln -fs %{_datadir}/%{name}-%{version}/routines $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/routines
ln -fs %{_datadir}/%{name}-%{version}/scilab.star $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/scilab.star
ln -fs %{_datadir}/%{name}-%{version}/scilab.quit $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/scilab.quit
ln -fs %{_datadir}/%{name}-%{version}/tcl $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/tcl
ln -fs %{_datadir}/%{name}-%{version}/X11_defaults $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/X11_defaults

find $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin -type f | xargs perl -pi -e "s#$RPM_BUILD_ROOT##g"
perl -pi -e 's#PVM_ROOT=\$SCI/pvm3#PVM_ROOT=%{_libdir}/%{name}-%{version}/pvm3#g' \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin/scilab

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/macros -name Makefile\* -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS license.txt README_Unix
%attr(755,root,root) %{_bindir}/scilab
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/bin
%dir %{_libdir}/%{name}-%{version}/pvm3
%{_libdir}/%{name}-%{version}/bin/.scicos_pal
%{_libdir}/%{name}-%{version}/bin/Blatdoc
%{_libdir}/%{name}-%{version}/bin/Blatdocs
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/BEpsf
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/Blatexpr*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/Blpr
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/S*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/[a-z]*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/pvm3/*
%{_libdir}/%{name}-%{version}/contrib
%{_libdir}/%{name}-%{version}/demos
%{_libdir}/%{name}-%{version}/macros
%{_libdir}/%{name}-%{version}/man
%{_libdir}/%{name}-%{version}/maple
%{_libdir}/%{name}-%{version}/routines
%{_libdir}/%{name}-%{version}/scilab.quit
%{_libdir}/%{name}-%{version}/scilab.star
%dir %{_libdir}/%{name}-%{version}/tcl
%{_libdir}/%{name}-%{version}/X11_defaults
%{_datadir}/%{name}-%{version}/X11_defaults
%{_datadir}/%{name}-%{version}/contrib
%{_datadir}/%{name}-%{version}/demos
%dir %{_datadir}/%{name}-%{version}/macros
%{_datadir}/%{name}-%{version}/macros/[a-z]*
%{_datadir}/%{name}-%{version}/macros/*.c
%{_datadir}/%{name}-%{version}/man
%{_datadir}/%{name}-%{version}/maple
%{_datadir}/%{name}-%{version}/routines
%attr(755,root,root) %{_datadir}/%{name}-%{version}/tcl/browsehelpexe
%{_datadir}/%{name}-%{version}/tcl/*.*
%{_datadir}/%{name}-%{version}/tcl/Makefile
%{_datadir}/%{name}-%{version}/tcl/words
%{_datadir}/%{name}-%{version}/.binary
%{_datadir}/%{name}-%{version}/scilab*
%{_examplesdir}/scilab
%{_applnkdir}/Scientific/Numerics/*
