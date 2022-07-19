Có thể thấy bài này đã bị thêm opcode rác nên IDA không disassembly được 

![writeup](https://user-images.githubusercontent.com/101321172/179648262-560fae9e-3f4b-4ab3-8c42-4fbb7771f9d8.jpg)

Ngoài ra khi nhập sai flag thì chương trình sẽ bị crash
![writeup](https://user-images.githubusercontent.com/101321172/179648478-44ea09ee-6994-482d-a4c7-621c387ce793.jpg)

Debug bằng GDB, attach vào process

![writeup](https://user-images.githubusercontent.com/101321172/179648689-f8dfef52-ca11-4f26-b3f9-0c2c6ece413e.jpg)

Có thể thấy bài này được code bằng assembly, và có sử dụng ```syscall``` để nhập flag

![writeup](https://user-images.githubusercontent.com/101321172/179648840-ccb822fe-54fd-42ca-8e5a-89834a8dde28.jpg)

Có thể thấy ở đoạn này ax giữ input, và sau đó được sub 0x60.

Tiếp sau đó là sub 0x9

![writeup](https://user-images.githubusercontent.com/101321172/179648930-f65200b0-bd00-4d4e-b9db-9cbd5d5b7e37.jpg)

Và sau đó lại xor giá trị có được này với ```rip```

![writeup](https://user-images.githubusercontent.com/101321172/179649004-41640196-1c3b-4eb2-aaa0-54278b182eac.jpg)

Việc này rõ ràng sẽ khiến luồng chương trình bị rối nếu giá trị al != 0 => lỗi chương trình

=> Để chương trình không bị lỗi thì đến đoạn này al phải = 0.

=> trước đó al phải bằng = 0x60 + 0x9 = 0x69 = "i" (kí tự đầu của flag)

Các kí tự sau cũng tương tự

![writeup](https://user-images.githubusercontent.com/101321172/179649652-a44dfad8-f79b-4e21-bc0f-d86e3600f7b7.jpg)

![writeup](https://user-images.githubusercontent.com/101321172/179649420-f29c5c66-368f-4f2e-befc-12655984766a.jpg)

0x60 + 0x3 = 0x63 = "c"

=> flag: ictf{dynam1c_d3bugg1ng_1s_n1ce}
