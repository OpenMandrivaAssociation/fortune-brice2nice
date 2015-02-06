%define base_name	brice2nice
%define name		fortune-%{base_name}
%define version		0.2
%define release		8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Brice de nice sketches
License:	Public Domain
Group:		Toys
Source:		%{name}.tar.bz2
Url:		http://www.tom.free.fr/src/brice2nice
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot
Requires:	fortune-mod

BuildRequires: fortune-mod

%description
The "Brice de nice" sketches.
Special Thanks to the mandrakefr community during RMLL2004
where "Brice de Nice" was inside all our discussions.

%prep
%setup -q -n %{name} 

%build
%make clean
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_gamesdatadir}/fortunes/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-7mdv2011.0
+ Revision: 618331
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2010.0
+ Revision: 428869
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2009.0
+ Revision: 245325
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2008.1
+ Revision: 125188
- kill re-definition of %%buildroot on Pixel's request
- import fortune-brice2nice


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-3mdk
 - Buildrequires fix 

* Mon Jul 12 2004 Erwan Velu <erwan@mandrakesoft.com> 0.2-2mdk
- Fixing fu....ng monday mistakes (thx misc)*
- T'es cassé la !
* Mon Jul 12 2004 Erwan Velu <erwan@mandrakesoft.comg> 0.2-1mdk
- first Mandrake release
