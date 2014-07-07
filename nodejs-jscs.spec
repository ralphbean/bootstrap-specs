%global enable_tests 0

%global barename jscs

Name:               nodejs-jscs
Version:            1.5.7
Release:            1%{?dist}
Summary:            JavaScript Code Style

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/jscs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-minimatch
BuildRequires:      nodejs-vow-fs
BuildRequires:      nodejs-glob
BuildRequires:      nodejs-strip-json-comments
BuildRequires:      nodejs-xmlbuilder
BuildRequires:      nodejs-commander
BuildRequires:      nodejs-colors
BuildRequires:      nodejs-vow
BuildRequires:      nodejs-esprima

Requires:           nodejs-minimatch
Requires:           nodejs-vow-fs
Requires:           nodejs-glob
Requires:           nodejs-strip-json-comments
Requires:           nodejs-xmlbuilder
Requires:           nodejs-commander
Requires:           nodejs-colors
Requires:           nodejs-vow
Requires:           nodejs-esprima

%if 0%{?enable_tests}
BuildRequires:      nodejs-xml2js
BuildRequires:      nodejs-browserify
BuildRequires:      nodejs-jshint
BuildRequires:      nodejs-hooker
BuildRequires:      nodejs-sinon
BuildRequires:      nodejs-mocha
%endif


%description
JSCS — JavaScript Code Style.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep minimatch
%nodejs_fixdep vow-fs
%nodejs_fixdep glob
%nodejs_fixdep strip-json-comments
%nodejs_fixdep xmlbuilder
%nodejs_fixdep commander
%nodejs_fixdep colors
%nodejs_fixdep vow
%nodejs_fixdep esprima

%if 0%{?enable_tests}
%nodejs_fixdep --dev xml2js
%nodejs_fixdep --dev browserify
%nodejs_fixdep --dev jshint
%nodejs_fixdep --dev hooker
%nodejs_fixdep --dev sinon
%nodejs_fixdep --dev mocha
%else
%nodejs_fixdep --dev -r xml2js
%nodejs_fixdep --dev -r browserify
%nodejs_fixdep --dev -r jshint
%nodejs_fixdep --dev -r hooker
%nodejs_fixdep --dev -r sinon
%nodejs_fixdep --dev -r mocha
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jscs
cp -pr package.json jscs-browser.js lib \
    %{buildroot}%{nodejs_sitelib}/jscs

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm run lint && mocha
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/jscs/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 1.5.7-1
- Initial packaging for Fedora.