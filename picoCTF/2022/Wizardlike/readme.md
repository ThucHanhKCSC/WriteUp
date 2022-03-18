Đây là 1 trong những bài CTF hay nhất em từng chơi :v 

Đó là 1 game mê cung, yêu cầu chúng ta tìm flag trong cái mê cung này

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159042050-70bb72c5-9715-451c-b144-917d6b2192df.jpg)

Tuy nhiên sau 1 lúc tìm hiểu thì có thể thấy dù đã cố qua tất cả các map nhưng không có cách nào có được flag

Từ việc đọc hind => phải đi xuyên tường mới có thể tìm được flag

Vào hàm main, có thể thấy các đoạn code update lệnh dịch chuyển

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159042670-61a52c63-1dd5-48e2-b6e4-7ff613afa069.jpg)

Trong các tựa game 2D cơ bản, luôn có khái niệm: ```playerX - vị trí nhân vật trên tọa độ X```, ```playerY - vị trí nhân vật trên tọa độ Y``` và ```playerPos - Vị trí nhân vật hiển thị```  để chỉ vị trí nhân vật

Vào 1 hàm update vị trí bất kì, có thể thấy hàm playerPos

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159043029-33e6c85e-ccd0-487d-b8fc-8ef82f1e687b.jpg)

Nếu chúng ta muốn xuyên tường, thì phải tìm được đoạn code ký tự tường ```#``` và ký tự rỗng ``` ``` không cho phép chúng ta đi qua

May mắn là hàm playerPos có đoạn ktra đó rõ với IDA

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159043725-8acf3470-a068-454b-82dc-22f39d48d12f.jpg)

Giờ nhiệm vụ của chúng ta là chuyển lệnh jmp, Có thể hiểu là dù ktra thế nào thì vẫn jump update playerPos

Sau khi patch:
![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044113-d5482479-9672-401d-8dc0-464b8c83a206.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044237-4b6f1caf-6f0c-4137-9494-bc3bece7c88c.jpg)

Ok giờ tự do đi lại :D

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044319-f4c4433d-3fbe-4216-b03f-c690ecb94734.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044420-fe7c0eb8-c633-481c-809c-013431ca1e83.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044506-a0a297cf-466c-4ad7-9fcb-1640b1710241.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044591-df7a65af-d4cc-4643-ad40-7b2cdc161026.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044712-b284c028-33f7-4607-a954-9400ee019f83.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044791-6681b5b6-04cf-4130-8a90-c4d9c5811c82.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044862-f1629869-8321-4754-86f3-22afc9aca90f.jpg)


(Số 5 đấy :( nhìn lòi mắt)
![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159044955-8accab68-2666-400e-9da3-1916285546db.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159045091-22f52339-6e14-456a-b595-f8aaa1245aec.jpg)

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159045214-354802a1-3099-438e-a25b-f888558d6a1c.jpg)


flag: picoCTF{ur_4_w1z4rd_4B0DA5A9}
