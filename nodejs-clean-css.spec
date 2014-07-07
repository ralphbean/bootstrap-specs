%global enable_tests 0

%global barename clean-css

Name:               nodejs-clean-css
Version:            2.2.5
Release:            1%{?dist}
Summary:            A well-tested CSS minifier

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/clean-css
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-commander

Requires:           nodejs-commander

%if 0%{?enable_tests}
BuildRequires:      nodejs-browserify
BuildRequires:      nodejs-nock
BuildRequires:      nodejs-jshint
BuildRequires:      nodejs-uglify-js
BuildRequires:      nodejs-vows
%endif


%description
Clean-css is a fast and efficient [Node.js](http://nodejs.org/) library for
minifying CSS files.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep commander

%if 0%{?enable_tests}
%nodejs_fixdep --dev browserify
%nodejs_fixdep --dev nock
%nodejs_fixdep --dev jshint
%nodejs_fixdep --dev uglify-js
%nodejs_fixdep --dev vows
%else
%nodejs_fixdep --dev -r browserify
%nodejs_fixdep --dev -r nock
%nodejs_fixdep --dev -r jshint
%nodejs_fixdep --dev -r uglify-js
%nodejs_fixdep --dev -r vows
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/clean-css
cp -pr package.json lib index.js \
    %{buildroot}%{nodejs_sitelib}/clean-css

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
vows
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/clean-css/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.2.5-1
- Initial packaging for Fedora.