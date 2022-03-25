#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	LHA (.lzh) file extract interface
Summary(pl.UTF-8):	Interfejs do rozpakowywania plików LHA (.lzh)
Name:		python-lhafile
Version:	0.2.2
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/lhafile/
Source0:	https://files.pythonhosted.org/packages/source/l/lhafile/lhafile-%{version}.tar.gz
# Source0-md5:	5d916030a6623c12d12a1e4e05cb8939
URL:		https://pypi.org/project/lhafile/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extract LHA (.lzh) file extension. The interface is similar to the
zipfile module in the regular Python distribution.

%description -l pl.UTF-8
Rozszerzenie Pythona do rozpakowywania plików LHA (.lzh). Interfejs
jest podobny do modułu zipfile z dystrybucji Pythona.

%package -n python3-lhafile
Summary:	LHA (.lzh) file extract interface
Summary(pl.UTF-8):	Interfejs do rozpakowywania plików LHA (.lzh)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-lhafile
Extract LHA (.lzh) file extension. The interface is similar to the
zipfile module in the regular Python distribution.

%description -n python3-lhafile -l pl.UTF-8
Rozszerzenie Pythona do rozpakowywania plików LHA (.lzh). Interfejs
jest podobny do modułu zipfile z dystrybucji Pythona.

%prep
%setup -q -n lhafile-%{version}

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
%doc COPYING.txt README
%{py_sitedir}/lhafile
%attr(755,root,root) %{py_sitedir}/lzhlib.so
%{py_sitedir}/lhafile-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-lhafile
%defattr(644,root,root,755)
%doc COPYING.txt README
%{py3_sitedir}/lhafile
%attr(755,root,root) %{py3_sitedir}/lzhlib.cpython-*.so
%{py3_sitedir}/lhafile-%{version}-py*.egg-info
%endif
