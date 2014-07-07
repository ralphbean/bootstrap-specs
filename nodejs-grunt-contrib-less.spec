%global enable_tests 0

%global barename grunt-contrib-less

Name:               nodejs-grunt-contrib-less
Version:            0.9.0
Release:            1%{?dist}
Summary:            Compile LESS files to CSS

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-less
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-chalk
BuildRequires:      nodejs-grunt-lib-contrib
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-less

Requires:           nodejs-chalk
Requires:           nodejs-grunt-lib-contrib
Requires:           nodejs-grunt
Requires:           nodejs-less

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-internal
BuildRequires:      nodejs-grunt-contrib-clean
%endif


%description
Compile LESS files to CSS.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep chalk
%nodejs_fixdep grunt-lib-contrib
%nodejs_fixdep grunt
%nodejs_fixdep less

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
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-less
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-less

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-contrib-less/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Initial packaging for Fedora.
