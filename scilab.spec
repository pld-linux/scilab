Summary:	Scilab
Name:		scilab
Version:	2.5
Release:	1
Copyright:	distributable
Group:		Applications/Math
Source:		ftp://ftp.inria.fr/INRIA/Projects/Meta2/Scilab/distributions/%{name}-%{version}.src.tar.gz
Patch0:		scilab-configure.patch
BuildRequires:	gcc-g77
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Scilab

%prep
%setup -q
%patch0 -p1 

%build
autoconf
%configure \
	--disable-static \
	--enable-shared \
	--with-tk
%{__make} all

%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version}}
install -d $RPM_BUILD_ROOT{%{_examplesdir}/scilab,/usr/X11R6/lib/X11/app-defaults,%{_libdir}/%{name}-%{version}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	X11BASE=$RPM_BUILD_ROOT/usr/X11R6 \
	BSD_INSTALL_DATA=/usr/bin/install

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/{bin,pvm3} $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}
mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples/* $RPM_BUILD_ROOT%{_examplesdir}/scilab
mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/Makefile.incl $RPM_BUILD_ROOT%{_examplesdir}/scilab
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin/dold
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin/xless
install bin/xless $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin/xless

rm -f $RPM_BUILD_ROOT%{_bindir}/scilab
ln -sf ../lib/%{name}-%{version}/bin/scilab $RPM_BUILD_ROOT%{_bindir}/scilab
ln -sf ../../lib/%{name}-%{version}/bin $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin

find $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin -type f | xargs perl -pi -e "s#$RPM_BUILD_ROOT##g"
perl -pi -e 's#PVM_ROOT=\$SCI/pvm3#PVM_ROOT=%{_libdir}/%{name}-%{version}/pvm3#g' \
	$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin/scilab

find $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/macros -name Makefile\* -exec rm -f {} \;

gzip -9nf doc/*.ps notice.{tex,ps}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.ps.gz notice*.gz
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
%{_datadir}/%{name}-%{version}/X11_defaults
%{_datadir}/%{name}-%{version}/bin
%{_datadir}/%{name}-%{version}/contrib
%{_datadir}/%{name}-%{version}/demos
%dir %{_datadir}/%{name}-%{version}/macros
%{_datadir}/%{name}-%{version}/macros/[a-z]*
%{_datadir}/%{name}-%{version}/macros/*.c
#%attr(755,root,root) %{_datadir}/%{name}-%{version}/macros/[A-Z][a-z]
%{_datadir}/%{name}-%{version}/man
%{_datadir}/%{name}-%{version}/maple
%{_datadir}/%{name}-%{version}/routines
%{_datadir}/%{name}-%{version}/tcl
%{_datadir}/%{name}-%{version}/.binary
%{_datadir}/%{name}-%{version}/scilab*
/usr/X11R6/lib/X11/app-defaults/*
%{_examplesdir}/scilab
