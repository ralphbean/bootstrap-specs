%global enable_tests 0

%global barename grunt-saucelabs

Name:               nodejs-grunt-saucelabs
Version:            8.1.0
Release:            1%{?dist}
Summary:            Grunt task running tests using Sauce Labs

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-saucelabs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-saucelabs
BuildRequires:      nodejs-q
BuildRequires:      nodejs-colors
BuildRequires:      nodejs-lodash
BuildRequires:      nodejs-sauce-tunnel
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-request

Requires:           nodejs-saucelabs
Requires:           nodejs-q
Requires:           nodejs-colors
Requires:           nodejs-lodash
Requires:           nodejs-sauce-tunnel
Requires:           nodejs-grunt
Requires:           nodejs-request

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-sauce-tunnel
BuildRequires:      nodejs-grunt-contrib-watch
BuildRequires:      nodejs-grunt-contrib-connect
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt-jscs-checker
BuildRequires:      nodejs-publish
BuildRequires:      nodejs-merge
BuildRequires:      nodejs-load-grunt-config
BuildRequires:      nodejs-grunt
%endif


%description
A Grunt task for running QUnit, Jasmine, Mocha, YUI tests, or any framework
using Sauce Labs' Cloudified Browsers.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep saucelabs
%nodejs_fixdep q
%nodejs_fixdep colors
%nodejs_fixdep lodash
%nodejs_fixdep sauce-tunnel
%nodejs_fixdep grunt
%nodejs_fixdep request

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-sauce-tunnel
%nodejs_fixdep --dev grunt-contrib-watch
%nodejs_fixdep --dev grunt-contrib-connect
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt-jscs-checker
%nodejs_fixdep --dev publish
%nodejs_fixdep --dev merge
%nodejs_fixdep --dev load-grunt-config
%nodejs_fixdep --dev grunt
%else
%nodejs_fixdep --dev -r grunt-sauce-tunnel
%nodejs_fixdep --dev -r grunt-contrib-watch
%nodejs_fixdep --dev -r grunt-contrib-connect
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt-jscs-checker
%nodejs_fixdep --dev -r publish
%nodejs_fixdep --dev -r merge
%nodejs_fixdep --dev -r load-grunt-config
%nodejs_fixdep --dev -r grunt
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-saucelabs
cp -pr package.json tasks Gruntfile.js \
    %{buildroot}%{nodejs_sitelib}/grunt-saucelabs

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-saucelabs/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 8.1.0-1
- Initial packaging for Fedora.
