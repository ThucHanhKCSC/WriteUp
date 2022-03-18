Làm theo chính xác yêu cầu của đề
```
$ chmod +x gdbme              //Lấy quyền execute
$ gdb gdbme                   //Vào gdb
(gdb) layout asm              //Dòng này không cần thiết, để view asm
(gdb) break *(main+99)        //Breakpoint ở địa chỉ *(main+99)
(gdb) run                     //Chạy chương trình
(gdb) jump *(main+104)        //Jump đến địa chỉ *(main+104)
```

![New Bitmap Image](https://user-images.githubusercontent.com/101321172/159029396-cc937c3c-bc3d-4af4-9a61-288b6ab33dfa.jpg)

flag: picoCTF{d3bugg3r_dr1v3_50e616ac}
