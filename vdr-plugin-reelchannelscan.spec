
%define plugin	reelchannelscan
%define name	vdr-plugin-%plugin
%define version	0.4.3
%define rel	10

Summary:	VDR plugin: Search Transponders for DVB Channels
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdr-wiki.de/wiki/index.php/Reelchannelscan-plugin
# Not upstream URL:
Source:		http://deela.cc.fh-lippe.de/files/vdr-reelchannelscan/vdr-%plugin-%version.tar.bz2
# dpatches are from e-tobi repo
Patch0:		04_reelchannelscan-0.3.0-configdir.dpatch
Patch1:		02_scanning_status_service.dpatch
Patch2:		90_reelchannelscan-0.4.3-vdr-1.5.10.dpatch
Patch3:		reelchannelscan-0.4.3-i18n-1.6.patch
Patch4:		reelchannelscan-includes.patch
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	dos2unix
Requires:	vdr-abi = %vdr_abi

%description
This plugin reads sources.conf and parses the corresponding
transponderlist (.tpl file), then it scans this sat and
updates/appends all found channels to the current channel list.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%vdr_plugin_prep
dos2unix transponders/sources.conf

%build
%vdr_plugin_build

%install
%vdr_plugin_install
install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}/%plugin/transponders
install -m644 transponders/*.tpl %{buildroot}%{vdr_plugin_cfgdir}/%plugin/transponders

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO transponders/sources.conf
%dir %{vdr_plugin_cfgdir}/%plugin
%dir %{vdr_plugin_cfgdir}/%plugin/transponders
%config %{vdr_plugin_cfgdir}/%plugin/transponders/*.tpl


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.4.3-8mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.4.3-7mdv2009.1
+ Revision: 359769
- fix includes (includes.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.4.3-6mdv2009.0
+ Revision: 197970
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.4.3-5mdv2009.0
+ Revision: 197715
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- add scanning status service to avoid global variables (P1 from e-tobi)
- adapt for api changes of VDR 1.5.10 (P2 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.4.3-4mdv2008.1
+ Revision: 145194
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.4.3-3mdv2008.1
+ Revision: 103189
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.4.3-2mdv2008.0
+ Revision: 50038
- rebuild for new vdr

* Wed Jun 27 2007 Anssi Hannula <anssi@mandriva.org> 0.4.3-1mdv2008.0
+ Revision: 44991
- initial Mandriva release

