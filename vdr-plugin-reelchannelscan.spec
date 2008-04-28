
%define plugin	reelchannelscan
%define name	vdr-plugin-%plugin
%define version	0.4.3
%define rel	6

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
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%vdr_plugin_prep
dos2unix transponders/sources.conf

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install
install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%plugin/transponders
install -m644 transponders/*.tpl %{buildroot}%{_vdr_plugin_cfgdir}/%plugin/transponders

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO transponders/sources.conf
%dir %{_vdr_plugin_cfgdir}/%plugin
%dir %{_vdr_plugin_cfgdir}/%plugin/transponders
%config %{_vdr_plugin_cfgdir}/%plugin/transponders/*.tpl
