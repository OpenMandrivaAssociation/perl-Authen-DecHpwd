%define upstream_name    Authen-DecHpwd
%define upstream_version 2.006

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    DEC VMS password hashing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Data::Integer)
BuildRequires: perl(Digest::CRC)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Scalar::String)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements the 'LGI$HPWD' password hashing function from VMS,
and some associated VMS username and password handling functions.

The password hashing function is implemented in XS, with a hideously slow
pure Perl backup version for systems that can't handle XS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


