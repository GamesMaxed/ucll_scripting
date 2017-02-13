mov eax, DWORD PTR y$[rbp]
mov ecx, DWORD PTR x$[rbp]
add ecx, eax
mov eax, ecx
mov DWORD PTR z$[rbp], eax
