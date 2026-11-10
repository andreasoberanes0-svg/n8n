import sys
IMG = sys.argv[1] == "shopify"
ROW = '<tr><td style="padding:10px 0;border-bottom:1px solid #eee;font:15px Arial,sans-serif;color:#111"><b>{n}</b>{d}</td><td align="right" style="padding:10px 0;border-bottom:1px solid #eee;font:14px Arial,sans-serif;color:#999;text-decoration:line-through;white-space:nowrap">{v}</td><td align="right" style="padding:10px 0 10px 12px;border-bottom:1px solid #eee;font:bold 17px Arial,sans-serif;color:#d0021b;white-space:nowrap">{p}</td></tr>'
def rows(items):
    out=[]
    for n,d,v,p in items:
        dd = f'<br><span style="font-size:12px;color:#777;font-weight:normal">{d}</span>' if d else ''
        out.append(ROW.format(n=n,d=dd,v=v,p=p))
    return "".join(out)
def sec(t, items):
    return f'<tr><td style="padding:26px 28px 0"><div style="font:bold 14px Arial,sans-serif;color:#d0021b;letter-spacing:1px">{t}</div><table width="100%" cellpadding="0" cellspacing="0" role="presentation">{rows(items)}</table></td></tr>'
ed=[("GOAT Series Edición Buen Fade","Combo + insumos + tijeras + capa · producto estrella","$4,640","$3,199"),
("Predator Edición Buen Fade","Combo + insumos + tijeras + capa · pocas piezas","$4,640","$3,199"),
("GOAT Edición Buen Fade","Combo + tijeras + capa","$3,350","$2,199"),
("Joker Edición Buen Fade","Combo + capa","$2,750","$1,999")]
goat=[("Clipper GOAT","","$2,000","$1,400"),("Trimmer GOAT","","$1,500","$1,100"),("Shaver GOAT","","$1,300","$899")]
R="+ recortadora Wahl de regalo"
wahl=[("Barber Combo Cordless",R,"$3,500","$2,799"),("Senior 2.0",R,"$4,000","$3,300"),("Vapor Switch",R,"$4,000","$3,200"),("Magic Gold",R,"$3,500","$2,800"),("Vapor CE",R,"$3,500","$2,600"),("Barber Combo de cable",R,"$2,700","$1,900"),("Magic Black",R,"$2,500","$1,900"),("Combo Launch",R,"$2,700","$1,800"),("Micro Power",R,"$1,700","$1,000"),("Aceite Wahl","","$100","$60")]
otras=[("BaBylissPRO Clipper Gold FX Plus","","$2,800","$1,999"),("Combo Black Boost","Clipper + trimmer","$4,800","$3,999"),("Shaver One Black","","$2,800","$2,199"),("Navajas LV3","","$160","$100"),("Porta navaja Turkish LV3 + Dorco","","$300","$150"),("Niveles metálicos Barber Shop","","$300","$150"),("3 After Soy Barber 300 ml","","$360","$200"),("Tapete de estación","","$300","$150")]
hero = '<tr><td><img src="https://cdn.shopify.com/s/files/1/0679/6784/4632/files/bf-hero-mochila.png?v=1794032517" width="600" alt="Mochila para barbero llena con máquinas, tijeras e insumos" style="display:block;width:100%;height:auto;border:0"></td></tr>' if IMG else ''
wimg = '<tr><td align="center" style="padding:18px 28px 0"><img src="https://cdn.shopify.com/s/files/1/0679/6784/4632/files/bf-wahl-aio.png?v=1794030474" width="260" alt="Recortadora Wahl All in One de regalo" style="display:block;width:260px;max-width:100%;height:auto;border:0"></td></tr>' if IMG else ''
name = "{{ customer.first_name | default: 'barbero' }}" if IMG else "barbero"
btn = '<a href="https://soybarber.com/discount/BUENFADE" style="display:inline-block;background:#d0021b;color:#fff;font:bold 16px Arial,sans-serif;text-decoration:none;padding:15px 34px;border-radius:4px">COMPRAR CON MIS PRECIOS</a>'
box = lambda t,s: f'<td width="33%" valign="top" style="background:#111;padding:14px 12px;font:12px Arial,sans-serif;color:#ccc"><div style="font:bold 14px Arial,sans-serif;color:#fff;padding-bottom:4px">{t}</div>{s}</td>'
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>El Buen Fade 2026</title></head>
<body style="margin:0;padding:0;background:#f2f2f2">
<div style="display:none;max-height:0;overflow:hidden">Del 10 al 12 de noviembre solo para registrados: mochila gratis desde $2,500 y los precios de El Buen Fade.</div>
<table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="background:#f2f2f2"><tr><td align="center" style="padding:20px 10px">
<table width="600" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;max-width:600px;background:#fff">
<tr><td style="background:#111;padding:22px 28px;font:bold 26px Arial,sans-serif;color:#fff;letter-spacing:1px">EL BUEN FADE 2026<div style="font:13px Arial,sans-serif;color:#d0021b;letter-spacing:2px;padding-top:4px">SOY BARBER · ACCESO REGISTRADOS</div></td></tr>
{hero}
<tr><td style="padding:28px 28px 6px;font:16px/1.5 Arial,sans-serif;color:#222">
<p style="margin:0 0 12px;font:bold 22px Arial,sans-serif;color:#111">Hola, {name}: ya empezó tu acceso anticipado.</p>
<p style="margin:0 0 12px">Por haberte registrado, del <b>10 al 12 de noviembre</b> tienes los precios de El Buen Fade antes que todos, y la <b>mochila de barbero gratis desde $2,500</b>. El 13 abrimos para todos y la mochila ya será arriba de $3,500.</p>
<p style="margin:0">Usa tu código al pagar:</p></td></tr>
<tr><td align="center" style="padding:10px 28px 6px"><div style="border:2px dashed #d0021b;padding:14px 10px;font:bold 30px Arial,sans-serif;color:#111;letter-spacing:4px">BUENFADE</div><div style="font:12px Arial,sans-serif;color:#777;padding-top:6px">Válido del 10 al 12 de noviembre en soybarber.com</div></td></tr>
<tr><td align="center" style="padding:18px 28px 4px">{btn}</td></tr>
<tr><td style="padding:22px 28px 0"><table width="100%" cellpadding="0" cellspacing="4" role="presentation"><tr>
{box("Mochila gratis","Desde $2,500, solo registrados del 10 al 12. Una por pedido.")}
{box("Recortadora Wahl gratis","En toda máquina Wahl. Valor $500.")}
{box("Envío gratis","En compras desde $2,500.")}
</tr></table></td></tr>
{sec("SBM · EDICIONES BUEN FADE", ed)}
{sec("SBM · GOAT POR PIEZA", goat)}
{wimg}
{sec("WAHL · CON RECORTADORA DE REGALO (VALOR $500)", wahl)}
{sec("MÁS PROMOS", otras)}
<tr><td align="center" style="padding:28px 28px 8px">{btn}</td></tr>
<tr><td style="padding:16px 28px 26px;font:11px/1.5 Arial,sans-serif;color:#888">Precio tachado: en Ediciones, la suma de las piezas por separado; en Wahl, el precio normal más $500 de la recortadora; en el resto, el precio normal. Regalos hasta agotar existencias. Precios válidos en soybarber.com y sucursales Soy Barber.</td></tr>
</table></td></tr></table></body></html>'''
print(html)
