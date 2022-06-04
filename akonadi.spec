%define		snap		svn1057960
%define		qtver		4.8.1
Summary:	Akonadi - The PIM Storage Service
Summary(pl.UTF-8):	Akonadi - usługa przechowywania danych dla aplikacji PIM
Name:		akonadi
Version:	1.13.0
Release:	20
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/akonadi/src/%{name}-%{version}.tar.bz2
# Source0-md5:	84eb2e471bd6bdfe54a2a2f1d858c07d
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/akonadi/
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
Patch1:		0001-FindSqlite-Use-CMAKE_FLAGS-the-right-way-in-try_comp.patch
Patch2:		0002-Do-not-enter-the-test-directories-if-AKONADI_BUILD_T.patch
Patch3:		0003-STORE-Allow-modifying-items-tags-via-Tag-RID-or-GID.patch
Patch4:		0004-Fix-typo-in-if-condition.patch
Patch5:		0005-Fix-buffer-overflow-in-AKTEST_FAKESERVER_MAIN.patch
Patch6:		0006-Don-t-crash-when-setmntent-returns-NULL.patch
Patch7:		0007-Don-t-call-insert-from-Q_ASSERT-breaks-unit-tests-in.patch
Patch8:		0008-Suppress-unused-variable-warnings-in-release-mode.patch
Patch9:		0009-Test-whether-compiler-supports-all-required-C-11-fea.patch
Patch10:	0010-prevent-starting-a-QTimer-with-a-negative-interval.patch
Patch11:	0011-Convert-some-qDebugs-to-akDebugs.patch
Patch12:	0012-Optimize-Reduce-the-amount-of-allocations-required-t.patch
Patch13:	0013-Intern-entity-strings-for-table-and-column-names.patch
Patch14:	0014-No-semicolon-after-Q_DECLARE_METATYPE.patch
Patch15:	0015-Use-QMutexLocker-instead-of-manual-lock-unlock-calls.patch
Patch16:	0016-Use-an-QAtomicInt-instead-of-a-plain-bool-for-Entity.patch
Patch17:	0017-Optimize-Only-do-one-hash-lookup-to-retrieve-value-f.patch
Patch18:	0018-Optimize-Skip-value-condition-on-invalid-flags.patch
Patch19:	0019-Optimize-queries-Do-not-retrieve-known-key-used-in-t.patch
Patch20:	0020-Avoid-ridiculous-amount-of-SQL-queries-by-caching-Pa.patch
Patch21:	0021-Implement-support-for-CASE.WHEN.THEN-SQL-statements-.patch
Patch22:	0022-Implement-cache-for-CollectionStatistics-to-signific.patch
Patch23:	0023-Always-create-a-new-PartType-when-it-does-not-exist.patch
Patch24:	0024-Fix-compilation-with-strict-iterators.patch
Patch25:	0025-Avoid-repeated-calls-to-PimItem-flags-and-PimItem-ta.patch
Patch26:	0026-Avoid-recursive-collection-listing-in-SearchHelper.patch
Patch27:	0027-Minor-improvements-in-StatisticsCache-as-suggested-b.patch
Patch28:	0028-Extend-imapparser-benchmark-and-keep-static-data-aro.patch
Patch29:	0029-Reduce-the-amount-of-allocations-by-preallocating-a-.patch
Patch30:	0030-Preallocate-a-capacity-of-16-for-the-returned-list.patch
Patch31:	moc.patch
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
Conflicts:	ka5-akonadi >= 21
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1

%build
install -d build
cd build
%cmake \
	-DWITH_SOPRANO=on \
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

install -d $RPM_BUILD_ROOT%{_libdir}/kde4/akonadi

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
%dir %{_libdir}/kde4/akonadi
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
