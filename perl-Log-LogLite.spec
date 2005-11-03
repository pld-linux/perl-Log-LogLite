#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	LogLite
Summary:	Log::LogLite - class to help us create simple logs for our application
Summary(pl):	Log::LogLite - klasa pomagaj±ca tworzyæ proste logi z aplikacji
Name:		perl-Log-LogLite
Version:	0.82
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67e72da51df7423c028b4dc0186f5f52
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-IO-LockedFile
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In order to have a log we have first to create a Log::LogLite object.
The Log::LogLite object is created with a logging level. The default 
logging level is 5. After the Log::LogLite object is created, each
call to the write method may write a new line in the log file. If the
level of the message is lower or equal to the logging level, the
message will be written to the log file. The format of the logging
messages can be controled by changing the template, and by defining a
default message. The class uses the IO::LockedFile class.

%description -l pl
W celu stworzenia logu trzeba najpierw utworzyæ obiekt Log::LogLite.
Obiekt Log::LogLite tworzy siê z poziomem logowania. Domy¶lny poziom
logowania to 5. Po utworzeniu obiektu Log::LogLite ka¿de wywo³anie
metody write mo¿e zapisaæ now± liniê w pliku logu. Je¶li poziom
komunikatu jest mniejszy lub równy poziomowi logowania, komunikat jest
zapisywany do pliku. Format komunikatów loguj±cych mo¿e byæ sterowany
poprzez zmianê szablonu i definiowanie domy¶lnego komunikatu. Ta klasa
u¿ywa klasy IO::LockedFile.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/*.pm
%{_mandir}/man3/*
