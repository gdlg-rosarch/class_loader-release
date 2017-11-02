Name:           ros-kinetic-class-loader
Version:        0.3.7
Release:        0%{?dist}
Summary:        ROS class_loader package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/class_loader
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       poco-devel
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  poco-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-cmake-modules >= 0.3.3

%description
The class_loader package is a ROS-independent package for loading plugins during
runtime and the foundation of the higher level ROS &quot;pluginlib&quot;
library. class_loader utilizes the host operating system's runtime loader to
open runtime libraries (e.g. .so/.dll files), introspect the library for
exported plugin classes, and allows users to instantiate objects of said
exported classes without the explicit declaration (i.e. header file) for those
classes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Nov 02 2017 Mikael Arguedas <mikael@osrfoundation.org> - 0.3.7-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 0.3.6-0
- Autogenerated by Bloom

* Tue Sep 20 2016 Mikael Arguedas <mikael@osrfoundation.org> - 0.3.5-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 0.3.4-0
- Autogenerated by Bloom

* Thu Mar 10 2016 Mikael Arguedas <mikael@osrfoundation.org> - 0.3.3-0
- Autogenerated by Bloom

* Wed Mar 09 2016 Esteve Fernandez <esteve@osrfoundation.org> - 0.3.2-0
- Autogenerated by Bloom

