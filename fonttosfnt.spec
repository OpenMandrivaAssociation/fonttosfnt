Name:		fonttosfnt
Version:	1.0.4
Release:	7
Summary:	Wrap a bitmap font in a sfnt (TrueType) wrapper
Group:		System/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libfontenc-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.1.10
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-6mdv2011.0
+ Revision: 664344
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5mdv2011.0
+ Revision: 605209
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2010.1
+ Revision: 522656
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-3mdv2010.0
+ Revision: 424459
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2009.0
+ Revision: 264468
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 212548
- new release

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2008.1
+ Revision: 150079
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.3-2mdv2008.0
+ Revision: 91067
- rebuild for 2008
- minor spec clean


* Fri Feb 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 121974
- fix file list
- kill merged patch
- new release

* Fri Aug 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-4mdv2007.0
+ Revision: 57866
- fixed the group
- added a patch fixing compilation with newer freetype versions
  (thanks Stefan van der Eijk for the patch)
- rebuild to fix cooker uploading
- increment release
- Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description

