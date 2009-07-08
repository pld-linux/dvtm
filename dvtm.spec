Summary:	dvtm brings the concept of tiling window management to the console
Summary(hu.UTF-8):	dvtm a tiling ablakkezelést valósítja meg konzolon
Summary(pl.UTF-8):	dvtm - idea kaflowego zarządcy okien przeniesiona na konsolę
Name:		dvtm
Version:	0.5.2
Release:	1
License:	MIT
Group:		Applications/Terminal
Source0:	http://www.brain-dump.org/projects/dvtm/%{name}-%{version}.tar.gz
# Source0-md5:	7872b9e61705a4e9952655b3b88e4add
Patch0:		%{name}-optflags.patch
URL:		http://www.brain-dump.org/projects/dvtm/
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
Obsoletes:	dvtm-common
Obsoletes:	dvtm-iso
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

%description -l pl.UTF-8
dvtm przenosi na konsolę ideę kaflowego zarządcy okien, upowszechnioną
przez zarządców dla X11, takich jak dwm. Jako zarządca okien konsoli
próbuje ułatwić pracę z wieloma programami terminalowymi, takimi jak
vim, mutt, cmus czy irssi.

%prep
%setup -q
%patch0 -p1
%{__sed} -i "s@^PREFIX.*@PREFIX = %{_prefix}@ ; \
	s@\(^INCS =.*\)@\1 -I/usr/include/ncursesw@" config.mk

%build
%{__make} \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvtm*
%{_mandir}/man1/dvtm*
