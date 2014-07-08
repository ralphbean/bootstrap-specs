# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename lodash.noop

Name:               nodejs-lodash-noop
Version:            2.4.1
Release:            1%{?dist}
Summary:            The Lo-Dash function `_.noop` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash.noop
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6




%description
The [Lo-Dash](http://lodash.com/) function
[`_.noop`](http://lodash.com/docs#noop) as a [Node.js](http://nodejs.org/)
module generated by [lodash-cli](https://npmjs.org/package/lodash-cli).

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/






%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash.noop
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash.noop

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash.noop/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.