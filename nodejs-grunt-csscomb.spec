# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(csscomb)
BuildRequires:      npm(grunt)

Requires:           npm(csscomb)
Requires:           npm(grunt)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-clean)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
%endif


%description
The grunt plugin for sorting CSS properties in specific order.

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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.1
- Initial packaging for Fedora.