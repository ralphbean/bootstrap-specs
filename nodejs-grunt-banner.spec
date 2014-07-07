%global enable_tests 0

%global barename grunt-banner

Name:               nodejs-grunt-banner
Version:            0.2.3
Release:            1%{?dist}
Summary:            Adds a simple banner to files

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-banner
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-grunt

Requires:           nodejs-grunt

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-clean
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-copy
BuildRequires:      nodejs-grunt-contrib-jshint
%endif

%description
Adds a simple banner to files

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep grunt

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-contrib-clean
%nodejs_fixdep --dev grunt
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-copy
%nodejs_fixdep --dev grunt-contrib-jshint
%else
%nodejs_fixdep --dev -r grunt-contrib-clean
%nodejs_fixdep --dev -r grunt
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-copy
%nodejs_fixdep --dev -r grunt-contrib-jshint
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-banner
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-banner

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-banner/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.2.3-1
- Initial packaging for Fedora.
