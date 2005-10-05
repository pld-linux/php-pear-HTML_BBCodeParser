%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	BBCodeParser
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - parser to replace UBB style tags with their HTML equivalents
Summary(pl):	%{_pearname} - parser zastêpuj±cy tagi typu UBB ich odpowiednikami HTML
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0baca616b569dff6966ff6422b5ecdc4
URL:		http://pear.php.net/package/HTML_BBCodeParser/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Jest to parser zastêpuj±cy tagi typu UBB ich odpowiednikami HTML. Nie
jest to jednak to tylko wywo³anie kilku wyra¿eñ regularnych, ale
kompletny silnik parsuj±cy. Dziêki temu pewne jest, i¿ wszystkie tagi
bêd± poprawnie zagnie¿d¿one, a je¶li nie, dodatkowy tag zostanie
dodany w celu zachowania zagnie¿d¿enia. Ten parser powinien
wyprodukowaæ kod zgodny z XHTML 1.0. Wszystkie tagi oraz ich atrybuty
sprawdzane s± pod k±tem poprawno¶ci. Mo¿liwe jest rozszerzenie parsera
o w³asne tagi.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/HTML/BBCodeParser/example docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/example
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
