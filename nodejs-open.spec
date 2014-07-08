# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename open

Name:               nodejs-open
Version:            0.0.5
Release:            1%{?dist}
Summary:            Open a file or url in the user's preferred application

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/open
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:      npm(mocha)
%endif


%description
Open a file or url in the user's preferred application.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
%endif

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/open
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/open

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
node_modules/mocha/bin/mocha
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/open/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.0.5-1
- Initial packaging for Fedora.