# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename grunt-saucelabs

Name:               nodejs-grunt-saucelabs
Version:            8.1.1
Release:            1%{?dist}
Summary:            Grunt task running tests using Sauce Labs

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-saucelabs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(saucelabs)
BuildRequires:      npm(q)
BuildRequires:      npm(colors)
BuildRequires:      npm(lodash)
BuildRequires:      npm(sauce-tunnel)
BuildRequires:      npm(grunt)
BuildRequires:      npm(request)

Requires:           npm(saucelabs)
Requires:           npm(q)
Requires:           npm(colors)
Requires:           npm(lodash)
Requires:           npm(sauce-tunnel)
Requires:           npm(grunt)
Requires:           npm(request)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-sauce-tunnel)
BuildRequires:      npm(grunt-contrib-watch)
BuildRequires:      npm(grunt-contrib-connect)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt-jscs-checker)
BuildRequires:      npm(publish)
BuildRequires:      npm(merge)
BuildRequires:      npm(load-grunt-config)
BuildRequires:      npm(grunt)
%endif


%description
A Grunt task for running QUnit, Jasmine, Mocha, YUI tests, or any framework
using Sauce Labs' Cloudified Browsers.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep request ~2.x
%nodejs_fixdep q

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 8.1.1-1
- Initial packaging for Fedora.
