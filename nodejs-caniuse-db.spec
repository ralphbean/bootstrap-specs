# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename caniuse-db

Name:               nodejs-caniuse-db
Version:            1.0.20140702
Release:            1%{?dist}
Summary:            Raw browser/feature support data from caniuse.com

Group:              Development/Libraries
License:            CC-BY
URL:                https://www.npmjs.org/package/caniuse-db
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6




%description
This repo contains raw data from the caniuse.com support tables. It servers
two purposes:

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret



%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/caniuse-db
cp -pr package.json \
    %{buildroot}%{nodejs_sitelib}/caniuse-db

%nodejs_symlink_deps



%files
%doc README.md
%{nodejs_sitelib}/caniuse-db/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 1.0.20140702-1
- Initial packaging for Fedora.