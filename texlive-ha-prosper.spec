%global tl_name ha-prosper
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.21
Release:	%{tl_revision}.1
Summary:	Patches and improvements for prosper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ha-prosper
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ha-prosper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ha-prosper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ha-prosper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
HA-prosper is a patch for prosper that adds new functionality to prosper
based presentations. Among the new features you will find automatic
generation of a table of contents on each slide, support for notes and
portrait slides. The available styles demonstrate how to expand the
functionality of prosper even further.

