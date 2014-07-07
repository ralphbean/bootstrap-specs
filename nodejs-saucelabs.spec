%global enable_tests 0

%global barename saucelabs

Name:               nodejs-saucelabs
Version:            0.1.1
Release:            1%{?dist}
Summary:            A wrapper around Sauce Labs REST API

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/saucelabs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:      nodejs-mocha
BuildRequires:      nodejs-chai
BuildRequires:      nodejs-jshint
BuildRequires:      nodejs-nock
%endif


%description
node-saucelabs
========

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/


%if 0%{?enable_tests}
%nodejs_fixdep --dev mocha
%nodejs_fixdep --dev chai
%nodejs_fixdep --dev jshint
%nodejs_fixdep --dev nock
%else
%nodejs_fixdep --dev -r mocha
%nodejs_fixdep --dev -r chai
%nodejs_fixdep --dev -r jshint
%nodejs_fixdep --dev -r nock
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/saucelabs
cp -pr package.json lib index.js \
    %{buildroot}%{nodejs_sitelib}/saucelabs

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
make lint test
%endif


%files
%doc README.md
%{nodejs_sitelib}/saucelabs/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- Initial packaging for Fedora.
