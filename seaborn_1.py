# -*- coding: utf-8 -*-
"""seaborn_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b5sFqpuM-zmFMZzTVVvy-AeyHt3ZZ9yv
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset("tips") # cos nhieu sns build-in 
tips_df.head()

"""# Box plot"""

#@title Box plot definition { vertical-output: true }
variable_name = "hue component split boxplot along object." #@param {type:"string"}
sns.boxplot(data = tips_df, x = "day", y = "total_bill", hue="sex", palette  = "Blues");
plt.legend(loc=0)
# cần tính xem số lượng bill theo ngày chênh lệch bao nhiêu. bao nhiêu đơn trung bình
# bao nhiêu đơn ít, sai số bao nhiêu
# có bao nhiêu giá trị ngoại lai(vượt quá só với số liệu trung bình )
# trung bình đàn ông trả nhiều tiền hơn phụ nữa, và mức trung bình cũng lớn hơn
# các giá trị max và min cũng chênh lệch 
# các giá trị ngoại lai cũng chỉ có một số

"""# FacetGrib"""

#@title Figure of FaceGrib { run: "auto", vertical-output: true }
variable_name = "map function in FacetGrid" #@param {type:"string"}
# cho phép vẽ trong không gian 3 biến và nhiều hơn
# Create a class instance of FacetGrid class
tips_fg = sns.FacetGrid(data=tips_df, row="smoker",col ="time")
tips_fg.map(sns.scatterplot,"total_bill","tip");
# Figure sẽ chia dựa trên giá trị của smoker và chia theo thời điểm
# hàm Map sẽ giúp định hình cho sns biểu đồ thích hợp phân theo dòng và côt
# từ đây ta có thể đánh giá được nhiều đối tượng khác nhau

"""Facetgrid"""

#@title Vi du 2 { vertical-output: true }
kws = dict(s=100,edgecolor="b",alpha=0.7)
new_fg = sns.FacetGrid(data=tips_df, col ="sex",
                       hue="smoker", col_order=["Female","Male"],
                       palette ="Set2",
                       height = 4, aspect= 1.4)
new_fg.map(sns.scatterplot,"total_bill","tip", **kws)
new_fg.add_legend();
#tạo 1 class kws để sử dụng cho tất cả
# Specify bằng các parameter trong định nghĩa
# hàm add_legend() đc gọi để thêm legend
# không sử dungn=j đc legend(), vì phía trên không ghi label cho các phần

# hue nó sẽ xét đối tượng như 1 obj. tuy nhiên obj đó lại xét trong 1 mqh khác

"""# Joint plot"""

#@title Joint Plot { vertical-output: true }
penguins_df =sns.load_dataset("penguins")
penguins_df.head()
sns.jointplot(data=penguins_df, x="flipper_length_mm",y="bill_depth_mm",hue = "species");

# Nhận xét được tỉ lệ giữa fllipper và bill của penguins theo từng loài
# băt cặp 2 giá trị tương quan tuyến tính, đặt theo trục x và trục y
# fig sẽ thể hiện dựa trên các chấm nhỏ và có biểu đồ đường kde thể hiện
# thể hiện được sự giao nhau trong các phần tử

"""# Pair Plot"""

#@title How to pair plot { vertical-output: true }
sns.pairplot(data=penguins_df, hue ='species');

# thiết lập các bảng số liệu thông số thông qua hue
# bằng cách đó, chúng ta có thể bắt cặp được các giá trị tương quanquan

"""# Heat MapMap"""

#@title Sử dụng pivot_table trong pd để làm lại table { vertical-output: true }
flight_df = sns.load_dataset("flights")
flight_df.head(15)

flights = pd.pivot_table(flight_df,index="month",columns="year",values="passengers")
flights
sns.heatmap(data=flights,cmap="Blues");

# dung pivot_table để biểu thị lại bảng giá trị, với các col và obj

"""# Ví dụ thực """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

cereal_df = pd.read_csv("cereal.csv")

#irrelevent data
fields = ['shelf','weight','cups','rating']
cereal_df_new = cereal_df.drop(fields,axis = 1) # axis 1 giup xoa gia trij cot
cereal_corr = cereal_df_new.corr()
cereal_corr

#@title lọc giá trị về 1 thành phần

ones_corr = np.ones_like(cereal_corr, dtype = bool)
mask = np.triu(ones_corr) # dua ve dang matrix tam giac voi mot nua True-False

sns.heatmap(data = cereal_corr,mask = mask);

from seaborn.utils import adjust_legend_subtitles
# Điều chỉnh giá trị True Flase trong Mask
adjusted_mask = mask[1:,:-1]
adjusted_mask
adjusted_cereal_corr = cereal_corr.iloc[1:,:-1]
# bo di dong 1, cot cuoi trong data


cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True)

fig,ax = plt.subplots(figsize=(10,8))
sns.heatmap(data=adjusted_cereal_corr,mask = adjusted_mask,annot=True,annot_kws={'fontsize':13},fmt=".2f",cmap=cmap,
            vmin = -1, vmax = 1, linecolor = "white",linewidth=0.9);
# gia tri annot va annot_kws se dieu chinh cac thong so ve so trong moi bins
# annot_kws co the dieu chinh nhu 1 kws ca ve fontsize, color, alpha..............)

yticks = [i.upper() for i in adjusted_cereal_corr.index] # cau truc lay 1 list 
xticks = [i.upper() for i in adjusted_cereal_corr.columns]
print(yticks)
print(xticks)

# thuc hien cau lenh set_ de dieu chinh thong so
# plt.set() thi chi dung o plt
ax.set_yticklabels(yticks, rotation=0, fontsize=13);
ax.set_xticklabels(xticks, rotation=90, fontsize=13); 
title = 'CORRELATION MATRIX\nSAMPLED CEREALS COMPOSITION\n'
ax.set_title(title, loc='left', fontsize=18)

# tao bien kws
# dung gia tri cmap(tuy chinh)
#seaborn.husl_palette(n_colors=6, h=0.01, s=0.9, l=0.65, as_cmap=False)
