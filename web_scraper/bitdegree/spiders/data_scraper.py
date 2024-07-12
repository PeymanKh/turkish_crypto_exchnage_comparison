import scrapy


class DataScraperSpider(scrapy.Spider):
    name = "data_scraper"
    allowed_domains = ["bitdegree.org"]
    start_urls = ["https://www.bitdegree.org/top-crypto-exchanges/btcturk-pro"]

    # BtcTurk statistics
    def parse(self, response):
        btcturk_statics = response.css('div.overall-stats span.stats-value::text').getall()
        btcturk_data = {
            'btcturk_volume': str(btcturk_statics[0]).split(),
            'btcturk_volume_in_btc': str(btcturk_statics[1]).split(),
            'btcturk_total_cryptocurrencies': str(btcturk_statics[2]).split(),
            'btcturk_markets_raw': str(response.css('div.overall-stats span.stats-value::text')[3].get()).split(),
            'btcturk_market_dominance': str(btcturk_statics[-2]).split(),
            'btcturk_market_rank': str(btcturk_statics[-1]).split(),
            'markets': []  # Initialize an empty list to store results
        }

        btcturk_assets_page1 = 'https://www.bitdegree.org/top-crypto-exchanges/btcturk-pro/markets?page=1#all-markets'
        yield response.follow(btcturk_assets_page1, callback=self.parse_btcturk_asset1,
                              meta={'btcturk_data': btcturk_data})

    def parse_btcturk_asset1(self, response):
        btcturk_data = response.meta['btcturk_data']
        btcturk_markets = []
        table_btcturk = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_btcturk:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            btcturk_markets.append(market_data)

        btcturk_data['markets'].extend(btcturk_markets)

        btcturk_assets_page2 = 'https://www.bitdegree.org/top-crypto-exchanges/btcturk-pro/markets?page=2#all-markets'
        yield response.follow(btcturk_assets_page2, callback=self.parse_btcturk_asset2,
                              meta={'btcturk_data': btcturk_data})

    def parse_btcturk_asset2(self, response):
        btcturk_data = response.meta['btcturk_data']
        btcturk_markets = []
        table_btcturk = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_btcturk:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            btcturk_markets.append(market_data)

        btcturk_data['markets'].extend(btcturk_markets)

        btcturk_assets_page3 = 'https://www.bitdegree.org/top-crypto-exchanges/btcturk-pro/markets?page=3#all-markets'
        yield response.follow(btcturk_assets_page3, callback=self.parse_btcturk_asset3,
                              meta={'btcturk_data': btcturk_data})

    def parse_btcturk_asset3(self, response):
        btcturk_data = response.meta['btcturk_data']
        btcturk_markets = []
        table_btcturk = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_btcturk:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            btcturk_markets.append(market_data)

        btcturk_data['markets'].extend(btcturk_markets)

        btcturk_assets_page4 = 'https://www.bitdegree.org/top-crypto-exchanges/btcturk-pro/markets?page=4#all-markets'
        yield response.follow(btcturk_assets_page4, callback=self.parse_btcturk_asset4,
                              meta={'btcturk_data': btcturk_data})

    def parse_btcturk_asset4(self, response):
        btcturk_data = response.meta['btcturk_data']
        btcturk_markets = []
        table_btcturk = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_btcturk:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            btcturk_markets.append(market_data)

        btcturk_data['markets'].extend(btcturk_markets)

        btcturk_assets_page5 = 'https://www.bitdegree.org/top-crypto-exchanges/btcturk-pro/markets?page=5#all-markets'
        yield response.follow(btcturk_assets_page5, callback=self.parse_btcturk_asset5,
                              meta={'btcturk_data': btcturk_data})


    def parse_btcturk_asset5(self, response):
        btcturk_data = response.meta['btcturk_data']

        btcturk_markets = []
        table_btcturk = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_btcturk:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            btcturk_markets.append(market_data)

        btcturk_data['markets'].extend(btcturk_markets)

        binance_url = 'https://www.bitdegree.org/top-crypto-exchanges/binance-tr'
        yield response.follow(binance_url, callback=self.parse_binance,
                              meta={'btcturk_data': btcturk_data})

        yield {'btcturk': btcturk_data}


    def parse_binance(self, response):
        btcturk_data = response.meta['btcturk_data']

        binance_statics = response.css('div.overall-stats span.stats-value::text').getall()

        binance_data = {
            'binance_volume': str(binance_statics[0]).split(),
            'binance_volume_in_btc': str(binance_statics[1]).split(),
            'binance_total_cryptocurrencies': str(binance_statics[2]).split(),
            'binance_markets': str(binance_statics[3]).split(),
            'binance_market_dominance': str(binance_statics[-2]).split(),
            'binance_market_rank': str(binance_statics[-1]).split(),
            'markets': []
        }

        binance_assets_page1 = 'https://www.bitdegree.org/top-crypto-exchanges/binance-tr/markets?page=1#all-markets'
        yield response.follow(binance_assets_page1, callback=self.parse_binance_asset1,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data})

    def parse_binance_asset1(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']


        binance_markets = []
        table_binance = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_binance:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            binance_markets.append(market_data)

        binance_data['markets'].extend(binance_markets)

        binance_assets_page2 = 'https://www.bitdegree.org/top-crypto-exchanges/binance-tr/markets?page=2#all-markets'
        yield response.follow(binance_assets_page2, callback=self.parse_binance_asset2,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data})

    def parse_binance_asset2(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']


        binance_markets = []
        table_binance = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_binance:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            binance_markets.append(market_data)

        binance_data['markets'].extend(binance_markets)

        btcturk_assets_page3 = 'https://www.bitdegree.org/top-crypto-exchanges/binance-tr/markets?page=3#all-markets'
        yield response.follow(btcturk_assets_page3, callback=self.parse_binance_asset3,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data})

    def parse_binance_asset3(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']


        binance_markets = []
        table_binance = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_binance:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            binance_markets.append(market_data)

        binance_data['markets'].extend(binance_markets)

        btcturk_assets_page4 = 'https://www.bitdegree.org/top-crypto-exchanges/binance-tr/markets?page=4#all-markets'
        yield response.follow(btcturk_assets_page4, callback=self.parse_binance_asset4,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data})

    def parse_binance_asset4(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']


        binance_markets = []
        table_binance = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_binance:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            binance_markets.append(market_data)

        binance_data['markets'].extend(binance_markets)

        paribu_url = 'https://www.bitdegree.org/top-crypto-exchanges/paribu'
        yield response.follow(paribu_url, callback=self.parse_paribu,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data})

        yield {'binance': binance_data}

    def parse_paribu(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']


        paribu_statics = response.css('div.overall-stats span.stats-value::text').getall()

        paribu_data = {
            'paribu_volume': str(paribu_statics[0]).split(),
            'paribu_volume_in_btc': str(paribu_statics[1]).split(),
            'paribu_total_cryptocurrencies': str(paribu_statics[2]).split(),
            'paribu_markets': str(paribu_statics[3]).split(),
            'paribu_market_dominance': str(paribu_statics[-2]).split(),
            'paribu_market_rank': str(paribu_statics[-1]).split(),
            'markets': []
        }

        paribu_assets_page1 = 'https://www.bitdegree.org/top-crypto-exchanges/paribu/markets?page=1#all-markets'
        yield response.follow(paribu_assets_page1, callback=self.parse_paribu_asset1,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data, 'paribu_data': paribu_data})

    def parse_paribu_asset1(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']
        paribu_data = response.meta['paribu_data']



        paribu_markets = []
        table_paribu = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_paribu:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            paribu_markets.append(market_data)

        paribu_data['markets'].extend(paribu_markets)

        paribu_assets_page2 = 'https://www.bitdegree.org/top-crypto-exchanges/paribu/markets?page=2#all-markets'
        yield response.follow(paribu_assets_page2, callback=self.parse_paribu_asset2,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data, 'paribu_data': paribu_data})


    def parse_paribu_asset2(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']
        paribu_data = response.meta['paribu_data']



        paribu_markets = []
        table_paribu = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_paribu:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            paribu_markets.append(market_data)

        paribu_data['markets'].extend(paribu_markets)

        paribu_assets_page3 = 'https://www.bitdegree.org/top-crypto-exchanges/paribu/markets?page=3#all-markets'
        yield response.follow(paribu_assets_page3, callback=self.parse_paribu_asset3,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data, 'paribu_data': paribu_data})


    def parse_paribu_asset3(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']
        paribu_data = response.meta['paribu_data']



        paribu_markets = []
        table_paribu = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_paribu:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            paribu_markets.append(market_data)

        paribu_data['markets'].extend(paribu_markets)

        paribu_assets_page4 = 'https://www.bitdegree.org/top-crypto-exchanges/paribu/markets?page=4#all-markets'
        yield response.follow(paribu_assets_page4, callback=self.parse_paribu_asset4,
                              meta={'binance_data': binance_data, 'btcturk_data': btcturk_data, 'paribu_data': paribu_data})


    def parse_paribu_asset4(self, response):
        btcturk_data = response.meta['btcturk_data']
        binance_data = response.meta['binance_data']
        paribu_data = response.meta['paribu_data']

        paribu_markets = []
        table_paribu = response.css('div.exchange-currencies-table div.table-wrp table.table tbody tr')
        for row in table_paribu:
            market_data = {
                'Base Coin': str(row.css('td:nth-child(2) div.mr-1::text').get()).split(),
                'Name': row.css('td:nth-child(4) strong::text').get(),
                'Volume': row.css('td:nth-child(6) span::text').get(),
                'Volume %': str(row.css('td:nth-child(7)::text').get()).split(),
            }
            paribu_markets.append(market_data)

        paribu_data['markets'].extend(paribu_markets)

        yield {'Paribu': paribu_data}
