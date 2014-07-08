# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename clean-css

Name:               nodejs-clean-css
Version:            2.2.6
Release:            1%{?dist}
Summary:            A well-tested CSS minifier

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/clean-css
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(commander)

Requires:           npm(commander)

%if 0%{?enable_tests}
BuildRequires:      npm(browserify)
BuildRequires:      npm(nock)
BuildRequires:      npm(jshint)
BuildRequires:      npm(uglify-js)
BuildRequires:      npm(vows)
%endif


%description
Clean-css is a fast and efficient [Node.js](http://nodejs.org/) library for
minifying CSS files.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep commander ~2.2.x


%if 0%{?enable_tests}
%nodejs_fixdep --dev browserify ~4.x
%nodejs_fixdep --dev nock ~0.28.x
%nodejs_fixdep --dev jshint ~2.5.x
%nodejs_fixdep --dev uglify-js ~2.4.x
%nodejs_fixdep --dev vows ~0.7.x
%else
%nodejs_fixdep --dev -r browserify ~4.x
%nodejs_fixdep --dev -r nock ~0.28.x
%nodejs_fixdep --dev -r jshint ~2.5.x
%nodejs_fixdep --dev -r uglify-js ~2.4.x
%nodejs_fixdep --dev -r vows ~0.7.x
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/clean-css
cp -pr package.json lib index.js \
    %{buildroot}%{nodejs_sitelib}/clean-css

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
vows
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/clean-css/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.2.6-1
- Initial packaging for Fedora.