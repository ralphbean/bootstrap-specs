# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(lodash.assign)
BuildRequires:      npm(hooker)
BuildRequires:      npm(jscs)
BuildRequires:      npm(vow)
BuildRequires:      npm(grunt)

Requires:           npm(lodash.assign)
Requires:           npm(hooker)
Requires:           npm(jscs)
Requires:           npm(vow)
Requires:           npm(grunt)

%if 0%{?enable_tests}
BuildRequires:      npm(time-grunt)
BuildRequires:      npm(load-grunt-tasks)
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt-cli)
BuildRequires:      npm(grunt-bump)
%endif


%description
Task for checking JavaScript Code Style with jscs.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash.assign ~2.4.x
%nodejs_fixdep hooker ~0.2.x
%nodejs_fixdep jscs ~1.5.x
%nodejs_fixdep vow ~0.4.x
%nodejs_fixdep grunt ~0.4.x




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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Initial packaging for Fedora.