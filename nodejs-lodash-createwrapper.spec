# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename lodash._createwrapper

Name:               nodejs-lodash-createwrapper
Version:            2.4.1
Release:            1%{?dist}
Summary:            The internal Lo-Dash function `createWrapper` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash._createwrapper
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(lodash._slice)
BuildRequires:      npm(lodash.isfunction)
BuildRequires:      npm(lodash._basebind)
BuildRequires:      npm(lodash._basecreatewrapper)

Requires:           npm(lodash._slice)
Requires:           npm(lodash.isfunction)
Requires:           npm(lodash._basebind)
Requires:           npm(lodash._basecreatewrapper)


%description
The internal [Lo-Dash](http://lodash.com/) function `createWrapper` as a
[Node.js](http://nodejs.org/) module generated by [lodash-
cli](https://npmjs.org/package/lodash-cli).

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash._slice ~2.4.x
%nodejs_fixdep lodash.isfunction ~2.4.x
%nodejs_fixdep lodash._basebind ~2.4.x
%nodejs_fixdep lodash._basecreatewrapper ~2.4.x





%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash._createwrapper
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash._createwrapper

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash._createwrapper/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.