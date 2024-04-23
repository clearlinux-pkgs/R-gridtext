#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-gridtext
Version  : 0.1.5
Release  : 1
URL      : https://cran.r-project.org/src/contrib/gridtext_0.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gridtext_0.1.5.tar.gz
Summary  : Improved Text Rendering Support for 'Grid' Graphics
Group    : Development/Tools
License  : MIT
Requires: R-gridtext-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-curl
Requires: R-jpeg
Requires: R-markdown
Requires: R-png
Requires: R-rlang
Requires: R-stringr
Requires: R-xml2
BuildRequires : R-Rcpp
BuildRequires : R-curl
BuildRequires : R-jpeg
BuildRequires : R-markdown
BuildRequires : R-png
BuildRequires : R-rlang
BuildRequires : R-stringr
BuildRequires : R-xml2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
formatted via a minimal subset of 'Markdown', 'HTML', and inline 'CSS' directives, and it can be
    rendered both with and without word wrap.

%package lib
Summary: lib components for the R-gridtext package.
Group: Libraries

%description lib
lib components for the R-gridtext package.


%prep
%setup -q -n gridtext

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713891213

%install
export SOURCE_DATE_EPOCH=1713891213
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


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gridtext/DESCRIPTION
/usr/lib64/R/library/gridtext/INDEX
/usr/lib64/R/library/gridtext/LICENSE
/usr/lib64/R/library/gridtext/Meta/Rd.rds
/usr/lib64/R/library/gridtext/Meta/features.rds
/usr/lib64/R/library/gridtext/Meta/hsearch.rds
/usr/lib64/R/library/gridtext/Meta/links.rds
/usr/lib64/R/library/gridtext/Meta/nsInfo.rds
/usr/lib64/R/library/gridtext/Meta/package.rds
/usr/lib64/R/library/gridtext/NAMESPACE
/usr/lib64/R/library/gridtext/NEWS.md
/usr/lib64/R/library/gridtext/R/gridtext
/usr/lib64/R/library/gridtext/R/gridtext.rdb
/usr/lib64/R/library/gridtext/R/gridtext.rdx
/usr/lib64/R/library/gridtext/extdata/Rlogo.png
/usr/lib64/R/library/gridtext/help/AnIndex
/usr/lib64/R/library/gridtext/help/aliases.rds
/usr/lib64/R/library/gridtext/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/gridtext/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/gridtext/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/gridtext/help/figures/README-unnamed-chunk-7-1.png
/usr/lib64/R/library/gridtext/help/figures/README-unnamed-chunk-8-1.png
/usr/lib64/R/library/gridtext/help/gridtext.rdb
/usr/lib64/R/library/gridtext/help/gridtext.rdx
/usr/lib64/R/library/gridtext/help/paths.rds
/usr/lib64/R/library/gridtext/html/00Index.html
/usr/lib64/R/library/gridtext/html/R.css
/usr/lib64/R/library/gridtext/tests/figs/deps.txt
/usr/lib64/R/library/gridtext/tests/figs/grid-renderer/mixing-text-and-boxes.svg
/usr/lib64/R/library/gridtext/tests/figs/grid-renderer/rendering-raster-data.svg
/usr/lib64/R/library/gridtext/tests/figs/grid-renderer/text-in-different-stylings.svg
/usr/lib64/R/library/gridtext/tests/figs/richtext-grob/aligned-heights.svg
/usr/lib64/R/library/gridtext/tests/figs/richtext-grob/aligned-widths.svg
/usr/lib64/R/library/gridtext/tests/figs/richtext-grob/various-text-boxes-w-debug.svg
/usr/lib64/R/library/gridtext/tests/figs/richtext-grob/various-text-boxes.svg
/usr/lib64/R/library/gridtext/tests/figs/test_image.png
/usr/lib64/R/library/gridtext/tests/figs/textbox-grob/box-spanning-entire-viewport-with-margins.svg
/usr/lib64/R/library/gridtext/tests/figs/textbox-grob/multiple-boxes-internal-alignment.svg
/usr/lib64/R/library/gridtext/tests/figs/textbox-grob/multiple-boxes-inverted-internal-alignment.svg
/usr/lib64/R/library/gridtext/tests/figs/textbox-grob/multiple-boxes-left-rotated-internal-alignment.svg
/usr/lib64/R/library/gridtext/tests/figs/textbox-grob/multiple-boxes-right-rotated-internal-alignment.svg
/usr/lib64/R/library/gridtext/tests/figs/textbox-grob/rotation-around-fixed-point.svg
/usr/lib64/R/library/gridtext/tests/testthat.R
/usr/lib64/R/library/gridtext/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/gridtext/tests/testthat/test-get_file.R
/usr/lib64/R/library/gridtext/tests/testthat/test-grid-constructors.R
/usr/lib64/R/library/gridtext/tests/testthat/test-grid-renderer.R
/usr/lib64/R/library/gridtext/tests/testthat/test-null-box.R
/usr/lib64/R/library/gridtext/tests/testthat/test-raster-box.R
/usr/lib64/R/library/gridtext/tests/testthat/test-rect-box.R
/usr/lib64/R/library/gridtext/tests/testthat/test-richtext-grob.R
/usr/lib64/R/library/gridtext/tests/testthat/test-text-details.R
/usr/lib64/R/library/gridtext/tests/testthat/test-textbox-grob.R
/usr/lib64/R/library/gridtext/tests/testthat/test-vbox.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gridtext/libs/gridtext.so
