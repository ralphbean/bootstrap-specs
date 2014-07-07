%global enable_tests 0
%global prerelease 1
%global barename grunt-csscomb

Name:               nodejs-grunt-csscomb
Version:            3.0.0
Release:            0.1.%{prerelease}%{?dist}
Summary:            The grunt plugin for sorting CSS properties in specific order

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-csscomb
Source0:            http://registry.npmjs.org/grunt-csscomb/-/grunt-csscomb-3.0.0-%{prerelease}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-csscomb
BuildRequires:      nodejs-grunt

Requires:           nodejs-csscomb
Requires:           nodejs-grunt

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-clean
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
%endif


%description
The grunt plugin for sorting CSS properties in specific order.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep csscomb
%nodejs_fixdep grunt

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-contrib-clean
%nodejs_fixdep --dev grunt
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-jshint
%else
%nodejs_fixdep --dev -r grunt-contrib-clean
%nodejs_fixdep --dev -r grunt
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-jshint
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-csscomb
cp -pr package.json tasks Gruntfile.js \
    %{buildroot}%{nodejs_sitelib}/grunt-csscomb

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-csscomb/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.1
- Initial packaging for Fedora.
