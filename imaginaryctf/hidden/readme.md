Debug file, attach vào process khi đã nhập được flag rồi step qua từng bước, ta sẽ thấy flag nhập vào được xor với 1 key nào đó

![writeup](https://user-images.githubusercontent.com/101321172/179646985-21afbd58-4228-4096-a79e-0a9212e17361.jpg)

Key đó sẽ xor 8 chữ số lần lượt với 0x1C417CF092EDB590
![writeup](https://user-images.githubusercontent.com/101321172/179647033-786123b0-f031-4f74-ad84-db109aa9b8ad.jpg)

Rồi sau đó kết quả sẽ được só sánh với

![writeup](https://user-images.githubusercontent.com/101321172/179647421-7e0921d4-b0ea-442f-a154-16613efb1cae.jpg)

=> Xor ngược lại là được:

![writeup](https://user-images.githubusercontent.com/101321172/179647613-6028fc7f-f5d2-4ee2-8472-1005eea8cec0.jpg)

Làm tương tự các bước còn lại:

![writeup](https://user-images.githubusercontent.com/101321172/179647731-379fd8af-c4aa-43b7-8317-adc04ec0f5e2.jpg)

![image](https://user-images.githubusercontent.com/101321172/179647758-1e544639-eb1f-43fa-91ac-bb3af30a2889.png)

![writeup](https://user-images.githubusercontent.com/101321172/179647928-8e0a2f78-fd32-4298-a855-205c95afe1a9.jpg)

flag: ictf{h1ddenc0de_1a29d3}
