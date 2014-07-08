# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename lodash.bind

Name:               nodejs-lodash-bind
Version:            2.4.1
Release:            1%{?dist}
Summary:            The Lo-Dash function `_.bind` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash.bind
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(lodash._slice)
BuildRequires:      npm(lodash._createwrapper)

Requires:           npm(lodash._slice)
Requires:           npm(lodash._createwrapper)


%description
The Lo-Dash function `_.bind` as a Node.js module generated by lodash-cli.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret



%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash.bind
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash.bind

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash.bind/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.