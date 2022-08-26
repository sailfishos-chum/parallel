Summary:    Shell tool for executing jobs in parallel
Name:       parallel
Version:    20220822
Release:    0
License:    GPLv3+
Group:      Productivity/File utilities
URL:        https://www.gnu.org/software/parallel
Source0:    http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make

%description
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers. A job can be a single command or a small script
that has to be run for each of the lines in the input. The typical
input is a list of files, a list of hosts, a list of users, a list of
URLs, or a list of tables. A job can also be a command that reads from
a pipe. GNU Parallel can then split the input and pipe it into
commands in parallel.

If you use xargs and tee today you will find GNU Parallel very easy to
use as GNU Parallel is written to have the same options as xargs. If
you write loops in shell, you will find GNU Parallel may be able to
replace most of the loops and make them run faster by running several
jobs in parallel.

GNU Parallel makes sure output from the commands is the same output as
you would get had you run the commands sequentially. This makes it
possible to use output from GNU Parallel as input for other programs.

For each line of input GNU Parallel will execute command with the line
as arguments. If no command is given, the line of input is
executed. Several lines will be run in parallel. GNU Parallel can
often be used as a substitute for xargs or cat | bash.

%if "%{?vendor}" == "chum"
PackageName: GNU parallel
Type: console-application
DeveloperName: Free Software Foundation
PackagerName: nephros
Categories:
 - Utility
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/parallel
  Repo: https://git.savannah.gnu.org/git/parallel.git
Icon: https://www.gnu.org/software/parallel/logo-gray+black300.png
Url:
  Homepage: https://www.gnu.org/software/parallel
  Help: https://www.gnu.org/software/parallel/parallel.html
  Donations: https://my.fsf.org/donate
%endif

%prep
%setup -q -n %{name}-%{version}/upstream

%build
autoreconf --install -W gnu
%configure --disable-documentation
%make_build

%install
rm -rf %{buildroot}
%make_install

rm -rf %{buildroot}%{_mandir}/

%files
%defattr(-,root,root,-)
/usr/bin/*

