Bài yêu cầu chúng ta nhập 1 số nào đó

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159034948-7f55bf8c-4a16-40c3-b565-f3beed1321a3.jpg)

Từ phần hint, có thể thấy bài pack bằng UPX

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159035275-7a445cb7-c0ab-4f77-99d8-64f7470d9f6f.jpg)

Load file vào IDA

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159035683-01aa8d4a-3086-42b0-a762-ec5367594d86.jpg)

Tuy nhiên các câu lệnh vẫn được thực thi một cách hoàn toàn bình thường dù bị pack, nên chúng ta có thể thấy được các câu lệnh khi debug :v

Attach vào tiến trình khi đã nhập được số, ta có:

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159036696-1266ca29-0995-4c7e-83a6-2feb4ce62651.jpg)

Mẹo nhỏ là IDA cho phép chúng ta search string:

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159037922-fb0bd551-8c26-4790-b9cd-2c7ffee39c04.jpg)

Vào đoạn code có string này, chúng ta có thể thấy input chúng ta nhập được so sánh với 0xB83CB

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159038239-59816761-b247-434e-bf0a-c9b19a84718f.jpg)

(0x311 = 785 = input của chúng ta)

Từ đó thấy được chúng ta cần nhập input = 0xB83CB = 754635

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159038547-4739d7ba-ce43-4178-8638-22a861d671aa.jpg)
