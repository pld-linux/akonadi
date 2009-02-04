%define		qtbrver		4.4.0
Summary:	Akonadi - The PIM Storage Service
Summary(pl.UTF-8):	Akonadi - usługa przechowywania danych dla aplikacji PIM
Name:		akonadi
Version:	1.1.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://akonadi.omat.nl/%{name}-%{version}.tar.bz2
# Source0-md5:	2e98b42cec9ec4e60a2e3c096f1a3106
URL:		http://pim.kde.org/akonadi/
BuildRequires:	QtCore-devel >= %{qtbrver}
BuildRequires:	QtDBus-devel >= %{qtbrver}
BuildRequires:	QtNetwork-devel >= %{qtbrver}
BuildRequires:	QtSql-devel >= %{qtbrver}
BuildRequires:	QtTest-devel >= %{qtbrver}
BuildRequires:	automoc4
#BuildRequires:	clucene-core-devel >= 0.9.16a-2
BuildRequires:	cmake >= 2.6.2
BuildRequires:	libxslt-progs
BuildRequires:	mysql-devel
BuildRequires:	qt4-build >= %{qtbrver}
BuildRequires:	qt4-qmake >= %{qtbrver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Akonadi is a personal information management (PIM) framework for KDE
4.1 and newer. Akonadi will function as an extensible data storage for
all PIM applications.

Besides data storage, Akonadi has several other components including
search, and a library (cache) for easy access and notification of data
changes.

%description -l pl.UTF-8
Akonadi do szkielet zarządzania informacjami osobistymi (PIM) dla KDE
w wersji 4.1 i nowszych. Działa jako rozszerzalny system
przechowywania danych dla wszystkich aplikacji PIM.

Poza przechowywaniem danych Akonadi ma kilka innych komponentów, w tym
wyszukiwanie oraz bibliotekę (pamięć podręczną) w celu łatwego dostępu
i powiadamiania i zmianie danych.

%package devel
Summary:	Header files for Akonadi
Summary(pl.UTF-8):	Pliki nagłówkowe dla Akonadi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed to build Akonadi client libraries and
applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia bibliotek klienckich i aplikacji
używających Akonadi.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DMYSQLD_EXECUTABLE=/usr/bin/mysqld \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_control
%attr(755,root,root) %{_bindir}/akonadictl
%attr(755,root,root) %{_bindir}/akonadiserver
%attr(755,root,root) %ghost %{_libdir}/libakonadiprivate.so.?
%attr(755,root,root) %{_libdir}/libakonadiprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadiprotocolinternals.so.?
%attr(755,root,root) %{_libdir}/libakonadiprotocolinternals.so.*.*.*
%dir %{_datadir}/config/akonadi
%{_datadir}/config/akonadi/mysql-global.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Control.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Status.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.AgentManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.ControlManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.DebugInterface.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.NotificationManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Resource.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Search.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.SearchQuery.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.SearchQueryIterator.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Server.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Tracer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.TracerNotification.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakonadiprivate.so
%attr(755,root,root) %{_libdir}/libakonadiprotocolinternals.so
%{_includedir}/akonadi
%{_pkgconfigdir}/akonadi.pc
