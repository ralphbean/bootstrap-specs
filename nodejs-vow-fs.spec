# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(node-uuid)
BuildRequires:      npm(glob)
BuildRequires:      npm(vow)
BuildRequires:      npm(vow-queue)

Requires:           npm(node-uuid)
Requires:           npm(glob)
Requires:           npm(vow)
Requires:           npm(vow-queue)

%if 0%{?enable_tests}
BuildRequires:      npm(nodeunit)
BuildRequires:      npm(istanbul)
%endif


%description
[Vow](https://github.com/dfilatov/vow)-based file I/O for Node.js

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep glob ^3.2

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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.3.2-1
- Initial packaging for Fedora.
