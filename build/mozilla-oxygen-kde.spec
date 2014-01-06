#firefox globals
%global moz_extensions %{_datadir}/mozilla/extensions
%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
#theme
%global src_ext_id \{C1F83B1E-D6EE-11DE-B441-1AD556D89593\}
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}
#options
%global src_ext_id2 \{c2a3f51e-2920-4eab-9008-1bcb44d21d57\}
%global inst_dir2 %{moz_extensions}/%{firefox_app_id}/%{src_ext_id2}

Name:           mozilla-oxygen-kde
Version:        4.0b3
%global version2 4_0_b3
%global version3 40b3
Release:        1%{?dist}.1
Summary:        Oxygen KDE theme for Mozilla Firefox

Group:          Applications/Internet
License:        GPLv3
URL:            http://oxygenkde.altervista.org
#Source0:	http://dl.dropbox.com/u/11188253/OXYGEN%20KDE%20FIREFOX/Oxygen%20KDE%20%{version}/OxygenKDE_%{version2}.xpi
Source0:        http://oxygenkde.altervista.org/download/OxygenKDE_%{version2}.xpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
#BuildRequires: java-1.6.0-openjdk-devel
#Requires:      firefox

%description
Oxygen KDE theme for Firefox providing nice integration with the KDE desktop.

%prep
%setup -q -c

mkdir tmp && cd tmp
unzip ../oxykdetheme.xpi
sed -i s/em:maxVersion\>23\./em:maxVersion\>29\./g install.rdf
zip ../oxykdetheme.xpi *
cd -
rm -Rf tmp

%build

rm -rf %{buildroot}
#Theme
install -Dp -m 644 oxykdetheme.xpi %{buildroot}%{inst_dir}.xpi

#Options for theme
install -Dp -m 644 oxykdeopt.xpi %{buildroot}%{inst_dir2}.xpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{inst_dir}.xpi
%{inst_dir2}.xpi

%changelog
* Sat Sep 21 2013 Chris Smart <csmart@kororaproject.org>- 4.0b3-1
- Update to upstream 4.0b3 release.

* Tue Mar 05 2013 Chris Smart <chris@kororaa.org>- 4.0b2-1
- Update to upstream 4.0b2 release.

* Tue Jan 15 2013 Chris Smart <chris@kororaa.org>- 3.9.4-1
- Update to upstream 3.9.4 bugfix release.

* Sat Jun 16 2012 Chris Smart <chris@kororaa.org>- 3.9.1-1
- Update to upstream 3.9.1 bugfix release.

* Tue Jun 12 2012 Chris Smart <chris@kororaa.org>- 3.9-1
- Update to upstream 3.9 release, Firefox 13 support.

* Sat Apr 28 2012 Chris Smart <chris@kororaa.org>- 3.8-1
- Update to upstream 3.8 release.

* Sat Feb 16 2012 Chris Smart <chris@kororaa.org>- 3.7-1
- Update to upstream 3.7 release.

* Fri Nov 11 2011 Chris Smart <chris@kororaa.org>- 3.6-1
- Update to 3.6 which includes support for Firefox 8.

* Wed Jul 06 2011 Chris Smart <chris@kororaa.org>- 3.5.1-1
- Update to 3.5.1 which includes support for Firefox 7.

* Wed Jul 06 2011 Chris Smart <chris@kororaa.org>- 3.2.1-1
- Update to 3.2.1 which includes support for Firefox 5.0.

* Mon Apr 25 2011 Chris Smart <chris@kororaa.org>- 3.1-1
- Update to 3.1 which fixes system-wide bug with options addon, switched to using .xpi rather than directory.

* Sat Mar 26 2011 Chris Smart <chris@kororaa.org>- 3.0-1
- Update to 3.0 which is Firefox4 compatible.

* Sat Mar 18 2011 Chris Smart <chris@kororaa.org>- 1.15-1
- Initial port.
