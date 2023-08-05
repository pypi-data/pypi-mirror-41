# bitcoinhisyprice




use case :


from bitcoinhisyprice.core import CoinMarketCap
    cap=CoinMarketCap()
    pricetable=cap.coin_price(start=20180101,end=20181231)
    fp = open("path_to_save_data", 'w')
    json.dump(pricetable, fp)
    fp.close()
