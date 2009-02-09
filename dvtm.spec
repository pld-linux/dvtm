Summary:	dvtm brings the concept of tiling window management to the console (UTF version)
Summary(hu.UTF-8):	dvtm a tiling ablakkezelést valósítja meg konzolon
Name:		dvtm
Version:	0.5.1
Release:	0.1
License:	MIT/X
Group:		Applications/Terminal
Source0:	http://www.brain-dump.org/projects/dvtm/%{name}-%{version}.tar.gz
# Source0-md5:	15af44198d6a636190480122b8de7155
URL:		http://www.brain-dump.org/projects/dvtm/
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
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

%prep
%setup -q
%{__sed} -i "s@^PREFIX.*@PREFIX = %{_prefix}@ ; \
	s@\(^INCS =.*\)@\1 -I/usr/include/ncursesw@" config.mk

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvtm*
%{_mandir}/man1/dvtm*
