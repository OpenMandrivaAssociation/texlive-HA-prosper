Name:		texlive-HA-prosper
Version:	59651
Release:	2
Summary:	Patches and improvements for prosper
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ha-prosper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ha-prosper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ha-prosper.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ha-prosper.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/ha-prosper
%doc %{_texmfdistdir}/doc/latex/ha-prosper
#- source
%doc %{_texmfdistdir}/source/latex/ha-prosper

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
