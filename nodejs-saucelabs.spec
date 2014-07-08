# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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
BuildRequires:      npm(mocha)
BuildRequires:      npm(chai)
BuildRequires:      npm(jshint)
BuildRequires:      npm(nock)
%endif


%description
node-saucelabs
========

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/



%if 0%{?enable_tests}
%nodejs_fixdep --dev mocha ~1.9.x
%nodejs_fixdep --dev chai ~1.5.x
%nodejs_fixdep --dev jshint ~*
%nodejs_fixdep --dev nock ~0.17.x
%else
%nodejs_fixdep --dev -r mocha ~1.9.x
%nodejs_fixdep --dev -r chai ~1.5.x
%nodejs_fixdep --dev -r jshint ~*
%nodejs_fixdep --dev -r nock ~0.17.x
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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- Initial packaging for Fedora.