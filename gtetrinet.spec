Summary:	Clone of the popular Tetrinet game for Win95/NT
Summary(pl):	Klon Tetrinet, popularnej gry dla Win95/NT
Name:		gtetrinet
Version:	0.7.8
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	825e95f8665e4ada682c59edb5fcd861
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-desktop.patch
URL:		http://gtetrinet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	esound-devel
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTetrinet is a clone of the popular Tetrinet game for Win95/NT. It is
designed to be fully compatible with, and to be identical in gameplay
to the original Tetrinet.

%description -l pl
GTetrinet jest klonem Tetrinet, popularnej gry dla Win95/NT.
Zaprojektowano go maj±c na celu zapewnienie pe³nej zgodno¶ci z
Tetrinet oraz identycznego z ni± ¶rodowiska gry.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f po/no.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	gamesdir=%{_bindir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man6/*
