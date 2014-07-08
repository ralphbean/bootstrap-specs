# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename grunt-contrib-copy

Name:               nodejs-grunt-contrib-copy
Version:            0.5.0
Release:            1%{?dist}
Summary:            Copy files and folders

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-copy
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(grunt)

Requires:           npm(grunt)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-internal)
BuildRequires:      npm(grunt-contrib-clean)
%endif


%description
Copy files and folders.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep grunt ~0.4.x




%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-copy
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-copy

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-contrib-copy/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Initial packaging for Fedora.