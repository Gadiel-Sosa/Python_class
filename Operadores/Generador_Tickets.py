print('*** generación de ticket de venta ***')
precio_leche = float(input('Captura el precio de la leche: '))
precio_pan = float(input('Captura el prcio del pan: '))
precio_lechuga = float(input('Captura el precio de la lechuga: '))
precio_platanos = float(input('Captura el precio de los platanos: '))

precio_sin_impuestos = precio_leche + precio_platanos + precio_lechuga + precio_pan

precio_impuesto = precio_sin_impuestos * 0.16

total_compra = precio_sin_impuestos + precio_impuesto

descuento = int(input('Aplicar algún desceunto (%)? '))
total_descuento = total_compra * (descuento/100)
total_con_descuento = total_compra - total_descuento


print(f"""
Subtotal: ${precio_sin_impuestos:.2f}
Impuesto: ${precio_impuesto:.2f}
Total con impuesto: ${total_compra:.2f}
Descuento ({descuento}%): ${total_descuento:.2f}
Total final: ${total_con_descuento:.2f}
""")