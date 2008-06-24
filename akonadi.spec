%define		qtbrver		4.4.0
Summary:	Akonadi
Summary(pl.UTF-8):	Akonadi
Name:		akonadi
Version:	0.82.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/4.0.83/support/%{name}-%{version}.tar.bz2
# Source0-md5:	a6ab075c69a54abc024285a76673110b
Patch0:		%{name}-lib64.patch
URL:		http://pim.kde.org/akonadi/
BuildRequires:	QtCore-devel >= %{qtbrver}
BuildRequires:	QtDBus-devel >= %{qtbrver}
BuildRequires:	QtNetwork-devel >= %{qtbrver}
BuildRequires:	QtSql-devel >= %{qtbrver}
BuildRequires:	QtTest-devel >= %{qtbrver}
#BuildRequires:	clucene-core-devel >= 0.9.16a-2
BuildRequires:	cmake
BuildRequires:	kde4-automoc
BuildRequires:	libxslt-progs
#BuildRequires:	mysql
BuildRequires:	qt4-build >= %{qtbrver}
BuildRequires:	qt4-qmake >= %{qtbrver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Akonadi.

%description -l pl.UTF-8
Akonadi.

%package devel
Summary:	Header files for akonadi
Summary(pl.UTF-8):	Pliki nagłówkowe dla akonadi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for akonadi.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla akonadi.

%prep
%setup -q
%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
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
%{_pkgconfigdir}/akonadi.pc
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Control.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Status.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.AgentManager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.ControlManager.xml
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
%{_libdir}/libakonadiprivate.so
%{_libdir}/libakonadiprotocolinternals.so
%{_includedir}/akonadi
