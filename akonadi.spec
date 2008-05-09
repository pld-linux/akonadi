%define		qtbrver		4.4.0

Summary:	Akonadi
Summary(pl.UTF-8):	Akonadi
Name:		akonadi
Version:	0.80.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/4.0.71/support/%{name}-%{version}.tar.bz2
# Source0-md5:	0aba67ad18dcba35b8b1b52b9c126e1b
URL:		http://pim.kde.org/akonadi/
BuildRequires:	QtCore-devel >= %{qtbrver}
BuildRequires:	QtDBus-devel >= %{qtbrver}
BuildRequires:	QtNetwork-devel >= %{qtbrver}
BuildRequires:	QtTest-devel >= %{qtbrver}
#BuildRequires:	clucene-core-devel >= 0.9.16a-2
BuildRequires:	cmake
BuildRequires:	qt4-build >= %{qtbrver}
BuildRequires:	qt4-qmake >= %{qtbrver}
BuildRequires:	rpmbuild(macros) >= 1.293
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
%attr(755,root,root) %ghost %{_libdir}/libakonadiprivate.so.0
%attr(755,root,root) %{_libdir}/libakonadiprivate.so.0.80.0
%attr(755,root,root) %ghost %{_libdir}/libakonadiprotocolinternals.so.0
%attr(755,root,root) %{_libdir}/libakonadiprotocolinternals.so.0.80.0
%dir %{_datadir}/config/akonadi
%{_datadir}/config/akonadi/mysql-global.conf
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Agent.Control.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Agent.Status.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.AgentManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.ControlManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.NotificationManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Resource.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Search.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.SearchQuery.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.SearchQueryIterator.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Server.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Tracer.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.TracerNotification.xml
%{_datadir}/dbus-1/services/org.kde.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml

%files devel
%defattr(644,root,root,755)
%{_libdir}/libakonadiprivate.so
%{_libdir}/libakonadiprotocolinternals.so
%{_includedir}/akonadi
