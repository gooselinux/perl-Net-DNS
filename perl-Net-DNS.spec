Name: perl-Net-DNS
Version: 0.65
Release: 2%{?dist}
Summary: DNS resolver modules for Perl
License: GPL+ or Artistic
Group: Development/Libraries
URL: http://www.net-dns.org/
Source0: http://www.cpan.org/authors/id/O/OL/OLAF/Net-DNS-%{version}.tar.gz
BuildRequires: perl(Digest::HMAC), perl(ExtUtils::MakeMaker), perl(Test::More), perl(Net::IP)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Digest::BubbleBabble)
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Net::DNS is a collection of Perl modules that act as a Domain Name
System (DNS) resolver. It allows the programmer to perform DNS queries
that are beyond the capabilities of gethostbyname and gethostbyaddr.

The programmer should be somewhat familiar with the format of a DNS
packet and its various sections. See RFC 1035 or DNS and BIND (Albitz
& Liu) for details.


%package Nameserver
Summary:        DNS server for Perl
Group:          Development/Libraries
License:        GPL+ or Artistic

%description Nameserver
Instances of the "Net::DNS::Nameserver" class represent DNS server
objects.


%prep
%setup -q -n Net-DNS-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --no-online-tests
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

for i in Changes; do
  /usr/bin/iconv -f iso8859-1 -t utf-8 $i > $i.conv && /bin/mv -f $i.conv $i
done

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes TODO
%{perl_vendorarch}/Net/
%exclude %{perl_vendorarch}/Net/DNS/Resolver/Cygwin.pm
%exclude %{perl_vendorarch}/Net/DNS/Resolver/Win32.pm
%{perl_vendorarch}/auto/Net/
%{_mandir}/man3/Net::DNS*.3*
%exclude %{_mandir}/man3/Net::DNS::Resolver::Cygwin.3*
%exclude %{_mandir}/man3/Net::DNS::Resolver::Win32.3*

# perl-Net-DNS-Nameserver
%exclude %{perl_vendorarch}/Net/DNS/Nameserver.pm
%exclude %{_mandir}/man3/Net::DNS::Nameserver*

%files Nameserver
%defattr(-,root,root)
%{perl_vendorarch}/Net/DNS/Nameserver.pm
%{_mandir}/man3/Net::DNS::Nameserver*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.65-2
- rebuild against perl 5.10.1

* Thu Sep 17 2009 Warren Togami <wtogami@redhat.com> - 0.65-1
- 0.65

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 12 2008 Marcela Maslanova <mmaslano@redhat.com> - 0.63-4
- 437681 remove previous patch and use upstream patch, which should solve
        all problems with noisy logs.

* Wed Apr  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-3
- fix patch to not require Socket6

* Wed Apr  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-2
- fix AF_INET6/PF_INET6 redefine noise (bz 437681)

* Wed Mar 19 2008 Marcela Maslanova <mmaslano@redhat.com> - 0.63-1
- upgrade on new upstream version which fix CVE-2007-6341 - no security impact.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.61-7
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.61-6
- Autorebuild for GCC 4.3

* Thu Jan 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.61-5
- rebuild for new perl

* Fri Dec 21 2007 Paul Howarth <paul@city-fan.org> - 0.61-4
- Fix file ownership for Nameserver subpackage
- Fix argument order for find with -depth

* Fri Dec 14 2007 Robin Norwood <rnorwood@redhat.com> - 0.61-3
- Split Nameserver.pm into subpackage, per recommendation from
  upstream maintainer Dick Franks.
  - Separates the server bits from the client bits.
  - Removes the dependancy on perl(Net::IP) from perl-Net-DNS
- Add BR for perl(Test::Pod) and perl(Digest::BubbleBabble)

* Wed Oct 24 2007 Robin Norwood <rnorwood@redhat.com> - 0.61-2
- Update license tag
- Convert Changes to utf-8

* Thu Aug 09 2007 Robin Norwood <rnorwood@redhat.com> - 0.61-1
- Update to latest upstream version

* Sat Jun 23 2007 Robin Norwood <rnorwood@redhat.com> - 0.60-1
- Upgrade to latest upstream version - 0.60

* Thu Apr 05 2007 Robin Norwood <rnorwood@redhat.com> - 0.59-2
- Resolves: bz#226270
- Fixed issues brought up during package review
- BuildRequires should not require perl, and fixed the format.
- Fixed the BuildRoot

* Wed Sep 27 2006 Robin Norwood <rnorwood@redhat.com> - 0.59-1
- Upgrade to upstream version 0.59 per bug #208315

* Mon Jul 17 2006 Jason Vas Dias <jvdias@redhat.com> - 0.58-1.fc6
- Upgrade to upstream version 0.58

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.57-1.1
- rebuild

* Wed Mar 08 2006 Jason Vas Dias <jvdias@redhat.com> - 0.57-1
- Upgrade to upstream version 0.57

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.55-1.1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.55-1.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 0.55-1.1
- rebuild for new perl-5.8.8

* Mon Dec 19 2005 Jason Vas Dias <jvdias@redhat.com> - 0.55-1
- Upgrade to upstream version 0.55

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sun Oct 30 2005 Warren Togami <wtogami@redhat.com> - 0.53-1
- 0.53 buildreq perl-Net-IP

* Sat Apr  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.49-2
- Explicitly disable tests requiring network access at build time.
- Exclude Win32 and Cygwin specific modules.
- More specfile cleanups.
- Honor $RPM_OPT_FLAGS.

* Sat Apr 02 2005 Robert Scheck <redhat@linuxnetz.de> 0.49-1
- upgrade to 0.49 and spec file cleanup (#153186)

* Thu Mar 17 2005 Warren Togami <wtogami@redhat.com> 0.48-3
- reinclude ia64, thanks jvdias

* Tue Mar 15 2005 Warren Togami <wtogami@redhat.com> 0.48-2
- exclude ia64 for now due to Bug #151127

* Mon Oct 11 2004 Warren Togami <wtogami@redhat.com> 0.48-1
- #119983 0.48 fixes bugs

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 0.45-4
- rebuild

* Thu Apr 29 2004 Chip Turner <cturner@redhat.com> 0.45-3
- fix bug 122039 -- add filter-depends.sh to remove Win32 deps

* Fri Apr 23 2004 Chip Turner <cturner@redhat.com> 0.45-1
- bump, no longer noarch

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 0.45-1
- update to 0.45

* Mon Oct 20 2003 Chip Turner <cturner@redhat.com> 0.31-3.2
- fix interactive build issue

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Tue Dec 10 2002 Chip Turner <cturner@redhat.com>
- update to latest version from CPAN

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Aug  6 2002 Chip Turner <cturner@localhost.localdomain>
- update to 0.26

* Thu Jun 27 2002 Chip Turner <cturner@redhat.com>
- description update

* Sat Jun 15 2002 cturner@redhat.com
- Specfile autogenerated

