Summary:	Scilab
Name:		scilab
Version:	2.5
Release:	0.1
Copyright:	distributable
Group:		Applications/Math
Source:		ftp://ftp.inria.fr/INRIA/Projects/Meta2/Scilab/distributions/%{name}-%{version}.src.tar.gz
Patch0:		scilab-configure.patch
BuildRequires:	gcc-g77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scilab

%prep
%setup -q
%patch0 -p1 

%build
autoconf
%configure --with-tk
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version},/usr/X11R6/lib/X11/app-defaults}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	X11BASE=$RPM_BUILD_ROOT/usr/X11R6 \
	BSD_INSTALL_DATA=/usr/bin/install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
