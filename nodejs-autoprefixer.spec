# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

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

BuildRequires:      npm(fs-extra)
BuildRequires:      npm(caniuse-db)
BuildRequires:      npm(postcss)

Requires:           npm(fs-extra)
Requires:           npm(caniuse-db)
Requires:           npm(postcss)

%if 0%{?enable_tests}
BuildRequires:      npm(stylus)
BuildRequires:      npm(nib)
BuildRequires:      npm(should)
BuildRequires:      npm(browserify)
BuildRequires:      npm(mocha)
%endif


%description
Parse CSS and add vendor prefixes to CSS rules using values from the Can I Use
website

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep fs-extra ~0.x

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
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
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 2.1.0-1
- Initial packaging for Fedora.
