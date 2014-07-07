

%global barename lodash.isobject

Name:               nodejs-lodash-isobject
Version:            2.4.1
Release:            1%{?dist}
Summary:            The Lo-Dash function `_.isObject` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash.isobject
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-lodash-objecttypes

Requires:           nodejs-lodash-objecttypes


%description
The Lo-Dash function `_.isObject` as a Node.js module generated by lodash-
cli.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash._objecttypes




%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash.isobject
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash.isobject

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash.isobject/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.
