%define		module		ruamel.yaml.clib
Summary:	C version of reader, parser and emitter for ruamel.yaml
Summary(pl.UTF-8):	Wersja C biblioteki do odczytu, analizy i tworzenia YAML-a dla ruamel.yaml
Name:		python3-%{module}
Version:	0.2.12
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.yaml.clib/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml.clib/%{module}-%{version}.tar.gz
# Source0-md5:	53fa5737bbe5a07fac7db3d1a083fee9
URL:		https://pypi.org/project/ruamel.yaml.clib/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:28.7.0
Requires:	python3-modules >= 1:3.9
# for dir
Requires:	python3-ruamel.base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C version of reader, parser and emitter for ruamel.yaml derived from
libyaml.

%description -l pl.UTF-8
Wersja C biblioteki do odczytu, analizy i tworzenia YAML-a dla
ruamel.yaml, wywodząca się z libyaml.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{py3_sitedir}/_ruamel_yaml.cpython-*.so
%dir %{py3_sitedir}/ruamel/yaml
%{py3_sitedir}/ruamel/yaml/clib
%{py3_sitedir}/ruamel.yaml.clib-%{version}-py*.egg-info
