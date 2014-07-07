# requires rubygem-jekyll which is not packaged
#%%global build_docs 1

%global enable_tests 1

Name:           bootstrap
Version:        3.1.1
Release:        2%{?dist}
Summary:        A front-end framework for developing projects on the web

License:        MIT
URL:            http://getbootstrap.com/
Source0:        https://github.com/twbs/bootstrap/archive/v%{version}/%{name}-%{version}.tar.gz

# the Gruntfile directly require()s some unnecessary JS needed only for local development
Patch1:         %{name}-disable-devel.patch

# the Gruntfile also directly require()s some stuff we don't need if we're not
# building documentation
Patch2:         %{name}-disable-docs.patch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging >= 6
BuildRequires:  fontpackages-devel
BuildRequires:  npm(grunt-cli)

BuildRequires:  npm(grunt)
BuildRequires:  npm(grunt-autoprefixer)
BuildRequires:  npm(grunt-banner)
BuildRequires:  npm(grunt-contrib-clean)
BuildRequires:  npm(grunt-contrib-concat)
BuildRequires:  npm(grunt-contrib-copy)
BuildRequires:  npm(grunt-contrib-cssmin)
BuildRequires:  npm(grunt-contrib-less)
BuildRequires:  npm(grunt-contrib-uglify)
BuildRequires:  npm(grunt-csscomb)
BuildRequires:  npm(load-grunt-tasks)

%if 0%{?enable_tests}
BuildRequires:  npm(grunt-contrib-csslint)
BuildRequires:  npm(grunt-saucelabs)
BuildRequires:  npm(grunt-contrib-connect)
BuildRequires:  npm(grunt-html-validation)
BuildRequires:  npm(grunt-jscs-checker)
%endif

%if 0%{?build_docs}
BuildRequires:  npm(grunt-jekyll)
BuildRequires:  npm(markdown)
%endif

Requires:       web-assets-filesystem
Requires:       glyphicons-halflings-fonts = %{version}-%{release}

%description
A front-end framework for developing responsive, mobile first projects on the 
web.

%if 0%{?build_docs}
%package doc
Summary:    Documentation for the Bootstrap front-end framework
Requires:   %{name} = %{version}-%{release}

%description doc
This package provides the documentation for Bootstrap in HTML format.
%endif

# only the bootstrap distribution of these fonts are free, therefore they are
# shipped here instead of seperately
%package -n glyphicons-halflings-fonts
Summary:    A library of precisely prepared monochromatic icons and symbols
Requires:   fontpackages-filesystem

%description -n glyphicons-halflings-fonts
GLYPHICONS is a library of precisely prepared monochromatic icons and symbols, 
created with an emphasis on simplicity and easy orientation.


%prep
%setup -q


# This removes the devDependencies from package.json.  Only npm respects these;
# we don't have automatic buildrequires in Fedora so when we don't "cheat" with
# npm anymore these will no longer be necessary.  (But since you can't see that
# I removed BuildRequires up there this also serves to document why certain
# dependencies were removed.)

# remove stuff only needed for local development
%patch1 -p1
%nodejs_fixdep --dev -r grunt-contrib-watch
%nodejs_fixdep --dev -r grunt-exec

# remove stuff only needed to make releases
%nodejs_fixdep --dev -r grunt-sed
%nodejs_fixdep --dev -r canonical-json

# remove stuff needed to build customizer on getbootstrap.com
%nodejs_fixdep --dev -r btoa
%nodejs_fixdep --dev -r grunt-contrib-jade

# remove nonfree dependency
%nodejs_fixdep --dev -r grunt-contrib-jshint

# don't install these if we're not running the tests
%if !(0%{?enable_tests})
%nodejs_fixdep --dev -r grunt-contrib-csslint
%nodejs_fixdep --dev -r grunt-contrib-connect
%nodejs_fixdep --dev -r grunt-contrib-qunit
%nodejs_fixdep --dev -r grunt-html-validation
%nodejs_fixdep --dev -r grunt-jscs-checker
%nodejs_fixdep --dev -r grunt-saucelabs
%endif

%if !(0%{?build_docs})
%patch2 -p1
%nodejs_fixdep --dev -r grunt-jekyll
%endif


%build
%nodejs_symlink_deps --build

# build bootstrap css from less and minify JS
grunt dist

%if 0%{?build_docs}
grunt jekyll dist-docs
%endif


%install
# install to a versioned subdirectory to allow multiple major versions to coexist
mkdir -p %{buildroot}%{_webassetdir}/%{name}/%{version}
cp -pr dist/css dist/js less %{buildroot}%{_webassetdir}/%{name}/%{version}

# symlinks to version levels people might want to depend on
# the top one might not be necessary if bootstrap doesn't break too many things
# in x.y updates
ln -sf %{version} \
    %{buildroot}%{_webassetdir}/%{name}/%(echo %{version} | cut -d. -f1-2)
ln -sf %{version} \
    %{buildroot}%{_webassetdir}/%{name}/%(echo %{version} | cut -d. -f1)
ln -sf %{version} %{buildroot}%{_webassetdir}/%{name}/latest

# install the font
mkdir -p %{buildroot}%{_datadir}/fonts/glyphicons-halflings
cp -p dist/fonts/glyphicons-halflings-regular.ttf \
    %{buildroot}%{_datadir}/fonts/glyphicons-halflings

# make it available where bootstrap expects it
mkdir -p %{buildroot}%{_webassetdir}/%{name}/%{version}/fonts
ln -sf %{_datadir}/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf \
    %{buildroot}%{_webassetdir}/%{name}/%{version}/fonts

# bundle the webfonts for now until we can do something better
cp -p dist/fonts/glyphicons-halflings-regular.{eot,svg,woff} \
    %{buildroot}%{_webassetdir}/%{name}/%{version}/fonts

# install documentation
%if 0%{?build_docs}
mkdir -p %{buildroot}%{_pkgdocdir}/html
cp -pr docs/* %{buildroot}%{_pkgdocdir}/html
%endif

%if 0%{?enable_tests}
%check
# use --force to bypass removed utilities like the nonfree jshint
grunt test --force
%endif 


%files
%{_webassetdir}/%{name}
%doc LICENSE README.md

%if 0%{?build_docs}
%files doc
%{_pkgdocdir}/html
%endif

%files -n glyphicons-halflings-fonts
%{_datadir}/fonts/glyphicons-halflings
%doc LICENSE


%changelog
* Wed Jul 02 2014 Ralph Bean <rbean@redhat.com> - 3.1.1-2
- Removed use_npm macro and associated blocks.

* Thu May 29 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.1-1
- initial package
