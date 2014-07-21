# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename w3cjs

Name:               nodejs-w3cjs
Version:            0.1.25
Release:            1%{?dist}
Summary:            A node.js module for using the w3c validator

Group:              Development/Libraries
License:            Public Domain
URL:                https://www.npmjs.org/package/w3cjs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(argparse)
BuildRequires:      npm(superagent)

Requires:           npm(argparse)
Requires:           npm(superagent)


%description
A node.js library for testing files or url's against the w3c html
validator.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep argparse ~0.x
%nodejs_fixdep superagent ~0.x


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/w3cjs
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/w3cjs

%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/w3cjs/

%changelog
* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.1.25-1
- Latest upstream.
- Specified noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.1.9-1
- Initial packaging for Fedora.
