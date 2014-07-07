%global enable_tests 0

%global barename grunt-lib-contrib

Name:               nodejs-grunt-lib-contrib
Version:            0.7.1
Release:            1%{?dist}
Summary:            Common functionality shared across grunt-contrib tasks

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-lib-contrib
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-maxmin
BuildRequires:      nodejs-strip-path

Requires:           nodejs-maxmin
Requires:           nodejs-strip-path

%if 0%{?enable_tests}
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt
%endif


%description
Common functionality shared across grunt-contrib tasks.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep maxmin
%nodejs_fixdep strip-path

%if 0%{?enable_tests}
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt
%else
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-lib-contrib
cp -pr package.json Gruntfile.js lib \
    %{buildroot}%{nodejs_sitelib}/grunt-lib-contrib

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md CHANGELOG
%{nodejs_sitelib}/grunt-lib-contrib/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.7.1-1
- Initial packaging for Fedora.
