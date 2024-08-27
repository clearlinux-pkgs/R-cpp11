#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-cpp11
Version  : 0.5.0
Release  : 37
URL      : https://cran.r-project.org/src/contrib/cpp11_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cpp11_0.5.0.tar.gz
Summary  : A C++11 Interface for R's C Interface
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
interface.  Compared to other approaches 'cpp11' strives to be safe
    against long jumps from the C API as well as C++ exceptions, conform
    to normal R function semantics and supports interaction with 'ALTREP'
    vectors.

%prep
%setup -q -n cpp11
pushd ..
cp -a cpp11 buildavx2
popd
pushd ..
cp -a cpp11 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724734005

%install
export SOURCE_DATE_EPOCH=1724734005
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cpp11/DESCRIPTION
/usr/lib64/R/library/cpp11/INDEX
/usr/lib64/R/library/cpp11/LICENSE
/usr/lib64/R/library/cpp11/Meta/Rd.rds
/usr/lib64/R/library/cpp11/Meta/features.rds
/usr/lib64/R/library/cpp11/Meta/hsearch.rds
/usr/lib64/R/library/cpp11/Meta/links.rds
/usr/lib64/R/library/cpp11/Meta/nsInfo.rds
/usr/lib64/R/library/cpp11/Meta/package.rds
/usr/lib64/R/library/cpp11/Meta/vignette.rds
/usr/lib64/R/library/cpp11/NAMESPACE
/usr/lib64/R/library/cpp11/NEWS.md
/usr/lib64/R/library/cpp11/R/cpp11
/usr/lib64/R/library/cpp11/R/cpp11.rdb
/usr/lib64/R/library/cpp11/R/cpp11.rdx
/usr/lib64/R/library/cpp11/doc/FAQ.R
/usr/lib64/R/library/cpp11/doc/FAQ.Rmd
/usr/lib64/R/library/cpp11/doc/FAQ.html
/usr/lib64/R/library/cpp11/doc/converting.R
/usr/lib64/R/library/cpp11/doc/converting.Rmd
/usr/lib64/R/library/cpp11/doc/converting.html
/usr/lib64/R/library/cpp11/doc/cpp11.R
/usr/lib64/R/library/cpp11/doc/cpp11.Rmd
/usr/lib64/R/library/cpp11/doc/cpp11.html
/usr/lib64/R/library/cpp11/doc/index.html
/usr/lib64/R/library/cpp11/doc/internals.R
/usr/lib64/R/library/cpp11/doc/internals.Rmd
/usr/lib64/R/library/cpp11/doc/internals.html
/usr/lib64/R/library/cpp11/doc/motivations.R
/usr/lib64/R/library/cpp11/doc/motivations.Rmd
/usr/lib64/R/library/cpp11/doc/motivations.html
/usr/lib64/R/library/cpp11/help/AnIndex
/usr/lib64/R/library/cpp11/help/aliases.rds
/usr/lib64/R/library/cpp11/help/cpp11.rdb
/usr/lib64/R/library/cpp11/help/cpp11.rdx
/usr/lib64/R/library/cpp11/help/paths.rds
/usr/lib64/R/library/cpp11/html/00Index.html
/usr/lib64/R/library/cpp11/html/R.css
/usr/lib64/R/library/cpp11/include/cpp11.hpp
/usr/lib64/R/library/cpp11/include/cpp11/R.hpp
/usr/lib64/R/library/cpp11/include/cpp11/altrep.hpp
/usr/lib64/R/library/cpp11/include/cpp11/as.hpp
/usr/lib64/R/library/cpp11/include/cpp11/attribute_proxy.hpp
/usr/lib64/R/library/cpp11/include/cpp11/data_frame.hpp
/usr/lib64/R/library/cpp11/include/cpp11/declarations.hpp
/usr/lib64/R/library/cpp11/include/cpp11/doubles.hpp
/usr/lib64/R/library/cpp11/include/cpp11/environment.hpp
/usr/lib64/R/library/cpp11/include/cpp11/external_pointer.hpp
/usr/lib64/R/library/cpp11/include/cpp11/function.hpp
/usr/lib64/R/library/cpp11/include/cpp11/integers.hpp
/usr/lib64/R/library/cpp11/include/cpp11/list.hpp
/usr/lib64/R/library/cpp11/include/cpp11/list_of.hpp
/usr/lib64/R/library/cpp11/include/cpp11/logicals.hpp
/usr/lib64/R/library/cpp11/include/cpp11/matrix.hpp
/usr/lib64/R/library/cpp11/include/cpp11/named_arg.hpp
/usr/lib64/R/library/cpp11/include/cpp11/protect.hpp
/usr/lib64/R/library/cpp11/include/cpp11/r_bool.hpp
/usr/lib64/R/library/cpp11/include/cpp11/r_string.hpp
/usr/lib64/R/library/cpp11/include/cpp11/r_vector.hpp
/usr/lib64/R/library/cpp11/include/cpp11/raws.hpp
/usr/lib64/R/library/cpp11/include/cpp11/sexp.hpp
/usr/lib64/R/library/cpp11/include/cpp11/strings.hpp
/usr/lib64/R/library/cpp11/include/fmt/core.h
/usr/lib64/R/library/cpp11/include/fmt/format-inl.h
/usr/lib64/R/library/cpp11/include/fmt/format.h
/usr/lib64/R/library/cpp11/tests/testthat.R
/usr/lib64/R/library/cpp11/tests/testthat/_snaps/register.md
/usr/lib64/R/library/cpp11/tests/testthat/_snaps/source.md
/usr/lib64/R/library/cpp11/tests/testthat/helper.R
/usr/lib64/R/library/cpp11/tests/testthat/linking_to_incorrect_registers.cpp
/usr/lib64/R/library/cpp11/tests/testthat/linking_to_registers.cpp
/usr/lib64/R/library/cpp11/tests/testthat/multiple.cpp
/usr/lib64/R/library/cpp11/tests/testthat/multiple_incorrect.cpp
/usr/lib64/R/library/cpp11/tests/testthat/single.cpp
/usr/lib64/R/library/cpp11/tests/testthat/single_error.cpp
/usr/lib64/R/library/cpp11/tests/testthat/single_incorrect.cpp
/usr/lib64/R/library/cpp11/tests/testthat/test-knitr.R
/usr/lib64/R/library/cpp11/tests/testthat/test-register.R
/usr/lib64/R/library/cpp11/tests/testthat/test-source.R
/usr/lib64/R/library/cpp11/tests/testthat/test-utils.R
/usr/lib64/R/library/cpp11/tests/testthat/test-vendor.R
