%define upstream_name Authen-DecHpwd
%define upstream_version 2.006

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	DEC VMS password hashing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Data::Integer)
BuildRequires:	perl(Digest::CRC)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Scalar::String)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module implements the 'LGI$HPWD' password hashing function from VMS,
and some associated VMS username and password handling functions.

The password hashing function is implemented in XS, with a hideously slow
pure Perl backup version for systems that can't handle XS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.6.0-2
+ Revision: 773603
- clean out spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-1
+ Revision: 674707
- new version

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 2.5.0-1mdv2011.0
+ Revision: 573788
- import perl-Authen-DecHpwd

