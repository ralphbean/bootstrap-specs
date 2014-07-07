

%global barename lodash._objecttypes

Name:               nodejs-lodash-objecttypes
Version:            2.4.1
Release:            1%{?dist}
Summary:            The internal Lo-Dash variable `objectTypes` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash._objecttypes
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6




%description
The internal Lo-Dash variable `objectTypes` as a Node.js module generated
by lodash-cli.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/





%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash._objecttypes
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash._objecttypes

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash._objecttypes/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.
