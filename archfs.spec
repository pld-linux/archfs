#
%define		_ver	%(echo %{version}|tr -d b)	
#
Summary:	Userspace filesystem based on rdiff-backup repository data
Summary(pl.UTF-8):	System plików w przestrzeni użytkownika wykorzystujący rdiff-backup
Name:		archfs
Version:	0.5.6b
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://archfs.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4f4e57d17c07f97fd7beb99dd1a46e2c
Source1:	%{name}.1
# Source1-md5:	3b00bae0666c498ce06adc1b30534973
URL:		http://code.google.com/p/archfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel
BuildRequires:	libtool
Requires:	rdiff-backup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archfs - userspace filesystem based on rdiff-backup repository data.

%description -l pl.UTF-8
Archfs - system plików w przestrzeni użytkownika reprezentujący dane z
kopii zapasowej wykonanej przy pomocy rdiff-backup.

%prep
%setup -q -n %{name}-%{_ver}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
