#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zopfli
Version  : 0.1.9
Release  : 1
URL      : https://files.pythonhosted.org/packages/10/7d/278fd896401b0ef76e06cd42c3ce1541572d83b1c713b6786795c60a1bbe/zopfli-0.1.9.zip
Source0  : https://files.pythonhosted.org/packages/10/7d/278fd896401b0ef76e06cd42c3ce1541572d83b1c713b6786795c60a1bbe/zopfli-0.1.9.zip
Summary  : Zopfli module for python
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-zopfli-license = %{version}-%{release}
Requires: pypi-zopfli-python = %{version}-%{release}
Requires: pypi-zopfli-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(setuptools_scm)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Zopfli Compression Algorithm is a compression library programmed in C to perform
very good, but slow, deflate or zlib compression.

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
Requires: python3-core
Provides: pypi(zopfli)

%description python3
python3 components for the pypi-zopfli package.


%prep
%setup -q -n zopfli-0.1.9
cd %{_builddir}/zopfli-0.1.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638618668
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zopfli
cp %{_builddir}/zopfli-0.1.9/COPYING %{buildroot}/usr/share/package-licenses/pypi-zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589
cp %{_builddir}/zopfli-0.1.9/zopfli/COPYING %{buildroot}/usr/share/package-licenses/pypi-zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
