%define _disable_ld_no_undefined 1

Summary:	Editor for manipulating PDF documents
Name:		pdfedit
Version:	0.4.5
Release:	4
License:	GPLv2
Group:		Publishing
URL:		https://sourceforge.net/projects/pdfedit
Source:		http://downloads.sourceforge.net/pdfedit/%{name}-%{version}.tar.bz2
Patch0:		pdfedit-0.4.5-gcc4.7.patch
Patch1:		pdfedit-0.4.5-undef.patch
BuildRequires:	qt3-devel
BuildRequires:	boost-devel
BuildRequires:	libt1lib-devel

%description
PDFedit is a free editor for PDF documents. You can change raw 
pdf objects (for advanced users) or use many gui functions.
Functionality can be easily extended using a scripting 
language (ECMAScript).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
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
install -d -m 0755 $%{buildroot}{%{_bindir},%{_libdir},%{_datadir}}
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
Categories=X-MandrivaLinux-Office-Publishing;Office;Publishing;
EOF

for i in 16 32 48; do
    mkdir -p %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps
    install -m 644 src/gui/icon/pdfedit_icon_$i.png %{buildroot}%{_iconsdir}/hicolor/"$i"x"$i"/apps/pdfedit.png
done

%files
%{_bindir}/pdfedit
%{_mandir}/man1/pdfedit.*
%{_datadir}/doc/pdfedit/*
%{_datadir}/pdfedit/*
%{_datadir}/applications/pdfedit.*
%{_iconsdir}/hicolor/*/apps/pdfedit.png


