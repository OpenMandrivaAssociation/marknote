Name: marknote
Version: 1.3.0
Release: 1
Source0: https://download.kde.org/stable/marknote/%{name}-%{version}.tar.xz
Summary: Note taking tool with MarkDown formatting support
URL: https://invent.kde.org/office/marknote
License: GPL-3.0
Group: Office
BuildRequires: cmake ninja
BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(KF6BreezeIcons)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KPim6Mime)
BuildRequires: pkgconfig(md4c)

%description
Write down your thoughts.

Marknote supports a wide range of formating options usefully for taking every
day notes, like bold, italic, underlined and strike through fonts as well as
headings, lists, check boxes, images and more.

%files -f %{name}.lang
%{_bindir}/marknote
%{_datadir}/applications/org.kde.marknote.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.marknote.svg
%{_datadir}/metainfo/org.kde.marknote.metainfo.xml
%{_datadir}/qlogging-categories6/marknote.categories
