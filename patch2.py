import sys,re
PIX='saladadefrutasbraganca@gmail.com'
MAP='https://www.google.com/maps/search/?api=1&amp;query=Rua+Senador+Alencar+909+Centro+Fortaleza'
def patch(s):
    def rep(a,b):
        nonlocal s
        assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
    # 1) tira Pix/endereço da tela inicial: aparecem só depois de enviar o pedido
    n=len(s); s=re.sub(r'<div class="pay">.*?</div></div>\n  (<div id="menu">)',r'\1',s,count=1,flags=re.S); assert len(s)<n
    # 2) texto do carrinho sem Pix/endereço
    i=s.index('Sua salada é montada na hora e fica pronta para retirada 20 minutos depois do pedido. Retirada na loja:')
    j=s.index('</div>',i)
    s=s[:i]+'Sua salada é montada na hora e fica pronta para retirada 20 minutos depois do pedido. Depois de enviar, mostramos a chave Pix e o endereço de retirada.'+s[j:]
    # 3) tela de pedido enviado
    rep('<div id="cartSheet" class="ov" hidden>',
'''<div id="doneSheet" class="ov" hidden><div class="sheet">
  <h3>Pedido enviado!</h3>
  <p class="ad">Falta só pagar e retirar. Siga os passos:</p>
  <div class="pr"><span class="pl">1 · Pague pelo Pix</span><b>Chave e-mail:<br><span class="pk">%s</span></b><button type="button" class="pa cpx" id="dpix">Copiar chave Pix</button><small class="pn">Prefere link de pagamento? Peça pelo WhatsApp que enviamos o link. Depois de pagar, mande o comprovante.</small></div>
  <div class="pr" style="margin-top:10px"><span class="pl">2 · Retire na loja em 20 minutos</span><b>Rua Senador Alencar, 909 · Centro, Fortaleza</b><a class="pa" id="dmap" href="%s" target="_blank" rel="noopener">Abrir no Google Maps</a> <button type="button" class="pa" id="dcopa">Copiar endereço</button></div>
  <button type="button" class="cta green" id="dclose" style="margin-top:14px;width:100%%">Fechar</button>
</div></div>
<div id="cartSheet" class="ov" hidden>'''%(PIX,MAP))
    rep("  $('sendO').addEventListener('click',function(e){if($('sendO').getAttribute('aria-disabled')==='true'){",
        "  $('dclose').onclick=function(){$('doneSheet').hidden=true};\n  $('dcopa').onclick=function(){var b=this,k='Rua Senador Alencar, 909 - Centro, Fortaleza',o=b.textContent,ok=function(){b.textContent='Endereço copiado!';setTimeout(function(){b.textContent=o},1800)};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(k).then(ok,fb)}else fb();function fb(){var t=document.createElement('textarea');t.value=k;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{document.execCommand('copy')}catch(x){}document.body.removeChild(t);ok()}};\n  $('sendO').addEventListener('click',function(e){if($('sendO').getAttribute('aria-disabled')!=='true'){setTimeout(function(){$('cartSheet').hidden=true;$('doneSheet').hidden=false},900)}if($('sendO').getAttribute('aria-disabled')==='true'){")
    return s
if __name__=='__main__':
    for f in sys.argv[1:]:
        t=open(f,encoding='utf-8').read(); open(f,'w',encoding='utf-8').write(patch(t)); print('ok',f)
