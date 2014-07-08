# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global prerelease 5
%global barename csscomb

Name:               nodejs-csscomb
Version:            3.0.0
Release:            0.1.%{prerelease}%{?dist}
Summary:            CSS coding style formatter

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/csscomb
Source0:            http://registry.npmjs.org/csscomb/-/csscomb-3.0.0-%{prerelease}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(gonzales-pe)
BuildRequires:      npm(minimatch)
BuildRequires:      npm(vow)
BuildRequires:      npm(vow-fs)
BuildRequires:      npm(commander)

Requires:           npm(gonzales-pe)
Requires:           npm(minimatch)
Requires:           npm(vow)
Requires:           npm(vow-fs)
Requires:           npm(commander)

%if 0%{?enable_tests}
BuildRequires:      npm(jscs)
BuildRequires:      npm(jshint)
BuildRequires:      npm(jshint-groups)
BuildRequires:      npm(mocha)
%endif


%description
CSScomb is a coding style formatter for CSS.  You can easily write your own
configuration to make your style sheets beautiful and consistent.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep gonzales-pe ~3.0.x
%nodejs_fixdep minimatch ~0.2.x
%nodejs_fixdep vow ~0.4.x
%nodejs_fixdep vow-fs ~0.3.x
%nodejs_fixdep commander ~2.x


%if 0%{?enable_tests}
%nodejs_fixdep --dev jscs ~1.4.x
%nodejs_fixdep --dev jshint ~2.3.x
%nodejs_fixdep --dev jshint-groups ~0.5.x
%nodejs_fixdep --dev mocha ~1.14.x
%else
%nodejs_fixdep --dev -r jscs ~1.4.x
%nodejs_fixdep --dev -r jshint ~2.3.x
%nodejs_fixdep --dev -r jshint-groups ~0.5.x
%nodejs_fixdep --dev -r mocha ~1.14.x
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/csscomb
cp -pr package.json .jshint-groups.js lib \
    %{buildroot}%{nodejs_sitelib}/csscomb

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
jshint-groups && ./node_modules/.bin/jscs . && node test/mocha
%endif


%files
%doc CHANGELOG.md README.md LICENSE
%{nodejs_sitelib}/csscomb/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.5
- Initial packaging for Fedora.
