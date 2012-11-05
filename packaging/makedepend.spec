Name:           makedepend
Version:        1.0.4
Release:        0
License:        MIT
Summary:        Utility to create dependencies in makefiles
Url:            http://xorg.freedesktop.org/
Group:          Development/Tools/Building
Source0:        http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
Conflicts:      xorg-x11-util-devel <= 7.6

%description
The makedepend program reads each sourcefile in sequence and parses it
like a C-preprocessor so that it can correctly tell which #include
directives would be used in a compilation.

These dependencies are then written to a makefile in such a way that
make will know which object files must be recompiled when a dependency
has changed.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING 
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1%{?ext_man}

%changelog
