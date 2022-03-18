Bài yêu cầu chúng ta nhập 1 key nào đó

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159039173-3ad145c7-45ab-4d12-a94b-134245365491.jpg)

Load file vào IDA, vào hàm main

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159039471-ee45e94e-fee0-4158-adf3-cb0d51bcfbb6.jpg)

Từ hàm main có thể thấy key được check trong đoạn ```sub_1208+1```

Vào đây, chúng ta có 1 phần của flag

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159039761-88bb4586-264d-485a-89a1-1970aba02dd1.jpg)

Ok giờ bắt đầu debug chương trình

Đặt breakpoint ở đây

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159040541-c8164a5c-ff71-45dd-a65e-53c52eed3d6d.jpg)

Step vào trong hàm, step thêm 1 lúc là có được đoạn cuối của flag:

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159041590-b6714b1f-f602-4796-944e-d7365235efcb.jpg)

flag: picoCTF{br1ng_y0ur_0wn_k3y_d4bccbf6}

