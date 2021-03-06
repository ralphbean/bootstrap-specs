# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global barename csslint

Name:               nodejs-csslint
Version:            0.10.0
Release:            1%{?dist}
Summary:            CSSLint

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/csslint
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(parserlib)

Requires:           npm(parserlib)

%description
CSSLint is a tool to help point out problems with your CSS code. It does
basic syntax checking as well as applying a set of rules to the code that
look for problematic patterns or signs of inefficiency. The rules are all
pluggable, so you can easily write your own or omit ones you don't want.

You can find information about both using CSS Lint and contributing to the
project in the wiki: https://github.com/stubbornella/csslint/wiki

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/csslint
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/csslint

%nodejs_symlink_deps

%files
%doc README.md
%{nodejs_sitelib}/csslint/

%changelog
* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.10.0-1
- Latest upstream.
- Specify arch.
- Include readme.
- Ditch cli.js for now.
- Added new dep on npm(parserlib)

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.9.9-1
- Initial packaging for Fedora.
