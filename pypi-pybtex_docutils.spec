#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pybtex_docutils
Version  : 1.0.2
Release  : 30
URL      : https://files.pythonhosted.org/packages/54/82/360c8d20d8fffdaac243d3b0d1633a037ea3af9a51aa47d7af5b0c059b49/pybtex-docutils-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/54/82/360c8d20d8fffdaac243d3b0d1633a037ea3af9a51aa47d7af5b0c059b49/pybtex-docutils-1.0.2.tar.gz
Summary  : A docutils backend for pybtex.
Group    : Development/Tools
License  : MIT
Requires: pypi-pybtex_docutils-license = %{version}-%{release}
Requires: pypi-pybtex_docutils-python = %{version}-%{release}
Requires: pypi-pybtex_docutils-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(pybtex)

%description
--------

%package license
Summary: license components for the pypi-pybtex_docutils package.
Group: Default

%description license
license components for the pypi-pybtex_docutils package.


%package python
Summary: python components for the pypi-pybtex_docutils package.
Group: Default
Requires: pypi-pybtex_docutils-python3 = %{version}-%{release}

%description python
python components for the pypi-pybtex_docutils package.


%package python3
Summary: python3 components for the pypi-pybtex_docutils package.
Group: Default
Requires: python3-core
Provides: pypi(pybtex_docutils)
Requires: pypi(docutils)
Requires: pypi(pybtex)

%description python3
python3 components for the pypi-pybtex_docutils package.


%prep
%setup -q -n pybtex-docutils-1.0.2
cd %{_builddir}/pybtex-docutils-1.0.2
pushd ..
cp -a pybtex-docutils-1.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656396731
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pybtex_docutils
cp %{_builddir}/pybtex-docutils-1.0.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-pybtex_docutils/b060e9b6372c36f719c9b9f2ccff3fd48c732512
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pybtex_docutils/b060e9b6372c36f719c9b9f2ccff3fd48c732512

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
