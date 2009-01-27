Summary:	dvtm brings the concept of tiling window management to the console (UTF version)
Summary(hu.UTF-8):	dvtm a tiling ablakkezelést valósítja meg konzolon
Name:		dvtm
Version:	0.5
Release:	0.1
License:	MIT/X
Group:		Applications/Terminal
Source0:	http://www.brain-dump.org/projects/dvtm/%{name}-%{version}.tar.gz
# Source0-md5:	076db11f53440c194cf24deceb469321
URL:		http://www.brain-dump.org/projects/dvtm/
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvtm brings the concept of tiling window management, popularized by
X11-window managers like dwm to the console. As a console window
manager it tries to make it easy to work with multiple console based
programs like vim, mutt, cmus or irssi.

%description -l hu.UTF-8
dvtm a tiling ablakkezelők (pl. dwm) koncepcióját valósítja meg
konzolon. Egy konzolos ablakkezelőként próbálja meg könnyűvé tenni a
munkát több konzol alapú programmal egyidőben, mint pl. a vim, mutt,
cmus vagy irssi.

%package common
Summary:	Common files of dvtm
Summary(hu.UTF-8):	A dvtm általános fájljai
Group:		Applications/Terminal

%description common
Common files of dvtm.

%description common -l hu.UTF-8
A dvtm általános fájljai

%package iso
Summary:	ISO version of dvtm
Summary(hu.UTF-8):	ISO verzió a dvtm-ből
Group:		Applications/Terminal
Requires:	%{name}-common = %{version}-%{release}

%description iso
ISO version of dvtm.

%description iso -l hu.UTF-8
ISO verzió a dvtm-ből.

%prep
%setup -q
%{__sed} -i "s@^PREFIX.*@PREFIX = %{_prefix}@ ; \
	s@\(^INCS =.*\)@\1 -I/usr/include/ncursesw@" config.mk

%build
# iso version
%{__make}
mv dvtm dvtm-iso

# we want unicode
%{__make} unicode

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install dvtm-iso $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvtm

%files common
%doc README
%attr(755,root,root) %{_bindir}/dvtm-status
%{_mandir}/man1/dvtm*

%files iso
%attr(755,root,root) %{_bindir}/dvtm-iso
