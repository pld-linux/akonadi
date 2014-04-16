%define		snap		svn1057960
%define		qtver		4.8.1
Summary:	Akonadi - The PIM Storage Service
Summary(pl.UTF-8):	Akonadi - usługa przechowywania danych dla aplikacji PIM
Name:		akonadi
Version:	1.12.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/akonadi/src/%{name}-%{version}.tar.bz2
# Source0-md5:	9a4a99d10e003a267a515fc60de4f817
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/akonadi/
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
URL:		http://pim.kde.org/akonadi/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	boost-devel
#BuildRequires:	clucene-core-devel >= 0.9.16a-2
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libxslt-progs
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	shared-mime-info
BuildRequires:	soprano-devel >= 2.4.64
Requires:	%{name}-libs = %{version}-%{release}
Requires:	QtSql-mysql
Requires:	mysql
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
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files needed to build Akonadi client libraries and
applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia bibliotek klienckich i aplikacji
używających Akonadi.

%package libs
Summary:	Akonadi libraries
Summary(pl.UTF-8):	Biblioteki Akonadi
Group:		Libraries

%description libs
Akonadi libraries.

%description libs -l pl.UTF-8
Biblioteki Akonadi.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DINSTALL_QSQLITE_IN_QT_PREFIX=%{_libdir}/qt4/plugins \
	-DMYSQLD_EXECUTABLE=/usr/sbin/mysqld \
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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_agent_launcher
%attr(755,root,root) %{_bindir}/akonadi_agent_server
%attr(755,root,root) %{_bindir}/akonadi_control
%attr(755,root,root) %{_bindir}/akonadi_rds
%attr(755,root,root) %{_bindir}/akonadictl
%attr(755,root,root) %{_bindir}/akonadiserver
%attr(755,root,root) %{_bindir}/asapcat
%dir %{_datadir}/config/akonadi
%{_datadir}/config/akonadi/mysql-global.conf
%{_datadir}/config/akonadi/mysql-global-mobile.conf
%{_datadir}/mime/packages/akonadi-mime.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libakonadiprotocolinternals.so.?
%attr(755,root,root) %{_libdir}/libakonadiprotocolinternals.so.*.*.*
%attr(755,root,root) %{_libdir}/qt4/plugins/sqldrivers/libqsqlite3.so
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.AgentManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Search.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Status.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.NotificationManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.NotificationSource.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Preprocessor.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Resource.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Tracer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Control.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.ControlManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.DebugInterface.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Server.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.StorageDebugger.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.TracerNotification.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakonadiprotocolinternals.so
%{_libdir}/cmake/Akonadi
%{_includedir}/akonadi
%{_pkgconfigdir}/akonadi.pc
