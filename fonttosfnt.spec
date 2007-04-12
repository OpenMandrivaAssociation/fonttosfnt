Name: fonttosfnt
Version: 1.0.3
Release: %mkrel 1
Summary: Wrap a bitmap font in a sfnt (TrueType) wrapper
Group: System/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libfontenc-devel >= 1.0.1
BuildRequires: freetype2-devel >= 2.1.10
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Fonttosfnt wraps a bitmap font in a sfnt (TrueType or OpenType) wrapper.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt*


