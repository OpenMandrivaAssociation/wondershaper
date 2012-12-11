%define name wondershaper
%define version 1.1a
%define release %mkrel 8

Summary: Helps maintain interactive latency on modem/ADSL/cable
Name: %name
Version: %version
Release: %release
License: GPL
Group: System/Servers
Url: http://lartc.org/wondershaper/
Source0: %name-%version.tar.bz2
Source1: wshaper.init.d
Source2: wshaper.cfg
Patch0: wondershaper-etc.patch.bz2
BuildRoot: %_tmppath/%name-%version
BuildArch: noarch
Requires(post,preun):	rpm-helper

%description
Maintain low latency for interfactive traffic at all times
This means that downloading or uploading files should not disturb SSH or 
even telnet. These are the most important things, even 200ms latency is 
sluggish to work over.
Allow 'surfing' at reasonable speeds while up or downloading
Even though http is 'bulk' traffic, other traffic should not drown it out 
too much.
Make sure uploads don't harm downloads, and the other way around. This is a 
much observed phenomenon where upstream traffic simply destroys download 
speed. It turns out that all this is possible, at the cost of a tiny bit of 
bandwidth. The reason that uploads, downloads and ssh hurt eachother is the 
presence of large queues in many domestic access devices like cable or DSL 
modems. 

%prep
rm -rf $RPM_BUILD_ROOT

%setup
%patch0 -p1

%build

%install

mkdir -p $RPM_BUILD_ROOT%_sbindir $RPM_BUILD_ROOT%_sysconfdir/rc.d/init.d
install -m 755 wshaper* $RPM_BUILD_ROOT%_sbindir/
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%_sysconfdir/rc.d/init.d/%{name}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%_sysconfdir/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service %{name}
/sbin/chkconfig --add %{name}


%preun
%_preun_service %{name}


%files
%defattr(-,root,root)
%doc COPYING README TODO VERSION ChangeLog
%{_sbindir}/*
%config(noreplace) %_sysconfdir/rc.d/init.d/%{name}
%attr(0644,root,root) %config(noreplace) %_sysconfdir/wshaper.cfg



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-8mdv2010.0
+ Revision: 434976
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-7mdv2009.0
+ Revision: 262125
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-6mdv2009.0
+ Revision: 256343
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-4mdv2008.1
+ Revision: 131806
- fix prereq on rpm-helper
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import wondershaper


* Fri Feb 11 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.1a-4mdk
- move config to /etc/wshaper.cfg
- add init script

* Mon Feb 16 2004 Michael Scherer <misc@mandrake.org> 1.1a-3mdk
- change to noarch
 
* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1a-2mdk
- rebuild

* Tue May 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1a-1mdk
- 1.1a
