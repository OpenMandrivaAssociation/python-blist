# Created by pyp2rpm-1.0.1
%global pypi_name blist

# This package is unmaintained upstream. Check its github PRs for
# important fixes when working on the package.
# https://github.com/DanielStutzbach/blist/pulls

Name:           python-blist
Version:        1.3.6
Release:        6
Group:          Development/Python
Summary:        a list-like type with better asymptotic performance and similar performance on small lists
License:        BSD
URL:            http://pypi.python.org/pypi/blist/
Source0:        https://pypi.python.org/packages/source/b/blist/blist-%{version}.tar.gz
#Patch0:		https://github.com/DanielStutzbach/blist/pull/84.patch
#Patch1:		https://github.com/DanielStutzbach/blist/pull/85.patch
#Patch2:		https://github.com/DanielStutzbach/blist/pull/91.patch
#Patch3:		https://github.com/DanielStutzbach/blist/pull/92.patch
Patch4:         0001CatchStopIterationinageneratorandreturninstea.patch
Patch5:         python3.9.patch
Patch6:         python3.11.patch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
The blist is a drop-in replacement for the Python list the
provides better performance when modifying large lists.

The blist package also provides sortedlist, sortedset,
weaksortedlist, weaksortedset, sorteddict, and btuple
types.

%prep
%setup -q -n %{pypi_name}-%{version}
%autopatch -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitearch}/*
