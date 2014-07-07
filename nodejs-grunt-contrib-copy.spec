%global enable_tests 0

%global barename grunt-contrib-copy

Name:               nodejs-grunt-contrib-copy
Version:            0.5.0
Release:            1%{?dist}
Summary:            Copy files and folders

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-copy
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-grunt

Requires:           nodejs-grunt

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-internal
BuildRequires:      nodejs-grunt-contrib-clean
%endif


%description
Copy files and folders.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep grunt

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt
%nodejs_fixdep --dev grunt-contrib-internal
%nodejs_fixdep --dev grunt-contrib-clean
%else
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt
%nodejs_fixdep --dev -r grunt-contrib-internal
%nodejs_fixdep --dev -r grunt-contrib-clean
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-copy
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-copy

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-contrib-copy/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Initial packaging for Fedora.
