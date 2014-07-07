%global enable_tests 0
%global prerelease 6
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
BuildRequires:      nodejs-coffee-script
BuildRequires:      nodejs-benchmark
BuildRequires:      nodejs-microtime
BuildRequires:      nodejs-mocha
%endif


%description
Gonzales is a fast CSS parser.    
Gonzales PE is a rework with support of preprocessors.    

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/


%if 0%{?enable_tests}
%nodejs_fixdep --dev coffee-script
%nodejs_fixdep --dev benchmark
%nodejs_fixdep --dev microtime
%nodejs_fixdep --dev mocha
%else
%nodejs_fixdep --dev -r coffee-script
%nodejs_fixdep --dev -r benchmark
%nodejs_fixdep --dev -r microtime
%nodejs_fixdep --dev -r mocha
%endif


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
(make && mkdir -p log && node ./test/mocha.js) | tee ./log/test.log
%endif


%files
%doc CHANGELOG.md README.md
%{nodejs_sitelib}/gonzales-pe/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 3.0.0-0.1.6
- Initial packaging for Fedora.