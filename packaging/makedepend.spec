#
# spec file for package makedepend
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# This was part of the xorg-x11-util-devel package up to version 7.6
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
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1%{?ext_man}

%changelog
