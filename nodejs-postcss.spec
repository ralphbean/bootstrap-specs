# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename postcss

Name:               nodejs-postcss
Version:            1.0.0
Release:            1%{?dist}
Summary:            Framework for CSS postprocessors with full source map support

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/postcss
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(source-map)
BuildRequires:      npm(base64-js)

Requires:           npm(source-map)
Requires:           npm(base64-js)

%if 0%{?enable_tests}
BuildRequires:      npm(cssom)
BuildRequires:      npm(fs-extra)
BuildRequires:      npm(gonzales)
BuildRequires:      npm(rework)
BuildRequires:      npm(should)
BuildRequires:      npm(mocha)
%endif


%description
PostCSS is a framework for CSS postprocessors, to modify CSS with JavaScript
with full source map support.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep source-map ~0.1.x

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/postcss
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/postcss

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
mocha
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/postcss/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
