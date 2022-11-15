#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zopfli
Version  : 0.2.2
Release  : 12
URL      : https://files.pythonhosted.org/packages/9a/ed/d004d5737f9546167eecf0ecd995ee1a796703e512deb2f2ea26cdbe4b3e/zopfli-0.2.2.zip
Source0  : https://files.pythonhosted.org/packages/9a/ed/d004d5737f9546167eecf0ecd995ee1a796703e512deb2f2ea26cdbe4b3e/zopfli-0.2.2.zip
Summary  : Zopfli module for python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-zopfli-filemap = %{version}-%{release}
Requires: pypi-zopfli-lib = %{version}-%{release}
Requires: pypi-zopfli-license = %{version}-%{release}
Requires: pypi-zopfli-python = %{version}-%{release}
Requires: pypi-zopfli-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Zopfli Compression Algorithm is a compression library programmed in C to perform
very good, but slow, deflate or zlib compression.

%package filemap
Summary: filemap components for the pypi-zopfli package.
Group: Default

%description filemap
filemap components for the pypi-zopfli package.


%package lib
Summary: lib components for the pypi-zopfli package.
Group: Libraries
Requires: pypi-zopfli-license = %{version}-%{release}
Requires: pypi-zopfli-filemap = %{version}-%{release}

%description lib
lib components for the pypi-zopfli package.


%package license
Summary: license components for the pypi-zopfli package.
Group: Default

%description license
license components for the pypi-zopfli package.


%package python
Summary: python components for the pypi-zopfli package.
Group: Default
Requires: pypi-zopfli-python3 = %{version}-%{release}

%description python
python components for the pypi-zopfli package.


%package python3
Summary: python3 components for the pypi-zopfli package.
Group: Default
Requires: pypi-zopfli-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(zopfli)

%description python3
python3 components for the pypi-zopfli package.


%prep
%setup -q -n zopfli-0.2.2
cd %{_builddir}/zopfli-0.2.2
pushd ..
cp -a zopfli-0.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668549168
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zopfli
cp %{_builddir}/zopfli-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589 || :
cp %{_builddir}/zopfli-%{version}/zopfli/COPYING %{buildroot}/usr/share/package-licenses/pypi-zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-zopfli

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
