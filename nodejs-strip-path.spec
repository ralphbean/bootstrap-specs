# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename strip-path

Name:               nodejs-strip-path
Version:            0.1.1
Release:            1%{?dist}
Summary:            Strip a path from a path

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/strip-path
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:      npm(mocha)
%endif


%description
Strip a path from a path

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/



%if 0%{?enable_tests}
%nodejs_fixdep --dev mocha ~*
%else
%nodejs_fixdep --dev -r mocha ~*
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/strip-path
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/strip-path

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
mocha
%endif


%files
%doc
%{nodejs_sitelib}/strip-path/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- Initial packaging for Fedora.