%global tl_name haranoaji
%global tl_revision 76078

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20250811
Release:	%{tl_revision}.1
Summary:	Harano Aji Fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/haranoaji
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/haranoaji.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/haranoaji.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are fonts
obtained by replacing Adobe-Identity-0 (AI0) CIDs of Source Han fonts
(Source Han Serif and Source Han Sans) with Adobe-Japan1 (AJ1) CIDs.
There are 14 fonts, 7 weights each for Mincho and Gothic.

