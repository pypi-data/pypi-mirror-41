%define name    dqsegdb2
%define version 1.0.1
%define release 1

Name:      %{name}
Version:   %{version}
Release:   %{release}%{?dist}
Summary:   Simplified python interface to DQSEGDB

License:   GPLv3
Url:       https://pypi.org/project/%{name}/
Source0:   https://pypi.io/packages/source/d/%{name}/%{name}-%{version}.tar.gz

Vendor:    Duncan Macleod <duncan.macleod@ligo.org>

BuildArch: noarch

BuildRequires: rpm-build
BuildRequires: python-rpm-macros
BuildRequires: python-srpm-macros
BuildRequires: python2-rpm-macros
BuildRequires: python3-rpm-macros

# python2-dqsegdb2
BuildRequires: python2-setuptools
BuildRequires: python2-ligo-segments
BuildRequires: python2-gwdatafind
BuildRequires: pytest
BuildRequires: python2-mock

# python3x-dqsegdb2
BuildRequires: python%{python3_version_nodots}-setuptools
BuildRequires: python%{python3_version_nodots}-ligo-segments
BuildRequires: python%{python3_version_nodots}-gwdatafind
BuildRequires: python%{python3_version_nodots}-pytest

%description
DQSEGDB2 is a simplified Python implementation of the DQSEGDB API as defined in
LIGO-T1300625.
This package only provides a query interface for `GET` requests, any users
wishing to make `POST` requests should refer to the official `dqsegdb` Python
client available from https://github.com/ligovirgo/dqsegdb/.

# -- python2-gwdatafind

%package -n python2-%{name}
Summary:  Simplified Python %{python2_version} interface to DQSEGDB
Requires: python2-ligo-segments
Requires: python2-gwdatafind
%{?python_provide:%python_provide python2-%{name}}
%description -n python2-%{name}
DQSEGDB2 is a simplified Python implementation of the DQSEGDB API as defined in
LIGO-T1300625.
This package only provides a query interface for `GET` requests, any users
wishing to make `POST` requests should refer to the official `dqsegdb` Python
client available from https://github.com/ligovirgo/dqsegdb/.

# -- python3x-gwdatafind

%package -n python%{python3_version_nodots}-%{name}
Summary:  Simplified Python %{python3_version} interface to DQSEGDB
Requires: python%{python3_version_nodots}-ligo-segments
Requires: python%{python3_version_nodots}-gwdatafind
%{?python_provide:%python_provide python%{python3_version_nodots}-%{name}}
%description -n python%{python3_version_nodots}-%{name}
DQSEGDB2 is a simplified Python implementation of the DQSEGDB API as defined in
LIGO-T1300625.
This package only provides a query interface for `GET` requests, any users
wishing to make `POST` requests should refer to the official `dqsegdb` Python
client available from https://github.com/ligovirgo/dqsegdb/.

# -- build steps

%prep
%autosetup -n %{name}-%{version}

%build
%py2_build
%py3_build

%check
%{__python2} -m pytest --pyargs %{name}
%{__python3} -m pytest --pyargs %{name}

%install
%py2_install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python2-%{name}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python%{python3_version_nodots}-%{name}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

# -- changelog

%changelog
* Thu Feb 07 2019 Duncan Macleod <duncan.macleod@ligo.org> - 1.0.1-1
- first release
