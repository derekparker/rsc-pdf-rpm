# Run tests in check section
%bcond_without check

%global goipath         rsc.io/pdf
%global forgeurl        https://github.com/rsc/pdf
Version:                0.1.1

%global common_description %{expand:
PDF reader implemented in Go.
}

%gometa 

Name:           %{goname}
Release:        1%{?dist}
Summary:        PDF reader implemented in Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Nov 28 2018 Derek Parker <deparker@redhat.com> - 0.1.1-1
- First package for Fedora

