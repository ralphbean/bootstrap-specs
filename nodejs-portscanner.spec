# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



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

BuildRequires:      npm(async)

Requires:           npm(async)


%description
The portscanner module is an asynchronous JavaScript port scanner for Node.js.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep async ~0.x

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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
