# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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
%nodejs_fixdep --dev uglify-js ~1.3.x
%nodejs_fixdep --dev jspath ~0.2.x
%nodejs_fixdep --dev istanbul ~
%nodejs_fixdep --dev promises-aplus-tests ~2.0.x
%nodejs_fixdep --dev marked ~0.2.x
%nodejs_fixdep --dev highlight.js ~7.5.x
%nodejs_fixdep --dev nodeunit ~
%nodejs_fixdep --dev bem-jsd ~1.3.x
%nodejs_fixdep --dev yate ~0.0.x
%else
%nodejs_fixdep --dev -r uglify-js ~1.3.x
%nodejs_fixdep --dev -r jspath ~0.2.x
%nodejs_fixdep --dev -r istanbul ~
%nodejs_fixdep --dev -r promises-aplus-tests ~2.0.x
%nodejs_fixdep --dev -r marked ~0.2.x
%nodejs_fixdep --dev -r highlight.js ~7.5.x
%nodejs_fixdep --dev -r nodeunit ~
%nodejs_fixdep --dev -r bem-jsd ~1.3.x
%nodejs_fixdep --dev -r yate ~0.0.x
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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Initial packaging for Fedora.