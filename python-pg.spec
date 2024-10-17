%define sourcename PyGreSQL
%define version 3.7
%define release 8

Summary: 	Postgresql support for Python
Name: 		python-pg
Version: 	%{version}
Release: 	%{release}
Source0: 	ftp://ftp.druid.net/pub/distrib/%{sourcename}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		https://www.druid.net/pygresql/
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

%files
%defattr(644,root,root,755)
%doc Announce ChangeLog 
%defattr(755,root,root)
%doc tutorial/
%py_platsitedir/*


%changelog
* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 3.7-7mdv2011.0
+ Revision: 599417
- update file list

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 3.7-7mdv2010.0
+ Revision: 442372
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 3.7-6mdv2009.1
+ Revision: 320186
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 3.7-5mdv2009.0
+ Revision: 259741
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 3.7-4mdv2009.0
+ Revision: 247586
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.7-2mdv2008.1
+ Revision: 136456
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 21 2007 Emmanuel Andry <eandry@mandriva.org> 3.7-2mdv2008.0
+ Revision: 16576
- rebuild for libpq (bug #30366)


* Thu Sep 08 2005 Buchan Milne <bgmilne@linux-mandrake.com> 3.7-1mdk
- New release 3.7

* Tue Jun 21 2005 Buchan Milne <bgmilne@linux-mandrake.com> 3.6.2-1mdk
- New release 3.6.2
- rpmbuildupdate-able and %%mkrel-ed (drop pre version handling as 
  rpmbuildupdate does not seem capable of handling it)

* Wed Apr 20 2005 Oden Eriksson <oeriksson@mandriva.com> 3.4-3mdk
- rebuilt against new postgresql libs

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 3.4-2mdk
- Rebuild for new python

* Tue Apr 06 2004 Buchan Milne <bgmilne@linux-mandrake.com> 3.4-1mdk
- First Mandrake package

