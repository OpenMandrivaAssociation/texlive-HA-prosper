# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ha-prosper
# catalog-date 2006-12-03 19:48:14 +0100
# catalog-license lppl
# catalog-version 4.21
Name:		texlive-HA-prosper
Version:	4.21
Release:	5
Summary:	Patches and improvements for prosper
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ha-prosper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/HA-prosper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/HA-prosper.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/HA-prosper.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
HA-prosper is a patch for prosper that adds new functionality
to prosper based presentations. Among the new features you will
find automatic generation of a table of contents on each slide,
support for notes and portrait slides. The available styles
demonstrate how to expand the functionality of prosper even
further.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/HA-prosper/HA-prosper.cfg
%{_texmfdistdir}/tex/latex/HA-prosper/HA-prosper.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Aggie/AMLogo.eps
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Aggie/HAPAggie.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Aggie/files.txt
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Capsules/HAPcapsules.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Ciment/HAPciment.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Fyma/HAPFyma.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/HA/HAPHA.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/HA/flower.ps
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Lakar/HAPLakar.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Simple/HAPsimple.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/TCS/HAPTCS.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/TCS/HAPTCSTealBlue.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/TCS/HAPTCSgrad.sty
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/TCS/TCSgradlogo.ps
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/TCS/TCSlogo.ps
%{_texmfdistdir}/tex/latex/HA-prosper/Styles/Tycja/HAPTycja.sty
%doc %{_texmfdistdir}/doc/latex/HA-prosper/HA-prosper.pdf
%doc %{_texmfdistdir}/doc/latex/HA-prosper/HAPBigtest.tex
%doc %{_texmfdistdir}/doc/latex/HA-prosper/HAPDualslide.tex
%doc %{_texmfdistdir}/doc/latex/HA-prosper/HAPIntroduction.tex
%doc %{_texmfdistdir}/doc/latex/HA-prosper/README
#- source
%doc %{_texmfdistdir}/source/latex/HA-prosper/HA-prosper.def
%doc %{_texmfdistdir}/source/latex/HA-prosper/HA-prosper.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.21-2
+ Revision: 752460
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.21-1
+ Revision: 718598
- texlive-HA-prosper
- texlive-HA-prosper
- texlive-HA-prosper
- texlive-HA-prosper
- texlive-HA-prosper

