%define base_name	brice2nice
%define name		fortune-%{base_name}
%define version		0.2
%define release		%mkrel 5

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

