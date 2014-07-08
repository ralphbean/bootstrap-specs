# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(portscanner)
BuildRequires:      npm(connect)
BuildRequires:      npm(async)
BuildRequires:      npm(open)
BuildRequires:      npm(grunt)
BuildRequires:      npm(connect-livereload)

Requires:           npm(portscanner)
Requires:           npm(connect)
Requires:           npm(async)
Requires:           npm(open)
Requires:           npm(grunt)
Requires:           npm(connect-livereload)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt-cli)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-internal)
%endif


%description
Start a connect web server.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep portscanner
%nodejs_fixdep connect ~2.x
%nodejs_fixdep async ~0.x
%nodejs_fixdep open ~0.0.x
%nodejs_fixdep grunt ~0.4.x
%nodejs_fixdep connect-livereload ~0.4.x




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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- Initial packaging for Fedora.
