%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	BBCodeParser
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - parser to replace UBB style tags with their HTML equivalents
Summary(pl.UTF-8):	%{_pearname} - parser zastępujący tagi typu UBB ich odpowiednikami HTML
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8cb028b0ae71a63bd60f432a08546e43
URL:		http://pear.php.net/package/HTML_BBCodeParser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a parser to replace UBB style tags with their HTML
equivalents. It does not simply do some regex calls, but is complete
stack based parse engine. This ensures that all tags are properly
nested, if not, extra tags are added to maintain the nesting. This
parser should only produce XHTML 1.0 compliant code. All tags are
validated and so are all their attributes. It should be easy to extend
this parser with your own tags.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Jest to parser zastępujący tagi typu UBB ich odpowiednikami HTML. Nie
jest to jednak to tylko wywołanie kilku wyrażeń regularnych, ale
kompletny silnik parsujący. Dzięki temu pewne jest, iż wszystkie tagi
będą poprawnie zagnieżdżone, a jeśli nie, dodatkowy tag zostanie
dodany w celu zachowania zagnieżdżenia. Ten parser powinien
wyprodukować kod zgodny z XHTML 1.0. Wszystkie tagi oraz ich atrybuty
sprawdzane są pod kątem poprawności. Możliwe jest rozszerzenie parsera
o własne tagi.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
