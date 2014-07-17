Name:		wondershaper
Version:	1.2.1
Release:	1
Summary:	Simple Network Shaper
Group:		System/Servers
License:	GPLv2+
URL:		http://sourceforge.net/projects/wondershaper/
Source:		http://downloads.sourceforge.net/project/wondershaper/%{name}-%{version}.tar.gz
Requires:	iproute2
BuildArch:	noarch

%description
Many cable-modem and ADSL users experience horrifying latency
while uploading or downloading. They also notice that uploading
hampers downloading greatly. The Wondershaper neatly addresses
these issues, allowing users of a router with a Wondershaper to
continue using SSH over a loaded link happily.

%prep
%setup -q

%build
# Nothing to build.

%install
install -pDm 755 wshaper %{buildroot}/%{_sbindir}/%{name}

%files
%doc ChangeLog COPYING README
%{_sbindir}/%{name}
