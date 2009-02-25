Summary:	Editor for manipulating PDF documents
Name:		pdfedit
Version:	0.4.2
Release:	%mkrel 1
License:	GPLv2
Group:		Publishing
URL: 		http://sourceforge.net/projects/pdfedit
Source: 	http://downloads.sourceforge.net/pdfedit/%{name}-%{version}.tar.bz2
Requires:	qt3
BuildRequires:	qt3-devel
BuildRequires:	boost-devel
BuildRequires:	libt1lib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PDFedit is a free editor for PDF documents. You can change raw 
pdf objects (for advanced users) or use many gui functions.
Functionality can be easily extended using a scripting 
language (ECMAScript).

%prep
%setup -q

%build
%ifarch x86_64
export QMAKESPEC=%{qt3dir}/mkspecs/linux-g++-64
%else
export QMAKESPEC=%{qt3dir}/mkspecs/linux-g++-32
%endif

export QTDIR=%{qt3dir}

%configure2_5x \
	--enable-release \
	--enable-stack-protector \
	--enable-qt3 \
	--with-parallel-make=auto
%make

%install
%__rm -rf %{buildroot}

%__install -d -m 0755 $%{buildroot}{%{_bindir},%{_libdir},%{_datadir}}
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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

for i in 16 32 48; do
    mkdir -p %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps
    %__install -m 644 src/gui/icon/pdfedit_icon_$i.png %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps/pdfedit.png
done

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_bindir}/pdfedit
%{_mandir}/man1/pdfedit.*
%{_datadir}/doc/pdfedit/*
%{_datadir}/pdfedit/*
%{_datadir}/applications/pdfedit.*
%{_iconsdir}/hicolor/*/apps/pdfedit.png
