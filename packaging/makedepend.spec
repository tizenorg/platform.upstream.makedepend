Name:           makedepend
Version:        1.0.5
Release:        0
License:        MIT
Summary:        Utility to create dependencies in makefiles
Url:            http://xorg.freedesktop.org/
Group:          Development/Tools/Building
Source0:        http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
Source1001:     makedepend.manifest
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
cp %{SOURCE1001} .

%build
%configure
%__make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING 
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1%{?ext_man}
