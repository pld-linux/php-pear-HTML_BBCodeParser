%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       BBCodeParser
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - parser to replace UBB style tags with their HTML equivalents
Summary(pl):	%{_pearname} - parser zastêpuj±cy tagi typu UBB ich odpowiednikami HTML
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bd67647b158ca513d615feb2d68f24ea
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

This class has in PEAR status: %{_status}.

%description -l pl
Jest to parser zastêpuj±cy tagi typu UBB ich odpowiednikami HTML. Nie
jest to jednak to tylko wywo³anie kilku wyra¿eñ regularnych, ale
kompletny silnik parsuj±cy. Dziêki temu pewne jest, i¿ wszystkie tagi
bêd± poprawnie zagnie¿dzone, a je¶li nie, dodatkowy tag zostanie
dodany w celu zachowania zagnie¿dzenia. Ten parser powinien
wyprodukowaæ kod zgodny z XHTML 1.0. Wszystkie tagi oraz ich atrybuty
sprawdzane s± pod k±tem poprawno¶ci. Mo¿liwe jest rozszerzenie parsera
o w³asne tagi.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Filter

install %{_pearname}-%{version}/*.php                     $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/Filter/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Filter

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/example
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
