# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename sauce-tunnel

Name:               nodejs-sauce-tunnel
Version:            2.0.6
Release:            1%{?dist}
Summary:            A wrapper around the Sauce Labs tunnel jar

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/sauce-tunnel
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(chalk)
BuildRequires:      npm(request)

Requires:           npm(chalk)
Requires:           npm(request)

%if 0%{?enable_tests}
%endif


%description
A Node.js wrapper around the Saucelabs tunnel jar.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep chalk ~0.4.x
%nodejs_fixdep request ~2.x


%if 0%{?enable_tests}
%else
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/sauce-tunnel
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/sauce-tunnel

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
node ./test/sanity
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/sauce-tunnel/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.0.6-1
- Initial packaging for Fedora.
