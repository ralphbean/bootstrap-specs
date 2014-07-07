%global enable_tests 0

%global barename vow-fs

Name:               nodejs-vow-fs
Version:            0.3.2
Release:            1%{?dist}
Summary:            File I/O by Vow

Group:              Development/Libraries
# https://github.com/dfilatov/vow-fs/blob/master/lib/fs.js
License:            MIT and GPLv3
URL:                https://www.npmjs.org/package/vow-fs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-node-uuid
BuildRequires:      nodejs-glob
BuildRequires:      nodejs-vow
BuildRequires:      nodejs-vow-queue

Requires:           nodejs-node-uuid
Requires:           nodejs-glob
Requires:           nodejs-vow
Requires:           nodejs-vow-queue

%if 0%{?enable_tests}
BuildRequires:      nodejs-nodeunit
BuildRequires:      nodejs-istanbul
%endif


%description
[Vow](https://github.com/dfilatov/vow)-based file I/O for Node.js

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep node-uuid
%nodejs_fixdep glob
%nodejs_fixdep vow
%nodejs_fixdep vow-queue

%if 0%{?enable_tests}
%nodejs_fixdep --dev nodeunit
%nodejs_fixdep --dev istanbul
%else
%nodejs_fixdep --dev -r nodeunit
%nodejs_fixdep --dev -r istanbul
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vow-fs
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/vow-fs

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
./node_modules/istanbul/lib/cli.js test test/runner.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/vow-fs/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.3.2-1
- Initial packaging for Fedora.
