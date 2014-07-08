# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename grunt-html-validation

Name:               nodejs-grunt-html-validation
Version:            0.1.6
Release:            1%{?dist}
Summary:            W3C html validation grunt plugin

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-html-validation
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(colors)
BuildRequires:      npm(grunt)
BuildRequires:      npm(request)
BuildRequires:      npm(w3cjs)

Requires:           npm(colors)
Requires:           npm(grunt)
Requires:           npm(request)
Requires:           npm(w3cjs)

%if 0%{?enable_tests}
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-clean)
%endif


%description
W3C html validation grunt plugin. Validate all files in a directory
automatically.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep request ~2.x
%nodejs_fixdep w3cjs ~0.1.x

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
%endif

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-html-validation
cp -pr package.json tasks Gruntfile.js lib \
    %{buildroot}%{nodejs_sitelib}/grunt-html-validation

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/grunt-html-validation/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.1.6-1
- Initial packaging for Fedora.
