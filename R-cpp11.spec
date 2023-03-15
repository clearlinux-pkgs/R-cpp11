#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cpp11
Version  : 0.4.3
Release  : 28
URL      : https://cran.r-project.org/src/contrib/cpp11_0.4.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cpp11_0.4.3.tar.gz
Summary  : A C++11 Interface for R's C Interface
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
interface.  Compared to other approaches 'cpp11' strives to be safe
    against long jumps from the C API as well as C++ exceptions, conform
    to normal R function semantics and supports interaction with 'ALTREP'
    vectors.

%prep
%setup -q -n cpp11
cd %{_builddir}/cpp11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665602253

%install
export SOURCE_DATE_EPOCH=1665602253
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
