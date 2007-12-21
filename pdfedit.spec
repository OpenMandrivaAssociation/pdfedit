%define name	pdfedit
%define version	0.3.2
%define release 1

Summary: 	Editor for manipulating PDF documents
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
License: 	GPL
Group: 		Publishing
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://pdfedit.petricek.net
Requires: 	qt3
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: 	qt3-devel, boost-devel

%description
Editor for manipulating PDF documents.

%prep
%setup -q

%build
%ifarch x86_64
export QMAKESPEC=/usr/lib/qt3/mkspecs/linux-g++-64
%else
export QMAKESPEC=/usr/lib/qt3/mkspecs/linux-g++-32
%endif
%configure 
%make  

%install
%__rm -rf %{buildroot}

%__install -d -m 0755 $%{buildroot}{%{_bindir},%{_libdir},%{_datadir}}
%make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=PDFedit
Comment=Editor for manipulating PDF documents
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
MimeType=application/x-pdf;application/pdf;
Categories=X-MandrivaLinux-Office-Publishing;Graphics;Publishing;
EOF

mkdir -p %{buildroot}%{_iconsdir}/{mini,large}
%__install -m644 src/gui/icon/pdfedit_icon_32.png %{buildroot}%{_iconsdir}/pdfedit.png
%__install -m644 src/gui/icon/pdfedit_icon_16.png %{buildroot}%{_miconsdir}/pdfedit.png
%__install -m644 src/gui/icon/pdfedit_icon_48.png %{buildroot}%{_liconsdir}/pdfedit.png

%post
%{update_menus}

%postun
%{clean_menus}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_bindir}/pdfedit
%{_mandir}/man1/pdfedit.*
%{_datadir}/doc/pdfedit/*
%{_datadir}/pdfedit/*
%{_datadir}/applications/mandriva*
%{_iconsdir}/pdfedit.png
%{_miconsdir}/pdfedit.png
%{_liconsdir}/pdfedit.png

