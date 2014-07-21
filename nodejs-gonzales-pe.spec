# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global prerelease 9
%global barename gonzales-pe

Name:               nodejs-gonzales-pe
Version:            3.0.0
Release:            0.1.%{prerelease}%{?dist}
Summary:            Gonzales Preprocessor Edition (fast CSS parser)

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/gonzales-pe
Source0:            http://registry.npmjs.org/gonzales-pe/-/gonzales-pe-3.0.0-%{prerelease}.tgz

BuildRequires:      nodejs-packaging >= 6



%if 0%{?enable_tests}
BuildRequires:      npm(coffee-script)
BuildRequires:      npm(benchmark)
BuildRequires:      npm(microtime)
BuildRequires:      npm(mocha)
%endif


%description
Gonzales is a fast CSS parser.    
Gonzales PE is a rework with support of preprocessors.    

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/gonzales-pe
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/gonzales-pe

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
(mkdir -p log && node ./test/mocha.js) | tee ./log/test.log
%endif


%files
%doc CHANGELOG.md README.md
%{nodejs_sitelib}/gonzales-pe/

%changelog
* Wed Jul 16 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.9
- Latest upstream.
- Fixed nodejs_fixdep statements.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.6
- Initial packaging for Fedora.
