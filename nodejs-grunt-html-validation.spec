%global enable_tests 0

%global barename grunt-html-validation

Name:               nodejs-grunt-html-validation
Version:            0.1.6
Release:            1%{?dist}
Summary:            W3C html validation grunt plugin

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-html-validation
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-colors
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-request
BuildRequires:      nodejs-w3cjs

Requires:           nodejs-colors
Requires:           nodejs-grunt
Requires:           nodejs-request
Requires:           nodejs-w3cjs

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-clean
%endif


%description
W3C html validation grunt plugin. Validate all files in a directory
automatically.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep colors
%nodejs_fixdep grunt
%nodejs_fixdep request
%nodejs_fixdep w3cjs

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt
%nodejs_fixdep --dev grunt-contrib-clean
%else
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt
%nodejs_fixdep --dev -r grunt-contrib-clean
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-html-validation
cp -pr package.json tasks Gruntfile.js lib \
    %{buildroot}%{nodejs_sitelib}/grunt-html-validation

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-html-validation/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.1.6-1
- Initial packaging for Fedora.
