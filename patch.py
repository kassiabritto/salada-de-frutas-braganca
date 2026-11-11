import sys
PIX='saladadefrutasbraganca@gmail.com'
ADDR='Rua Senador Alencar, 909 · Centro, Fortaleza'
MAP='https://www.google.com/maps/search/?api=1&amp;query=Rua+Senador+Alencar+909+Centro+Fortaleza'
def patch(s):
    def rep(a,b):
        nonlocal s
        assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
    rep('<div id="menu"></div>\n  <a class="back"',
'<div class="pay"><div class="pr"><span class="pl">Retirada na loja</span><b>%s</b><a class="pa" href="%s" target="_blank" rel="noopener">Abrir no mapa</a></div><div class="pr"><span class="pl">Pagamento: Pix ou link</span><b>Pix, chave e-mail: <span class="pk">%s</span></b><small class="pn">Prefere pagar por link de pagamento? Peça pelo WhatsApp que enviamos o link.</small><button type="button" class="pa cpx">Copiar chave Pix</button></div></div>\n  <div id="menu"></div>\n  <a class="back"'%(ADDR,MAP,PIX))
    rep('<b>Valor dos itens, sem retirada nem entrega.</b> O endereço de retirada e o pagamento são combinados pelo WhatsApp.</div>',
'<b>Valor dos itens, sem retirada nem entrega.</b> Sua salada é montada na hora e fica pronta para retirada 20 minutos depois do pedido. Retirada na loja: %s. Pagamento por Pix, chave e-mail <span class="pk">%s</span>, ou por link de pagamento (peça pelo WhatsApp). Depois de pagar, mande o comprovante pelo WhatsApp.<br><button type="button" class="pa cpx" style="margin-top:8px">Copiar chave Pix</button></div>'%(ADDR,PIX))
    rep("      m+='Dia e horário desejados: '+brd($('fd').value)+' às '+$('fh').value+'\\n';\n",
        "      m+='Retirada: 20 minutos depois do pedido (salada montada na hora)\\n';\n")
    rep("      if($('fo').value.trim())m+='Obs: '+$('fo').value.trim()+'\\n';\n      btn.href='https://wa.me/'+NUM+'?text='+encodeURIComponent(m);",
        "      if($('fo').value.trim())m+='Obs: '+$('fo').value.trim()+'\\n';\n      m+='\\nRetirada em: Rua Senador Alencar, 909 - Centro, Fortaleza\\nPagamento: Pix (chave e-mail %s) ou link de pagamento - me envie o link se preferir.';\n      btn.href='https://wa.me/'+NUM+'?text='+encodeURIComponent(m);"%PIX)
    rep("  // aberto agora\n",
"""  document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.cpx');if(!b)return;var k='%s',done=function(){var o=b.textContent;b.textContent='Chave copiada!';setTimeout(function(){b.textContent=o},1800)};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(k).then(done,function(){fb()})}else fb();
    function fb(){var t=document.createElement('textarea');t.value=k;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{document.execCommand('copy')}catch(x){}document.body.removeChild(t);done()}});
  // aberto agora
"""%PIX)
    rep('.note{background:var(--creme)',
""".pay{display:grid;gap:10px;margin:14px 0 0}
.pr{background:#fff;border-radius:16px;padding:14px;box-shadow:0 0 0 2px var(--polpa);font:600 14px/1.45 Nunito}
.pr .pl{display:block;font:800 12px Poppins;color:var(--morango);text-transform:uppercase;letter-spacing:.04em;margin-bottom:4px}
.pr b{display:block;font-weight:800}
.pk{word-break:break-all;color:var(--kiwi)}
.pn{display:block;margin-top:6px;font:600 12.5px/1.4 Nunito;color:#5a4a3a}
.pa{display:inline-block;margin-top:8px;background:var(--creme);color:var(--kiwi);border:2px solid var(--kiwi);border-radius:999px;padding:8px 14px;font:800 13px Nunito;text-decoration:none;cursor:pointer}
.vd .two,.vd .hh{display:none!important}
.note{background:var(--creme)""")
    rep("else if(ok&&!$('fd').value){err='Escolha o dia da retirada.';ok=false}",
        "else if(ok&&!(function(){var n=now();return n.min>=H0&&n.min<=H1-20})()){err='Pedidos das 13h às 18h40 (a retirada fica pronta 20 min depois). Volte nesse horário!';ok=false}")
    rep("$('openb').textContent=o?'Aberto agora':'Fechado agora · você pode agendar a retirada'",
        "o=n.min>=H0&&n.min<=H1-20;$('openb').textContent=o?'Aberto agora · pronto em 20 min':'Fechado agora · pedidos das 13h às 18h40'")
    rep('<p>Retirada na loja · pedidos das 13h às 19h</p>','<p>Retirada na loja · pedidos das 13h às 18h40 · pronto em 20 minutos</p>')
    rep('escolha seus itens, informe quando quer retirar e envie o pedido para o nosso WhatsApp.',
        'escolha seus itens e envie o pedido para o nosso WhatsApp. A salada é montada na hora e fica pronta para retirada 20 minutos depois do pedido.')
    return s
if __name__=='__main__':
    for f in sys.argv[1:]:
        t=open(f,encoding='utf-8').read(); open(f,'w',encoding='utf-8').write(patch(t)); print('ok',f)
