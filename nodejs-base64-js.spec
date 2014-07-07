%global enable_tests 0

%global barename base64-js

Name:               nodejs-base64-js
Version:            0.0.7
Release:            1%{?dist}
Summary:            Base64 encoding/decoding in pure JS

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/base64-js
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:      nodejs-tape
%endif


%description
base64-js
=========

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/


%if 0%{?enable_tests}
%nodejs_fixdep --dev tape
%else
%nodejs_fixdep --dev -r tape
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/base64-js
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/base64-js

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
tape test/*.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/base64-js/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.0.7-1
- Initial packaging for Fedora.