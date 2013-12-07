Summary:	Wrap a bitmap font in a sfnt (TrueType) wrapper
Name:		fonttosfnt
Version:	1.0.4
Release:	11
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org/releases/individual/app
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		aarch64.patch
Patch1:		fonttosfnt-1.0.4-bzip2-linkage.patch

BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel >= 2.1.10
BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
Fonttosfnt wraps a bitmap font in a sfnt (TrueType or OpenType) wrapper.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt*

