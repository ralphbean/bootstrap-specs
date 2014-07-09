# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(chalk)
BuildRequires:      npm(clean-css)
BuildRequires:      npm(grunt)
BuildRequires:      npm(maxmin)

Requires:           npm(chalk)
Requires:           npm(clean-css)
Requires:           npm(grunt)
Requires:           npm(maxmin)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-internal)
BuildRequires:      npm(grunt-contrib-clean)
%endif


%description
Compress CSS files.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep maxmin ~0.x

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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Initial packaging for Fedora.
