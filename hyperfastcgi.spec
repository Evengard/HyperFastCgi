Name:           mono-webserver-hyperfastcgi
Url:            https://github.com/xplicit/HyperFastCgi
License:        X11/MIT
Group:          Productivity/Networking/Web/Servers
Version:        0.4
Release:        2
Summary:        Mono WebServer HyperFastCgi
Source:         %{name}-%{version}-%{release}.tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#BuildRequires:  mono-devel

# To build the tar, you can use : 
# git archive --format=tar --prefix=mono-webserver-hyperfastcgi-0.4-2/ master > ~/rpmbuild/SOURCES/mono-webserver-hyperfastcgi-0.4-2.tar

%global _binaries_in_noarch_packages_terminate_build 0

%description
Performant nginx to mono fastcgi server

%prep
%setup -q -n %{name}-%{version}-%{release}
./autogen.sh --prefix=/usr

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
echo "#!/bin/sh" > %{buildroot}%{_bindir}/hyperfastcgi4
echo 'exec %{_bindir}/mono $MONO_OPTIONS "%{_prefix}/lib/mono/gac/HyperFastCgi/0.4.4.0__0738eb9f132ed756/HyperFastCgi.exe" "$@"' >> %{buildroot}%{_bindir}/hyperfastcgi4
chmod +x %{buildroot}%{_bindir}/hyperfastcgi4
make install DESTDIR=$DESTDIR

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/hyperfastcgi4
%{_prefix}/lib/mono/4.5/HyperFastCgi.exe
%{_prefix}/lib/mono/gac/HyperFastCgi/*
%{_prefix}/lib/hyperfastcgi/4.0/HyperFastCgi.exe
%{_prefix}/lib/libhfc-native.*

%changelog
