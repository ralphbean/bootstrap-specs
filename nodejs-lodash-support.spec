# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename lodash.support

Name:               nodejs-lodash-support
Version:            2.4.1
Release:            1%{?dist}
Summary:            The Lo-Dash object `_.support` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash.support
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(lodash._isnative)

Requires:           npm(lodash._isnative)


%description
The Lo-Dash object `_.support` as a Node.js module

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash._isnative ~2.4.x





%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash.support
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash.support

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash.support/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.