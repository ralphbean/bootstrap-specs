%global enable_tests 0

%global barename grunt-contrib-cssmin

Name:               nodejs-grunt-contrib-cssmin
Version:            0.9.0
Release:            1%{?dist}
Summary:            Compress CSS files

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-cssmin
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-chalk
BuildRequires:      nodejs-clean-css
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-maxmin

Requires:           nodejs-chalk
Requires:           nodejs-clean-css
Requires:           nodejs-grunt
Requires:           nodejs-maxmin

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-internal
BuildRequires:      nodejs-grunt-contrib-clean
%endif


%description
Compress CSS files.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep chalk
%nodejs_fixdep clean-css
%nodejs_fixdep grunt
%nodejs_fixdep maxmin

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
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-cssmin
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-cssmin

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-contrib-cssmin/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Initial packaging for Fedora.
