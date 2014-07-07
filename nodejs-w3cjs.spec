

%global barename w3cjs

Name:               nodejs-w3cjs
Version:            0.1.9
Release:            1%{?dist}
Summary:            A node.js module for using the w3c validator

Group:              Development/Libraries
License:            Public Domain
URL:                https://www.npmjs.org/package/w3cjs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-argparse
BuildRequires:      nodejs-superagent

Requires:           nodejs-argparse
Requires:           nodejs-superagent


%description
A node.js library for testing files or url's against the w3c html
validator.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep argparse
%nodejs_fixdep superagent




%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/w3cjs
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/w3cjs

%nodejs_symlink_deps



%files
%doc README.md LICENSE
%{nodejs_sitelib}/w3cjs/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.1.9-1
- Initial packaging for Fedora.
