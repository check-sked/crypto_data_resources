import requests
import openpyxl

# Set API key and parameters
api_key = "0da13dd9-4db8-45a5-a885-39431d8e3234"
params = {
    "symbol": "1inch,aave,ada,akro,algo,alpha,ampl,ant,ape,api3,arpa,arv,atom,audio,avax,awg,aws,awx,ax,axs,bal,band,bat,bch,bcha,bel,bnb,bnt,boba,bond,bsv,btc,btg,btt,bttc,busd,cake,chr,chz,comp,conv,coti,cream,cro,crv,cvc,dai,dash,dgb,dnt,doge,dot,dydx,edgt,egld,enj,eos,etc,eth,ethw,eur,euroc,eurs,ever,farm,fil,flow,ftm,fun,gala,gas,gbp,ghst,glm,gno,grt,gusd,gzil,hapi,hegic,hot,ht,icp,idex,inj,jasmy,jst,kava,keep,knc,kp3r,ksm,lamb,ldo,leo,lever,link,lqty,lrc,ltc,luna,luna2,lunc,lunr,mana,matic,merc,mhc,mina,miota,mkr,mpl,mta,musd,neo,nexo,nft,nmr,nu,ocean,ogn,omg,ong,ont,op,oxt,pax,paxg,pickle,pln,pols,qash,qnt,qrdo,rari,ren,renbtc,rep,repv2,req,roobee,rsr,rub,rvn,sand,sgb,shib,snx,sol,srm,storj,strk,sure,sushi,sxp,theta,tlm,ton,trb,trx,tusd,twt,txag,txau,uma,uni,usd,usdc,usdt,utk,value,vet,wabi,waves,wbtc,win,wnxm,xdc,xec,xlm,xrp,xsgd,xtz,xvs,yfi,yfii,zap,zec,zil,zrx,zwap",
    "convert": "USD"
}

# Set base URL for API endpoint
base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

# Make API request and get response
response = requests.get(base_url, params=params, headers={"X-CMC_PRO_API_KEY": api_key})
data = response.json()

# Parse response data and extract relevant information
prices = []
for currency, info in data["data"].items():
    name = info["name"]
    symbol = info["symbol"]
    price = info["quote"]["USD"]["price"]
    prices.append([name, symbol, price])

# Create a new Excel workbook and add a sheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write data to the sheet
worksheet.append(["Name", "Symbol", "Price"])
for price in prices:
    worksheet.append(price)

# Save the Excel file
workbook.save("coinmarketcap_prices_current.xlsx")