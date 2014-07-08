# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(grunt)

Requires:           npm(grunt)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-clean)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-copy)
BuildRequires:      npm(grunt-contrib-jshint)
%endif

%description
Adds a simple banner to files

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.2.3-1
- Initial packaging for Fedora.