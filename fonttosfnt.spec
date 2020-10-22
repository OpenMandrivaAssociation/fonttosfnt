Summary:	Wrap a bitmap font in a sfnt (TrueType) wrapper
Name:		fonttosfnt
Version:	1.2.0
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org/releases/individual/app
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch1:		fonttosfnt-1.0.4-bzip2-linkage.patch

BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
Fonttosfnt wraps a bitmap font in a sfnt (TrueType or OpenType) wrapper.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt*
