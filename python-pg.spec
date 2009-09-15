%define sourcename PyGreSQL
%define version 3.7
%define release %mkrel 7

Summary: 	Postgresql support for Python
Name: 		python-pg
Version: 	%{version}
Release: 	%{release}
Source0: 	ftp://ftp.druid.net/pub/distrib/%{sourcename}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://www.druid.net/pygresql/
BuildRequires:	postgresql-devel python-devel
Provides:	python-postgresql = %{version}-%{release}
Provides:	%{sourcename} = %{version}-%{release}

%description
PostgreSQL is a database system derived from Postgres4.2. It conforms to 
(most of) aNSI SQL and offers many interesting capabilities (C dynamic 
linking for functions or type definition, etc.). 

Python is an interpreted programming language. It is object oriented, 
simple to use (light syntax, simple and straightforward statements), 
and has many extensions for building GUIs, interfacing with WWW, etc. 

PyGreSQL is a python module that interfaces to a PostgreSQL database. It 
embeds the PostgreSQL query library to allow easy use of the powerful 
PostgreSQL features from a Python script. 

%prep
%setup -q -n %{sourcename}-%version

%build
env CFLAGS="$RPM_OPT_FLAGS -I %{_includedir}/pgsql/server" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc Announce ChangeLog 
%defattr(755,root,root)
%doc tutorial/

