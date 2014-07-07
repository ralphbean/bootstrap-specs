

%global barename portscanner

Name:               nodejs-portscanner
Version:            1.0.0
Release:            1%{?dist}
Summary:            Asynchronous port scanner for Node.js

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/portscanner
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-async

Requires:           nodejs-async


%description
The portscanner module is an asynchronous JavaScript port scanner for Node.js.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep async


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/portscanner
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/portscanner

%nodejs_symlink_deps

%files
%doc LICENSE README.md
%{nodejs_sitelib}/portscanner/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
