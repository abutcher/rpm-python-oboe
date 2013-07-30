%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-oboe
Version:        1.3.8
Release:        1%{?dist}
Summary:        AppNeta Traceview instrumentation libraries for Python

Group:          Development/Libraries
License:        GPLv2+
URL:            https://pypi.python.org/pypi/oboe
Source0:        dist/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-setuptools
Requires:       rpm-build
BuildArch:      noarch


%description
The 'oboe' and 'oboeware' modules provide support for instrumenting
programs for use with the Tracelytics Oboe instrumentation library.

The oboe module provides a Pythonic interface to liboboe for C, and
the oboeware module provides middleware and other components for
popular web frameworks such as Django, Tornado, Pylons, and WSGI.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Mon Jul 29 2013 Andrew Butcher <abutcher@redhat.com> - 1.3.8
- Initial packaging.
