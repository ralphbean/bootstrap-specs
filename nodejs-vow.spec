%global enable_tests 0

%global barename vow

Name:               nodejs-vow
Version:            0.4.4
Release:            1%{?dist}
Summary:            Promises/A+ proposal compatible promises library

Group:              Development/Libraries
# https://github.com/dfilatov/vow/issues/67
License:            MIT and GPLv3
URL:                https://www.npmjs.org/package/vow
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:      nodejs-uglify-js
BuildRequires:      nodejs-jspath
BuildRequires:      nodejs-istanbul
BuildRequires:      nodejs-promises-aplus-tests
BuildRequires:      nodejs-marked
BuildRequires:      nodejs-highlight-js
BuildRequires:      nodejs-nodeunit
BuildRequires:      nodejs-bem-jsd
BuildRequires:      nodejs-yate
%endif


%description
A Promises/A+ implementation.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/


%if 0%{?enable_tests}
%nodejs_fixdep --dev uglify-js
%nodejs_fixdep --dev jspath
%nodejs_fixdep --dev istanbul
%nodejs_fixdep --dev promises-aplus-tests
%nodejs_fixdep --dev marked
%nodejs_fixdep --dev highlight.js
%nodejs_fixdep --dev nodeunit
%nodejs_fixdep --dev bem-jsd
%nodejs_fixdep --dev yate
%else
%nodejs_fixdep --dev -r uglify-js
%nodejs_fixdep --dev -r jspath
%nodejs_fixdep --dev -r istanbul
%nodejs_fixdep --dev -r promises-aplus-tests
%nodejs_fixdep --dev -r marked
%nodejs_fixdep --dev -r highlight.js
%nodejs_fixdep --dev -r nodeunit
%nodejs_fixdep --dev -r bem-jsd
%nodejs_fixdep --dev -r yate
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vow
cp -pr package.json lib vow.min.js \
    %{buildroot}%{nodejs_sitelib}/vow

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
./node_modules/istanbul/lib/cli.js test test/utils/runner.js
%endif


%files
%doc
%{nodejs_sitelib}/vow/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Initial packaging for Fedora.
