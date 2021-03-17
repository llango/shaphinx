%define name shaphinx
%define version 0.1.2
%define unmangled_version 0.1.2
%define release 1

Summary: Just a sphinx theme.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: rontom <rontomai@gmail.com>
Url: https://github.com/llango/shaphinx

%description
==============
Shaphinx - 一个 Sphinx 主题
==============


.. image:: https://img.shields.io/pypi/v/shaphinx.svg
        :target: https://pypi.python.org/pypi/shaphinx

.. image:: https://img.shields.io/travis/llango/shaphinx.svg
        :target: https://travis-ci.com/llango/shaphinx

.. image:: https://readthedocs.org/projects/shaphinx/badge/?version=latest
        :target: https://shaphinx.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




该主题是我用于火葱科技文档编写的主题，绝对不错，特意开源分享出来。你可以试试。


* 免费软件: MIT license
* 文档: https://shaphinx.readthedocs.io.

特征
--------

* 主题比较清新，参考gitbook等主题。

名单
-------

该包使用 Cookiecutter_ 和 `audreyr/cookiecutter-pypackage`_ 项目模板创建.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


=======
历史
=======

0.1.0 (2021-03-16)
0.1.2 (2021-03-17)
------------------

* 首个版本，欢迎使用提出bug.


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
