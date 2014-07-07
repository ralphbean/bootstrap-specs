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

BuildRequires:      nodejs-chalk
BuildRequires:      nodejs-diff
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-autoprefixer

Requires:           nodejs-chalk
Requires:           nodejs-diff
Requires:           nodejs-grunt
Requires:           nodejs-autoprefixer

%if 0%{?enable_tests}
BuildRequires:      nodejs-time-grunt
BuildRequires:      nodejs-load-grunt-tasks
BuildRequires:      nodejs-grunt-contrib-nodeunit
BuildRequires:      nodejs-grunt-contrib-clean
BuildRequires:      nodejs-grunt-contrib-jshint
BuildRequires:      nodejs-grunt
BuildRequires:      nodejs-grunt-contrib-copy
%endif


%description
Autoprefixer parses CSS and adds vendor-prefixed CSS properties using the Can I
Use database.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep chalk
%nodejs_fixdep diff
%nodejs_fixdep grunt
%nodejs_fixdep autoprefixer

%if 0%{?enable_tests}
%nodejs_fixdep --dev time-grunt
%nodejs_fixdep --dev load-grunt-tasks
%nodejs_fixdep --dev grunt-contrib-nodeunit
%nodejs_fixdep --dev grunt-contrib-clean
%nodejs_fixdep --dev grunt-contrib-jshint
%nodejs_fixdep --dev grunt
%nodejs_fixdep --dev grunt-contrib-copy
%else
%nodejs_fixdep --dev -r time-grunt
%nodejs_fixdep --dev -r load-grunt-tasks
%nodejs_fixdep --dev -r grunt-contrib-nodeunit
%nodejs_fixdep --dev -r grunt-contrib-clean
%nodejs_fixdep --dev -r grunt-contrib-jshint
%nodejs_fixdep --dev -r grunt
%nodejs_fixdep --dev -r grunt-contrib-copy
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
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 0.8.1-1
- Initial packaging for Fedora.
