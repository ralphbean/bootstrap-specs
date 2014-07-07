

%global barename lodash._basecreatecallback

Name:               nodejs-lodash-basecreatecallback
Version:            2.4.1
Release:            1%{?dist}
Summary:            The internal Lo-Dash function `baseCreateCallback` as a Node.js module

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/lodash._basecreatecallback
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-lodash-bind
BuildRequires:      nodejs-lodash-setbinddata
BuildRequires:      nodejs-lodash-identity
BuildRequires:      nodejs-lodash-support

Requires:           nodejs-lodash-bind
Requires:           nodejs-lodash-setbinddata
Requires:           nodejs-lodash-identity
Requires:           nodejs-lodash-support


%description
The internal Lo-Dash function `baseCreateCallback` as a Node.js module
generated by lodash-cli.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash.bind
%nodejs_fixdep lodash._setbinddata
%nodejs_fixdep lodash.identity
%nodejs_fixdep lodash.support




%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/lodash._basecreatecallback
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/lodash._basecreatecallback

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/lodash._basecreatecallback/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.
