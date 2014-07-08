# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename grunt-contrib-csslint

Name:               nodejs-grunt-contrib-csslint
Version:            0.2.0
Release:            1%{?dist}
Summary:            Lint CSS files

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-contrib-csslint
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(csslint)
BuildRequires:      npm(grunt)

Requires:           npm(csslint)
Requires:           npm(grunt)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-internal)
BuildRequires:      npm(grunt-contrib-clean)
%endif


%description
Lint CSS files.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep csslint ~0.x

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
%endif

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-csslint
cp -pr package.json tasks Gruntfile.js \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-csslint

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test --force
%endif


%files
%doc LICENSE-MIT README.md CHANGELOG
%{nodejs_sitelib}/grunt-contrib-csslint/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Initial packaging for Fedora.
