def tipoTriangulo(l1,l2,l3):
    if (l1 == l2) and (l1 == l2):
        return 'Equilátero - Lados: {:.2f}, {:.2f} e {:.2f}'.format(l1,l2,l3)
    elif (l1==l2) or (l1==l3) or (l2==l3):
        return 'Isóceles - Lados: {:.2f}, {:.2f} e {:.2f}'.format(l1,l2,l3)
    else:
        return 'Escaleno - Lados: {:.2f}, {:.2f} e {:.2f}'.format(l1,l2,l3)

print(tipoTriangulo(2,3,4))