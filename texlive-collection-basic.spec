Name:		texlive-collection-basic
Epoch:		1
Version:	59159
Release:	2
Summary:	Essential programs and files
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-basic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-amsfonts
Requires:	texlive-bibtex
Requires:	texlive-cm
Requires:	texlive-dvipdfmx
Requires:	texlive-dvipdfmx-def
Requires:	texlive-dvips
Requires:	texlive-enctex
Requires:	texlive-etex
Requires:	texlive-etex-pkg
Requires:	texlive-glyphlist
Requires:	texlive-gsftopk
Requires:	texlive-hyph-utf8
Requires:	texlive-hyphen-base
Requires:	texlive-ifluatex
Requires:	texlive-ifxetex
Requires:	texlive-knuth-lib
Requires:	texlive-knuth-local
Requires:	texlive-kpathsea
Requires:	texlive-lua-alt-getopt
Requires:	texlive-luatex
Requires:	texlive-makeindex
Requires:	texlive-metafont
Requires:	texlive-mflogo
Requires:	texlive-mfware
Requires:	texlive-pdftex
Requires:	texlive-plain
Requires:	texlive-tetex
Requires:	texlive-tex
Requires:	texlive-texconfig
Requires:	texlive-texlive-common
Requires:	texlive-texlive-docindex
Requires:	texlive-texlive-en
Requires:	texlive-texlive-scripts
Requires:	texlive-xdvi

%description
These files are regarded as basic for any TeX system, covering
plain TeX macros, Computer Modern fonts, and configuration for
common drivers; no LaTeX.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
