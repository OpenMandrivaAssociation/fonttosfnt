Summary:	Wrap a bitmap font in a sfnt (TrueType) wrapper
Name:		fonttosfnt
Version:	1.2.4
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org/releases/individual/app
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
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
%doc %{_mandir}/man1/fonttosfnt*
