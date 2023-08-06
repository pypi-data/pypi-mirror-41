dfilter-python：机器学习一些统计量的分析工具
===============================

**注意: 本项目维护更新看作者心情！**

.. contents::


介绍
----

dfilter-python 采用 Python2.7 编写。

import，很简单：

.. code-block:: python

    import dfilter



快速开始
---------

准备
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Tips** :

1.  确保你的系统里面已经安装了 `Python2.7 <https://www.python.org/>`_ ，不同作业系统如何安装不再赘述。
2.  检查你系统中 `python` 和 `pip` 的版本, 如果不属于 `python2.7` , 请在执行代码范例时，自行将 `python` 和 `pip` 分别替换成 `python2.7` 和 `pip2` 。
3.  确保你的系统中安装了 `git` 程序 以及 `python-pip` 。




函数使用 ----在 pandas 后
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 **get_colume_name_as_list** (dataframe)

  得到数据的列名称。

 **basic_info** (dataframe，列名)

  得到数据列的基础信息。

 **get_coverage** (dataframe，列名)

  得到数据列元素的覆盖率。

 **get_pearson_similarity** (dataframe，列名1，列名2，是否均值填充空值)

  得到数据的皮尔逊相关系数。

 **get_fisher_score** (dataframe，列名1，y[列表]，是否均值填充空值)

  得到数据的Fisher得分。

 **get_fisher_score_with_list** (dataframe，[列名1,列名2，.....]，y[列表]，是否均值填充空值)

  输入列中元素的Fisher得分。

 **get_K_L_divergence** (dataframe，列名1，列名2)

  输入列中元素的KL散度

 **get_K_L_divergence_as_list** (dataframe，[列名1,列名2，.....])

  输入列中元素的KL散度。

 **get_K_L_divergence_as_list_with_y** (dataframe，[列名1,列名2，.....]，y[列表])

  输入列中元素的KL散度。

 **check_normal_cluster** (dataframe，列名，是否均值填充空值)

  输入列中元素的 正态检验

 **get_homogeneity_of_variance** (dataframe，列名1，列名2，是否均值填充空值)

  输入列中元素的 方差齐性检验

 **compare_between_two_couples** (dataframe，列名1，列名2，是否均值填充空值)

  输入列中元素的 两组数之间的比较


