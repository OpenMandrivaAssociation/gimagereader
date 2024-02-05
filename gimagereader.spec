%define tname gImageReader
%define oname %(echo %{tname} | tr [:upper:] [:lower:] )

Summary:	A simple Gtk/Qt front-end to tesseract-ocr
Name:		%{oname}
Version:	3.4.1
Release:	1
License:	GPLv3+
Group:		Office
URL:		https://github.com/manisandro/%{name}
Source0:	https://github.com/manisandro/gImageReader/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:		%{name}-3.1.2-qt_pi.patch
# (rosa)
Patch1:		gimagereader-3.4.1-dic-path.patch
# PoDoFo 0.10 support (fedora)
Patch10:	0001-Qt-Add-support-for-PoDoFo-0.10.x.patch
Patch11:	0002-Qt-Drop-PoDoFo-0.9.3-code-path.patch
Patch12:	0003-Gtk-Add-support-for-PoDoFo-0.10.x.patch
Patch13:	0004-Gtk-Drop-PoDoFo-0.9.3-code-path.patch

BuildRequires:	appstream-util
BuildRequires:	cmake ninja
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gomp-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(libpodofo)
BuildRequires:	pkgconfig(tesseract)
BuildRequires:	pkgconfig(sane-backends)
BuildRequires:	python%{pyver}dist(pygobject)
#BuildRequires:	libappstream-glib
# gtk interface
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(gtksourceviewmm-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(gtkspellmm-3.0) >= 3.0.4
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(poppler-glib)
# qt5 interface
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(quazip-qt5)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(QtSpell-qt5)
# qt6 interface
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(quazip-qt6)
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(QtSpell-qt6)

%description
gImageReader is a simple Gtk/Qt front-end to tesseract-ocr.

Features include:
  · Import PDF documents and images from disk, scanning devices, clipboard
    and screenshots
  · Process multiple images and documents in one go
  · Manual or automatic recognition area definition
  · Recognize to plain text or to hOCR documents
  · Recognized text displayed directly next to the image
  · Post-process the recognized text, including spellchecking
  · Generate PDF documents from hOCR documents

#----------------------------------------------------------------------------

%package gtk
Summary:	A Gtk+ front-end to tesseract-ocr
Requires:	%{name}-shared = %{version}-%{release}

%description gtk
gImageReader is a simple Gtk/Qt front-end to tesseract-ocr.

Features include:

  · Import PDF documents and images from disk, scanning devices, clipboard
    and screenshots
  · Process multiple images and documents in one go
  · Manual or automatic recognition area definition
  · Recognize to plain text or to hOCR documents
  · Recognized text displayed directly next to the image
  · Post-process the recognized text, including spellchecking
  · Generate PDF documents from hOCR documents

This package contains the Gtk+ front-end.

%files gtk
%{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_metainfodir}/%{name}-gtk.appdata.xml

#----------------------------------------------------------------------------

%package qt5
Summary:	A Qt5 front-end to tesseract-ocr
Requires:	%{name}-shared = %{version}-%{release}

%description qt5
gImageReader is a simple Gtk/Qt front-end to tesseract-ocr.

Features include:

  · Import PDF documents and images from disk, scanning devices, clipboard
    and screenshots
  · Process multiple images and documents in one go
  · Manual or automatic recognition area definition
  · Recognize to plain text or to hOCR documents
  · Recognized text displayed directly next to the image
  · Post-process the recognized text, including spellchecking
  · Generate PDF documents from hOCR documents

This package contains the Qt5 front-end.

%files qt5
%{_bindir}/%{name}-qt5
%{_datadir}/applications/%{name}-qt5.desktop
%{_metainfodir}/%{name}-qt5.appdata.xml

#----------------------------------------------------------------------------

%package qt6
Summary:	A Qt6 front-end to tesseract-ocr
Requires:	%{name}-shared = %{version}-%{release}

%description qt6
gImageReader is a simple Gtk/Qt front-end to tesseract-ocr.

Features include:

  · Import PDF documents and images from disk, scanning devices, clipboard
    and screenshots
  · Process multiple images and documents in one go
  · Manual or automatic recognition area definition
  · Recognize to plain text or to hOCR documents
  · Recognized text displayed directly next to the image
  · Post-process the recognized text, including spellchecking
  · Generate PDF documents from hOCR documents

This package contains the Qt6 front-end.

%files qt6
%{_bindir}/%{name}-qt6
%{_datadir}/applications/%{name}-qt6.desktop
%{_metainfodir}/%{name}-qt6.appdata.xml

#----------------------------------------------------------------------------

%package shared
Summary:	Shared files for %{name}
BuildArch:	noarch

%description shared
Shared files files for %{name}.

%files shared -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_docdir}/%{name}-shared/manual*.html
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%autosetup -p1

# fix include path
sed -i -e "s,#include <podofo/base/,#include <podofo/main/," gtk/src/hocr/HOCRPdfExporter.cc

%build
for i in gtk qt5 qt6
do
	CMAKE_BUILD_DIR=build-$i \
	%cmake \
		-DINTERFACE_TYPE=$i \
		-DENABLE_VERSIONCHECK:BOOL=FALSE \
		-DMANUAL_DIR="%{_docdir}/%{name}-shared" \
		-GNinja
	%ninja_build
	cd ..
done

%install
for i in gtk qt5 qt6
do
	%ninja_install -C build-$i
done

# locales
%find_lang %{name} --all-name

