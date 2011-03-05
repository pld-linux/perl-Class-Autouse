#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Autouse
Summary:	Class::Autouse - defer loading of one or more classes
Summary(pl.UTF-8):	Class::Autouse - wstrzymanie ładowania jednej lub więcej klas
Name:		perl-Class-Autouse
Version:	2.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/ADAMK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	84fbbad122191cb046ea5d96b2d51ac3
URL:		http://search.cpan.org/dist/Class-Autouse/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-File-Temp >= 0.17
BuildRequires:	perl-Scalar-List-Utils >= 1.19
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Autouse allows you to specify a class the will only load when a
method of that class is called. For large classes that might not be
used during the running of a program, such as Date::Manip, this can
save you large amounts of memory, and decrease the script load time.

%description -l pl.UTF-8
Class::Autouse pozwala na wskazanie klas, które będą załadowane tylko
wtedy, gdy metoda danej klasy zostanie wywołana. Dla dużych klas,
takich jak Date::Manip, które mogą być nieużywane podczas działania
programu, w ten sposób możliwe jest zaoszczędzenie dużej ilości
pamięci oraz zmniejszenie czasu ładowania skryptu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL --skipdeps \
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
%{perl_vendorlib}/Class/Autouse.pm
%{perl_vendorlib}/Class/Autouse
%{_mandir}/man3/Class::Autouse.3pm*
