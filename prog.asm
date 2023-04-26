ENTRY_POINT:
    Mov Ax, 0
    Mov Cx, 1
Ciclo:    
    Add Ax, Cx
    Inc Cx
    Cmp Cx, 10
    Jnz Ciclo
    Jmp Fin
Fin:
    Add Ax, Bx
