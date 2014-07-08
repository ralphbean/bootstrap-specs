# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename lodash.identity

Name:               nodejs-lodash-identity
Version:            2.4.1
Release:            1%{?dist}
Summary:            The Lo-Dash function `_.identity` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash.identity
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6




%description
The Lo-Dash function `_.identity` as a Node.js module generated by lodash-
cli.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/






%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash.identity
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash.identity

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash.identity/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.