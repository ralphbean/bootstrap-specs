# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global barename connect-livereload

Name:               nodejs-connect-livereload
Version:            0.4.0
Release:            2%{?dist}
Summary:            Connect middleware for adding the livereload script to the response

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/connect-livereload
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif


BuildRequires:      nodejs-packaging >= 6

%description
Connect middleware for adding the livereload script to the response.  No
browser plugin is needed.  If you are happy with a browser plugin, then you
don't need this middleware.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/connect-livereload
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/connect-livereload

%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/connect-livereload/

%changelog
* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- Specify noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Initial packaging for Fedora.
