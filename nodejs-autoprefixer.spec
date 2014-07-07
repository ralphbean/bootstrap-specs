%global enable_tests 0

%global barename autoprefixer

Name:               nodejs-autoprefixer
Version:            2.1.0
Release:            1%{?dist}
Summary:            Parse CSS and add vendor prefixes to CSS rules

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/autoprefixer
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      nodejs-fs-extra
BuildRequires:      nodejs-caniuse-db
BuildRequires:      nodejs-postcss

Requires:           nodejs-fs-extra
Requires:           nodejs-caniuse-db
Requires:           nodejs-postcss

%if 0%{?enable_tests}
BuildRequires:      nodejs-stylus
BuildRequires:      nodejs-nib
BuildRequires:      nodejs-should
BuildRequires:      nodejs-browserify
BuildRequires:      nodejs-mocha
%endif


%description
Parse CSS and add vendor prefixes to CSS rules using values from the Can I Use
website

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep fs-extra
%nodejs_fixdep caniuse-db
%nodejs_fixdep postcss

%if 0%{?enable_tests}
%nodejs_fixdep --dev stylus
%nodejs_fixdep --dev nib
%nodejs_fixdep --dev should
%nodejs_fixdep --dev browserify
%nodejs_fixdep --dev mocha
%else
%nodejs_fixdep --dev -r stylus
%nodejs_fixdep --dev -r nib
%nodejs_fixdep --dev -r should
%nodejs_fixdep --dev -r browserify
%nodejs_fixdep --dev -r mocha
%endif


%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/autoprefixer
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/autoprefixer

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
mocha
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/autoprefixer/

%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 2.1.0-1
- Initial packaging for Fedora.
