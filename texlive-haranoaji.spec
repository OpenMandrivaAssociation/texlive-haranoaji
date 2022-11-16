Name:		texlive-haranoaji
Version:	62100
Release:	1
Summary:	Harano Aji Fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/haranoaji
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/haranoaji.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/haranoaji.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are
fonts obtained by replacing Adobe-Identity-0 (AI0) CIDs of
Source Han fonts (Source Han Serif and Source Han Sans) with
Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7 weights each for
Mincho and Gothic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/haranoaji
%{_texmfdistdir}/texmf-dist/fonts/opentype/public/haranoaji
%doc %{_texmfdistdir}/texmf-dist/doc/fonts/haranoaji

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
