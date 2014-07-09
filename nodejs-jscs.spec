# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename jscs

Name:               nodejs-jscs
Version:            1.5.8
Release:            1%{?dist}
Summary:            JavaScript Code Style

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/jscs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(minimatch)
BuildRequires:      npm(vow-fs)
BuildRequires:      npm(glob)
BuildRequires:      npm(strip-json-comments)
BuildRequires:      npm(xmlbuilder)
BuildRequires:      npm(commander)
BuildRequires:      npm(colors)
BuildRequires:      npm(vow)
BuildRequires:      npm(esprima)

Requires:           npm(minimatch)
Requires:           npm(vow-fs)
Requires:           npm(glob)
Requires:           npm(strip-json-comments)
Requires:           npm(xmlbuilder)
Requires:           npm(commander)
Requires:           npm(colors)
Requires:           npm(vow)
Requires:           npm(esprima)

%if 0%{?enable_tests}
BuildRequires:      npm(xml2js)
BuildRequires:      npm(browserify)
BuildRequires:      npm(jshint)
BuildRequires:      npm(hooker)
BuildRequires:      npm(sinon)
BuildRequires:      npm(mocha)
%endif


%description
JSCS — JavaScript Code Style.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep glob
%nodejs_fixdep minimatch ^0.2
%nodejs_fixdep esprima ^1.1

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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 1.5.8-1
- Initial packaging for Fedora.
