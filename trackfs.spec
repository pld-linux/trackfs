Summary:	Track file system changes
Summary(pl.UTF-8):	Śledzenie zmian w systemie plików
Name:		trackfs
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.mr511.de/software/%{name}-%{version}.tar.gz
# Source0-md5:	602bdd3c74862c3cf2c1e06fd96e6f21
URL:		http://www.mr511.de/software/english.html
ExclusiveArch:	%{ix86} %{x8664} %{arm}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trackfs is a small program that tracks file system changes - creation,
update and removal of fs objects - of another program (or group of
programs). It is similar to `installwatch', but works quite
differently: while installwatch uses LD_PRELOAD to intercept library
functions like open() and unlink(), trackfs runs the child program(s)
with tracing enabled and tracks the system calls they make.

%description -l pl.UTF-8
Trackfs to mały program śledzący zmiany w systemie plików - tworzenie,
modyfikowanie i usuwanie obiektów systemu plików - wykonywane przez
inny program (lub grupę programów). Jest podobny do programu
"installwatch", ale działa trochę inaczej - o ile installwatch
wykorzystuje LD_PRELOAD do przechwytywania funkcji bibliotecznych
takich jak open() czy unlink(), trackfs uruchamia program(y) potomne z
włączonym śledzeniem i śledzi wykonywane wywołania systemowe.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	instroot=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/playback
%attr(755,root,root) %{_bindir}/trackfs
%attr(755,root,root) %{_bindir}/trexec
%{_mandir}/man1/playback.1*
%{_mandir}/man1/trackfs.1*
%{_mandir}/man1/trexec.1*
