%global enable_tests 0

%global barename grunt-contrib-connect

Name:               nodejs-grunt-contrib-connect
Version:            0.8.0
Release:            1%{?dist}
Summary:            Start a connect web server

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-connect
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-portscanner
BuildRequires:      nodejs-connect
BuildRequires:      nodejs-async
BuildRequires:      nodejs-open
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-connect-livereload

Requires:           nodejs-portscanner
Requires:           nodejs-connect
Requires:           nodejs-async
Requires:           nodejs-open
Requires:           nodejs-grunt
Requires:           nodejs-connect-livereload

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt-cli
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-internal
%endif


%description
Start a connect web server.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep portscanner
%nodejs_fixdep connect
%nodejs_fixdep async
%nodejs_fixdep open
%nodejs_fixdep grunt
%nodejs_fixdep connect-livereload

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt-cli
%nodejs_fixdep --dev grunt
%nodejs_fixdep --dev grunt-contrib-internal
%else
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt-cli
%nodejs_fixdep --dev -r grunt
%nodejs_fixdep --dev -r grunt-contrib-internal
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-connect
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-connect

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt jshint test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-contrib-connect/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- Initial packaging for Fedora.
