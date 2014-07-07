%global enable_tests 0

%global barename vow-queue

Name:               nodejs-vow-queue
Version:            0.3.1
Release:            1%{?dist}
Summary:            Vow-based task queue

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/vow-queue
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-vow

Requires:           nodejs-vow

%if 0%{?enable_tests}
BuildRequires:      nodejs-jscs
BuildRequires:      nodejs-vow
BuildRequires:      nodejs-jshint
BuildRequires:      nodejs-istanbul
BuildRequires:      nodejs-mocha-istanbul
BuildRequires:      nodejs-chai
BuildRequires:      nodejs-mocha
%endif


%description
vow-queue is a module for task queue with weights and priorities

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep vow

%if 0%{?enable_tests}
%nodejs_fixdep --dev jscs
%nodejs_fixdep --dev vow
%nodejs_fixdep --dev jshint
%nodejs_fixdep --dev istanbul
%nodejs_fixdep --dev mocha-istanbul
%nodejs_fixdep --dev chai
%nodejs_fixdep --dev mocha
%else
%nodejs_fixdep --dev -r jscs
%nodejs_fixdep --dev -r vow
%nodejs_fixdep --dev -r jshint
%nodejs_fixdep --dev -r istanbul
%nodejs_fixdep --dev -r mocha-istanbul
%nodejs_fixdep --dev -r chai
%nodejs_fixdep --dev -r mocha
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vow-queue
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/vow-queue

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
make validate
%endif


%files
%doc CHANGELOG.md README.md LICENSE
%{nodejs_sitelib}/vow-queue/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- Initial packaging for Fedora.
