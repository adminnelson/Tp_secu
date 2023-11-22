message="guv6Jv6Jz!J6rp5r7Jzr66ntrM"
symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?*'

for key in range(len(symbols)):
    
    translated=''
    
    for symbol in message:
        for symbol in symbols:
            symbolindex=symbols.find(symbol)
            translatedindex=symbolindex-key
            
            if translatedindex<0:
                translatedindex=translatedindex+len(symbols)
                
                translated=translated+symbols[translatedindex]
            else:
                translated=translated+symbol
        print('key #%s: %s' % (key, translated))