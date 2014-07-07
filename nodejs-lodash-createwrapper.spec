

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

BuildRequires:      nodejs-lodash-slice
BuildRequires:      nodejs-lodash-isfunction
BuildRequires:      nodejs-lodash-basebind
BuildRequires:      nodejs-lodash-basecreatewrapper

Requires:           nodejs-lodash-slice
Requires:           nodejs-lodash-isfunction
Requires:           nodejs-lodash-basebind
Requires:           nodejs-lodash-basecreatewrapper


%description
The internal [Lo-Dash](http://lodash.com/) function `createWrapper` as a
[Node.js](http://nodejs.org/) module generated by [lodash-
cli](https://npmjs.org/package/lodash-cli).

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash._slice
%nodejs_fixdep lodash.isfunction
%nodejs_fixdep lodash._basebind
%nodejs_fixdep lodash._basecreatewrapper




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
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.