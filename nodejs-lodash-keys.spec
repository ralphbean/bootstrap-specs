

%global barename lodash.keys

Name:               nodejs-lodash-keys
Version:            2.4.1
Release:            1%{?dist}
Summary:            The Lo-Dash function `_.keys` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash.keys
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-lodash-isobject
BuildRequires:      nodejs-lodash-isnative
BuildRequires:      nodejs-lodash-shimkeys

Requires:           nodejs-lodash-isobject
Requires:           nodejs-lodash-isnative
Requires:           nodejs-lodash-shimkeys


%description
The Lo-Dash function `_.keys` as a Node.js module

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash.isobject
%nodejs_fixdep lodash._isnative
%nodejs_fixdep lodash._shimkeys




%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash.keys
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash.keys

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash.keys/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.
