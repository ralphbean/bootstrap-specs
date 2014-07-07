%global enable_tests 0
%global prerelease 5
%global barename csscomb

Name:               nodejs-csscomb
Version:            3.0.0
Release:            0.1.%{prerelease}%{?dist}
Summary:            CSS coding style formatter

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/csscomb
Source0:            http://registry.npmjs.org/csscomb/-/csscomb-3.0.0-%{prerelease}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-gonzales-pe
BuildRequires:      nodejs-minimatch
BuildRequires:      nodejs-vow
BuildRequires:      nodejs-vow-fs
BuildRequires:      nodejs-commander

Requires:           nodejs-gonzales-pe
Requires:           nodejs-minimatch
Requires:           nodejs-vow
Requires:           nodejs-vow-fs
Requires:           nodejs-commander

%if 0%{?enable_tests}
BuildRequires:      nodejs-jscs
BuildRequires:      nodejs-jshint
BuildRequires:      nodejs-jshint-groups
BuildRequires:      nodejs-mocha
%endif


%description
CSScomb is a coding style formatter for CSS.  You can easily write your own
configuration to make your style sheets beautiful and consistent.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep gonzales-pe
%nodejs_fixdep minimatch
%nodejs_fixdep vow
%nodejs_fixdep vow-fs
%nodejs_fixdep commander

%if 0%{?enable_tests}
%nodejs_fixdep --dev jscs
%nodejs_fixdep --dev jshint
%nodejs_fixdep --dev jshint-groups
%nodejs_fixdep --dev mocha
%else
%nodejs_fixdep --dev -r jscs
%nodejs_fixdep --dev -r jshint
%nodejs_fixdep --dev -r jshint-groups
%nodejs_fixdep --dev -r mocha
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/csscomb
cp -pr package.json .jshint-groups.js lib \
    %{buildroot}%{nodejs_sitelib}/csscomb

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
jshint-groups && ./node_modules/.bin/jscs . && node test/mocha
%endif


%files
%doc CHANGELOG.md README.md LICENSE
%{nodejs_sitelib}/csscomb/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.5
- Initial packaging for Fedora.
