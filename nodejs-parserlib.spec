# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename parserlib

Name:               nodejs-parserlib
Version:            0.2.5
Release:            1%{?dist}
Summary:            CSS3 SAX-inspired parser

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/parserlib
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6


%description
CSS Parser

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/parserlib
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/parserlib

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
ant -f ../../build.xml test
%endif

%files
%doc README.md
%{nodejs_sitelib}/parserlib/

%changelog
* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.2.5-1
- Initial packaging for Fedora.
