#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		ruamel.yaml.clib
Summary:	C version of reader, parser and emitter for ruamel.yaml
Summary(pl.UTF-8):	Wersja C biblioteki do odczytu, analizy i tworzenia YAML-a dla ruamel.yaml
Name:		python-%{module}
Version:	0.2.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.yaml.clib/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.yaml.clib/%{module}-%{version}.tar.gz
# Source0-md5:	d188d050399426dd3ce4dd91a5f06518
URL:		https://pypi.org/project/ruamel.yaml.clib/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 28.7.0
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 28.7.0
%endif
Requires:	python-modules >= 1:2.7
# for dir
Requires:	python-ruamel.base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C version of reader, parser and emitter for ruamel.yaml derived from
libyaml.

%description -l pl.UTF-8
Wersja C biblioteki do odczytu, analizy i tworzenia YAML-a dla
ruamel.yaml, wywodząca się z libyaml.

%package -n python3-%{module}
Summary:	C version of reader, parser and emitter for ruamel.yaml
Summary(pl.UTF-8):	Wersja C biblioteki do odczytu, analizy i tworzenia YAML-a ruamel.yaml
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
# for dir
Requires:	python3-ruamel.base

%description -n python3-%{module}
C version of reader, parser and emitter for ruamel.yaml derived from
libyaml.

%description -n python3-%{module} -l pl.UTF-8
Wersja C biblioteki do odczytu, analizy i tworzenia YAML-a dla
ruamel.yaml, wywodząca się z libyaml.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{py_sitedir}/_ruamel_yaml.so
%dir %{py_sitedir}/ruamel/yaml
%{py_sitedir}/ruamel/yaml/clib
%{py_sitedir}/ruamel.yaml.clib-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{py3_sitedir}/_ruamel_yaml.cpython-*.so
%dir %{py3_sitedir}/ruamel/yaml
%{py3_sitedir}/ruamel/yaml/clib
%{py3_sitedir}/ruamel.yaml.clib-%{version}-py*.egg-info
%endif
