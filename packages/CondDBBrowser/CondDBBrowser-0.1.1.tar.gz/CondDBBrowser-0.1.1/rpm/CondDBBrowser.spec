%define prefix /opt/LHCbSoft

%global __os_install_post /usr/lib/rpm/check-buildroot

Name: CondDBBrowser
# version and release values are filled by the gitlab-ci job
Version: 0
Release: 0
Vendor: LHCb
Summary: GUI to explore the content of LHCb Conditions Database
License: GPLv3
URL:     https://gitlab.cern.ch/lhcb/%{name}
Source:  https://gitlab.cern.ch/lhcb/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

Group: LHCb

BuildArch: noarch
AutoReqProv: no
Prefix: %{prefix}
Provides: /bin/sh
Provides: /bin/bash

BuildRequires: python-virtualenv

%description
GUI to explore the content of LHCb Conditions Database.

%prep
#%setup -q

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/contrib/%{name}/%{version}/bin
tmpdir=$(mktemp -d)
virtualenv $tmpdir/venv
source $tmpdir/venv/bin/activate
pip install git+https://gitlab.cern.ch/lhcb/%{name}.git@%{version}
deactivate
virtualenv --relocatable $tmpdir/venv
mv $tmpdir/venv ${RPM_BUILD_ROOT}%{prefix}/contrib/%{name}/%{version}
rm -rf $tmpdir
cat > ${RPM_BUILD_ROOT}%{prefix}/contrib/%{name}/%{version}/bin/CondDBBrowser <<EOF
#!/bin/sh
exec <<prefix>>/contrib/%{name}/%{version}/venv/bin/python <<prefix>>/contrib/%{name}/%{version}/venv/bin/CondDBBrowser
EOF
chmod a+x ${RPM_BUILD_ROOT}%{prefix}/contrib/%{name}/%{version}/bin/CondDBBrowser

%clean

%post -p /bin/bash
sed -i "s#<<prefix>>#${RPM_INSTALL_PREFIX}#g" ${RPM_INSTALL_PREFIX}/contrib/%{name}/%{version}/bin/CondDBBrowser

%postun -p /bin/bash

%files
%defattr(-,root,root)
%{prefix}/contrib/%{name}/%{version}

%changelog
* Wed Jan 02 2019 Marco Clemencic <marco.clemencic@cern.ch>
- first rpm package
