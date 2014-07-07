%global enable_tests 0

%global barename postcss

Name:               nodejs-postcss
Version:            1.0.0
Release:            1%{?dist}
Summary:            Framework for CSS postprocessors with full source map support

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/postcss
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-source-map
BuildRequires:      nodejs-base64-js

Requires:           nodejs-source-map
Requires:           nodejs-base64-js

%if 0%{?enable_tests}
BuildRequires:      nodejs-cssom
BuildRequires:      nodejs-fs-extra
BuildRequires:      nodejs-gonzales
BuildRequires:      nodejs-rework
BuildRequires:      nodejs-should
BuildRequires:      nodejs-mocha
%endif


%description
PostCSS is a framework for CSS postprocessors, to modify CSS with JavaScript
with full source map support.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep source-map
%nodejs_fixdep base64-js

%if 0%{?enable_tests}
%nodejs_fixdep --dev cssom
%nodejs_fixdep --dev fs-extra
%nodejs_fixdep --dev gonzales
%nodejs_fixdep --dev rework
%nodejs_fixdep --dev should
%nodejs_fixdep --dev mocha
%else
%nodejs_fixdep --dev -r cssom
%nodejs_fixdep --dev -r fs-extra
%nodejs_fixdep --dev -r gonzales
%nodejs_fixdep --dev -r rework
%nodejs_fixdep --dev -r should
%nodejs_fixdep --dev -r mocha
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/postcss
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/postcss

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
mocha
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/postcss/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
