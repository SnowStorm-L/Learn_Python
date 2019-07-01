## LinearLayout 学习



[官网文档](https://developer.android.com/reference/android/widget/LinearLayout) (需要VPN打开)

LinearLayout的内容排布方向默认是 `android:orientation="horizontal` 横向排布




> 设置控件摆放位置

1. `android:layout_gravity` 和 `android: gravity`

    **gravity是设置自身内部元素的对齐方式**

   ​	比如一个TextView，则是设置内部文字的对齐方式。
   ​	如果是ViewGroup组件如LinearLayout的话，则为设置它内部view组件的对齐方式。

   

   **layout_gravity是设置自身相当于父容器的对齐方式**

   ​	比如，一个TextView设置layout_gravity属性，则表示这TextView相对于父容器的对齐方式。

   

   **注意事项**

    1.  **可以多个属性一起使用, 例如设置控件为右上:  `android:layout_gravity="right|left"`**

    2.  **如果要用`gravity`属性，此组件的`layout_width`和`layout_height`不能设置为`wrap_content`。此时设置的`gravity`属性没有效果，因为组件包裹着内容，无论设置什么，也都不能有改变**

    3.  **对于`layout_gravity`不是什么情况下都能设置的属性（如RelativeLayout），而且在不同的viewGroup中产生的效果也会不同（如LinearLayout)**

        例如:

        ```java
        <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:background="#f00"
                android:orientation="horizontal">
                <TextView
                    android:text="TextView在这里"
                    android:layout_width="200dp"
                    android:layout_height="200dp"
                    android:background="#ff0"
                    android:layout_gravity="center"/>
        </LinearLayout>
        ```

        此时layout_gravity的center值，并没有让TextVieW在LinearLayout的中间，这和LinearLayout的orientation的定位方向有关。

        当设置为horizontal时，LinearLayout中的组件时按照横着排列，当设置layout_gravity属性为center值时，组件就在垂直方向处于中间位置。

        当设置为vertical时, 同理.

   

   **可设置的属性**

   ​	layout_gravity 和  gravity 它们两个可设置的属性都一样

   - 居左

     `android:layout_gravity=“left"` 
     `android:layout_gravity=“start"`

   - 居右

     `android:layout_gravity=“right"`

     `android:layout_gravity="end"`

   - 居上

     `android:layout_gravity=“top"`

   - 居下

     `android:layout_gravity=“bottom"`

   - 居中

     `android:layout_gravity=“center"`

   - 水平居中

     `android:layout_gravity="center_horizontal"`

   - 垂直居中

     `android:layout_gravity="center_vertical"`

   - 充满容器

     `android:layout_gravity="fill"`

   - 水平方向充满容器

     `android:layout_gravity=“fill_horizontal"`

   - 垂直方向充满容器

     `android:layout_gravity=“fill_vertical"`

   - 水平裁剪

     `android:layout_gravity=“clip_horizontal"`

   - 垂直裁剪

     `android:layout_gravity=“clip_vertical”`

     当对象边缘超出容器的时候，将上下边缘超出的部分剪切掉，剪切基于纵向对齐设置

     默认剪切底部, 注意此属性要在父容器中设置,并且子视图高度比父视图高度高

     

> 权重

   1.    `android:layout_weight`

         ```java
         		<View
                 android:id="@+id/v1"
                 android:layout_width="0dp"
                 android:layout_height="70dp"
                 android:layout_weight="1"
                 android:background="@android:color/holo_red_dark" />
             <View
                 android:id="@+id/v2"
                 android:layout_width="0dp"
                 android:layout_height="70dp"
                 android:layout_weight="5"
                 android:background="@android:color/holo_blue_bright" />
         ```

         `width = 0dp` 和 `wrap_content` 同样的效果  都是按照1:5的权重分配视图的

         `width = match_parent`(旧的API是`fill_parent`) 的效果则不同, 分配例子如下:

         ​	v1, v2 都是match_parent, 他们的parent 宽度用W表示

         ​	设定的长度为W(屏幕一共就W宽)
         ​	给予的长度为2W(v1, v2 都是`match_parent` W+W)

         ​	剩余长度: W - 2W = -W
         ​	v1的宽度 = W(设定的长度为) + (-W) * 1/(1+5) (占的比率) = 5/6 W
         ​	v2的高度 = W(设定的长度为) + (-W) * 5/(1+5) (占的比率) = 1/6 W

         公式:
           	**View的宽度 = 设定+剩余*百分比**

         

> margin 外边距

  -   离某元素底边缘的距离 

      `android:layout_marginBottom`

- 离某元素左边缘的距离 

  `android:layout_marginLeft`

  `android:layout_marginStart`

- 离某元素右边缘的距离 

  `android:layout_marginRight`

  `android:layout_marginEnd`

- 离某元素上边缘的距离

  `android:layout_marginTop`

- 离某元素左右边缘的距离 (相当于同时设置`android:layout_marginLeft`和`android:layout_marginRight`)

  `android:layout_marginHorizontal`(API 26 或以上才能使用)

- 离某元素上下边缘的距离 (相当于同时设置`android:layout_marginTop`和`android:layout_marginBottom`)

  `android:layout_marginVertical`(API 26 或以上才能使用)

- 距离某元素 上,下,左,右 的外边距

  `android:layout_margin`



**当我们采用LinearLayout布局时，有以下特殊情况需要我们注意:**

 1.  当 `android:orientation=“vertical"`  时， `android:layout_gravity`只有水平方向的设置才起作用, 垂直方向的设置不起作用。

     即: left，right，center_horizontal 是生效的。

2. 当 `android:orientation=“horizontal"` 时， `android:layout_gravity`只有垂直方向的设置才起作用, 水平方向的设置不起作用。

    即: top，bottom，center_vertical 是生效的。