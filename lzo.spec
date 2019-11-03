#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lzo
Version  : 2.10
Release  : 22
URL      : http://www.oberhumer.com/opensource/lzo/download/lzo-2.10.tar.gz
Source0  : http://www.oberhumer.com/opensource/lzo/download/lzo-2.10.tar.gz
Summary  : LZO - a real-time data compression library
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: lzo-lib
Requires: lzo-doc

%description
============================================================================
LZO -- a real-time data compression library
============================================================================

%package dev
Summary: dev components for the lzo package.
Group: Development
Requires: lzo-lib
Provides: lzo-devel

%description dev
dev components for the lzo package.


%package doc
Summary: doc components for the lzo package.
Group: Documentation

%description doc
doc components for the lzo package.


%package lib
Summary: lib components for the lzo package.
Group: Libraries

%description lib
lib components for the lzo package.


%prep
%setup -q -n lzo-2.10

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488817319
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%configure --disable-static --enable-shared
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make test

%install
export SOURCE_DATE_EPOCH=1488817319
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/lzo/lzo1.h
/usr/include/lzo/lzo1a.h
/usr/include/lzo/lzo1b.h
/usr/include/lzo/lzo1c.h
/usr/include/lzo/lzo1f.h
/usr/include/lzo/lzo1x.h
/usr/include/lzo/lzo1y.h
/usr/include/lzo/lzo1z.h
/usr/include/lzo/lzo2a.h
/usr/include/lzo/lzo_asm.h
/usr/include/lzo/lzoconf.h
/usr/include/lzo/lzodefs.h
/usr/include/lzo/lzoutil.h
/usr/lib64/liblzo2.so
/usr/lib64/pkgconfig/lzo2.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/lzo/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblzo2.so.2
/usr/lib64/liblzo2.so.2.0.0
