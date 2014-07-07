%global enable_tests 0

%global barename grunt-jscs-checker

Name:               nodejs-grunt-jscs-checker
Version:            0.6.1
Release:            1%{?dist}
Summary:            Grunt task for checking JavaScript Code Style with jscs

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-jscs-checker
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-lodash-assign
BuildRequires:      nodejs-hooker
BuildRequires:      nodejs-jscs
BuildRequires:      nodejs-vow
BuildRequires:      nodejs-grunt

Requires:           nodejs-lodash-assign
Requires:           nodejs-hooker
Requires:           nodejs-jscs
Requires:           nodejs-vow
Requires:           nodejs-grunt

%if 0%{?enable_tests}
BuildRequires:      nodejs-time-grunt
BuildRequires:      nodejs-load-grunt-tasks
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt-cli
BuildRequires:      nodejs-grunt-bump
%endif


%description
Task for checking JavaScript Code Style with jscs.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash.assign
%nodejs_fixdep hooker
%nodejs_fixdep jscs
%nodejs_fixdep vow
%nodejs_fixdep grunt

%if 0%{?enable_tests}
%nodejs_fixdep --dev time-grunt
%nodejs_fixdep --dev load-grunt-tasks
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt-cli
%nodejs_fixdep --dev grunt-bump
%else
%nodejs_fixdep --dev -r time-grunt
%nodejs_fixdep --dev -r load-grunt-tasks
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt-cli
%nodejs_fixdep --dev -r grunt-bump
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-jscs-checker
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-jscs-checker

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-jscs-checker/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Initial packaging for Fedora.
