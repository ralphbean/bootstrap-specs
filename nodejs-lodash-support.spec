

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

BuildRequires:      nodejs-lodash-isnative

Requires:           nodejs-lodash-isnative


%description
The Lo-Dash object `_.support` as a Node.js module

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep lodash._isnative




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
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.4.1-1
- Initial packaging for Fedora.
