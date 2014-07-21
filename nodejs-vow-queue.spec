# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename vow-queue

Name:               nodejs-vow-queue
Version:            0.3.1
Release:            2%{?dist}
Summary:            Vow-based task queue

Group:              Development/Libraries
License:            MIT and GPLv3+
URL:                https://www.npmjs.org/package/vow-queue
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(vow)

Requires:           npm(vow)

%if 0%{?enable_tests}
BuildRequires:      npm(jscs)
BuildRequires:      npm(vow)
BuildRequires:      npm(jshint)
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha-istanbul)
BuildRequires:      npm(chai)
BuildRequires:      npm(mocha)
%endif


%description
vow-queue is a module for task queue with weights and priorities

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

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
* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.3.1-2
- Completed license field.
- Specified noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- Initial packaging for Fedora.
