#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Autouse
Summary:	Class::Autouse - defer loading of one or more classes
Summary(pl):	Class::Autouse - wstrzymanie ³adowania jednej lub wiêcej klas
Name:		perl-Class-Autouse
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ed8ab9529ac496576c65f3e8f315ebb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(List::Util) >= 1.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Autouse allows you to specify a class the will only load when a
method of that class is called. For large classes that might not be
used during the running of a program, such as Date::Manip, this can
save you large amounts of memory, and decrease the script load time.

%description -l pl
Class::Autouse pozwala na wskazanie klas, które bêd± za³adowane tylko
wtedy, gdy metoda danej klasy zostanie wywo³ana. Dla du¿ych klas,
takich jak Date::Manip, które mog± byæ nieu¿ywane podczas dzia³ania
programu, w ten sposób mo¿liwe jest zaoszczêdzenie du¿ej ilo¶ci
pamiêci oraz zmniejszenie czasu ³adowania skryptu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/*.pm
%{perl_vendorlib}/Class/Autouse
%{_mandir}/man3/*
