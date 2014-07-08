# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename lodash._basebind

Name:               nodejs-lodash-basebind
Version:            2.4.1
Release:            1%{?dist}
Summary:            The internal Lo-Dash function `baseBind` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash._basebind
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(lodash.isobject)
BuildRequires:      npm(lodash._basecreate)
BuildRequires:      npm(lodash._setbinddata)
BuildRequires:      npm(lodash._slice)

Requires:           npm(lodash.isobject)
Requires:           npm(lodash._basecreate)
Requires:           npm(lodash._setbinddata)
Requires:           npm(lodash._slice)


%description
The internal [Lo-Dash](http://lodash.com/) function `baseBind` as a
[Node.js](http://nodejs.org/) module generated by [lodash-
cli](https://npmjs.org/package/lodash-cli).

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret



%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash._basebind
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash._basebind

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash._basebind/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.