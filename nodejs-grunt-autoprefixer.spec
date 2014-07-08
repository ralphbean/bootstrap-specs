# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename grunt-autoprefixer

Name:               nodejs-grunt-autoprefixer
Version:            0.8.1
Release:            1%{?dist}
Summary:            Parse CSS and add vendor-prefixed CSS properties

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/grunt-autoprefixer
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(chalk)
BuildRequires:      npm(diff)
BuildRequires:      npm(grunt)
BuildRequires:      npm(autoprefixer)

Requires:           npm(chalk)
Requires:           npm(diff)
Requires:           npm(grunt)
Requires:           npm(autoprefixer)

%if 0%{?enable_tests}
BuildRequires:      npm(time-grunt)
BuildRequires:      npm(load-grunt-tasks)
BuildRequires:      npm(grunt-contrib-nodeunit)
BuildRequires:      npm(grunt-contrib-clean)
BuildRequires:      npm(grunt-contrib-jshint)
BuildRequires:      npm(grunt)
BuildRequires:      npm(grunt-contrib-copy)
%endif


%description
Autoprefixer parses CSS and adds vendor-prefixed CSS properties using the Can I
Use database.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%if 0%{?enable_tests}
%nodejs_fixdep --caret --dev
%endif

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-autoprefixer
cp -pr package.json tasks \
    %{buildroot}%{nodejs_sitelib}/grunt-autoprefixer

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
grunt test
%endif


%files
%doc LICENSE-MIT README.md CHANGELOG
%{nodejs_sitelib}/grunt-autoprefixer/

%changelog
* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.8.1-1
- Initial packaging for Fedora.