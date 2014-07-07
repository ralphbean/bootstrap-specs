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

BuildRequires:      nodejs-chalk
BuildRequires:      nodejs-request

Requires:           nodejs-chalk
Requires:           nodejs-request

%if 0%{?enable_tests}
%endif


%description
A Node.js wrapper around the Saucelabs tunnel jar.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep chalk
%nodejs_fixdep request

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
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.0.6-1
- Initial packaging for Fedora.