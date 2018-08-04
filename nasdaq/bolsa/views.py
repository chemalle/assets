from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Bovespa
import bovespa
from django.core.files.storage import FileSystemStorage
import pandas as pd
from stockstats import StockDataFrame
from .forms import bovespaFORM
import numpy as np
from decimal import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'bolsa/home.html')



def bovespa_upload(request):
    if request.method == 'POST' and request.FILES['tnt']:
        myfile = request.FILES['tnt']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        bf = bovespa.File(filename)

        MYPK = []
        FIBR = []
        EMBR = []
        MOVI = []
        CVCB = []
        MGLU = []
        VLID = []
        BBSE = []
        CMIG = []
        ENBR = []
        UGPA = []
        EGIE = []
        DAGB = []
        BBAS = []
        CCRO = []
        NATU = []
        VULC = []
        ALSC = []
        MDIA = []
        BRSR = []
        BRFS = []
        RENT = []
        PETR = []
        SMLS = []
        BRKM = []
        FLRY = []
        USIM = []
        LAME = []
        SHOW = []
        VALE = []
        RAPT = []
        CIEL = []
        KROT = []
        RAIL = []
        RADL = []
        HYPE = []
        VVAR = []
        BTOW = []
        LCAM = []
        TGMA = []
        HGTX = []
        QUAL = []
        ATOM = []
        AZUL = []
        GOLL = []
        CAML = []
        PCAR = []
        CRFB = []
        ALPA = []
        ECOR = []
        GFSA = []
        AMAR = []
        WEGE = []
        LREN = []
        GGBR = []
        CSAN = []
        IRBR = []
        ABEV = []
        ITUB = []
        ENGI = []
        KNRI = []
        MULT = []
        TEND = []
        TIMP = []
        VIVT = []
        BBDC = []
        TRPL = []
        CSMG = []
        BRML = []
        MRFG = []
        B3SA = []
        PSSA = []
        SUZB = []
        BRDT = []
        CSNA = []
        GOAU = []
        SANB = []
        SLCE = []
        UNIP = []
        GUAR = []

        try:

            for rec in bf.query(stock='MYPK3'):
                mypk = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                MYPK.append(mypk)

            for rec in bf.query(stock='FIBR3'):
                fibr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                FIBR.append(fibr)

            for rec in bf.query(stock='EMBR3'):
                embr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                EMBR.append(embr)

            for rec in bf.query(stock='MOVI3'):
                movi = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                MOVI.append(movi)

            for rec in bf.query(stock='MGLU3'):
                mglu = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                MGLU.append(mglu)

            for rec in bf.query(stock='CVCB3'):
                cvcb = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CVCB.append(cvcb)

            for rec in bf.query(stock='VLID3'):
                vlid = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                VLID.append(vlid)

            for rec in bf.query(stock='BBSE3'):
                bbse = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BBSE.append(bbse)

            for rec in bf.query(stock='CMIG4'):
                cmig = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CMIG.append(cmig)

            for rec in bf.query(stock='ENBR3'):
                enbr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ENBR.append(enbr)

            for rec in bf.query(stock='UGPA3'):
                ugpa = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                UGPA.append(ugpa)

            for rec in bf.query(stock='EGIE3'):
                egie = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                EGIE.append(egie)

            for rec in bf.query(stock='DAGB33'):
                dagb = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                DAGB.append(dagb)

            for rec in bf.query(stock='BBAS3'):
                bbas = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BBAS.append(bbas)

            for rec in bf.query(stock='CCRO3'):
                ccro = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CCRO.append(ccro)

            for rec in bf.query(stock='NATU3'):
                natu = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                NATU.append(natu)


            for rec in bf.query(stock='VULC3'):
                vulc = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                VULC.append(vulc)

            for rec in bf.query(stock='ALSC3'):
                alsc = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ALSC.append(alsc)

            for rec in bf.query(stock='MDIA3'):
                mdia = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                MDIA.append(mdia)

            for rec in bf.query(stock='BRSR6'):
                brsr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BRSR.append(brsr)

            for rec in bf.query(stock='BRFS3'):
                brfs = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BRFS.append(brfs)


            for rec in bf.query(stock='RENT3'):
                rent = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                RENT.append(rent)

            for rec in bf.query(stock='PETR4'):
                petr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                PETR.append(petr)

            for rec in bf.query(stock='SMLS3'):
                smls = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                SMLS.append(smls)

            for rec in bf.query(stock='BRKM5'):
                brkm = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BRKM.append(brkm)

            for rec in bf.query(stock='FLRY3'):
                flry = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                FLRY.append(flry)

            for rec in bf.query(stock='USIM5'):
                usim = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                USIM.append(usim)

            for rec in bf.query(stock='LAME4'):
                lame = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                LAME.append(lame)


            for rec in bf.query(stock='SHOW3'):
                show = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                SHOW.append(show)

            for rec in bf.query(stock='VALE3'):
                vale = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                VALE.append(vale)

            for rec in bf.query(stock='RAPT4'):
                rapt = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                RAPT.append(rapt)


            for rec in bf.query(stock='CIEL3'):
                ciel = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CIEL.append(ciel)

            for rec in bf.query(stock='KROT3'):
                krot = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                KROT.append(krot)

            for rec in bf.query(stock='RAIL3'):
                rail = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                RAIL.append(rail)

            for rec in bf.query(stock='RADL3'):
                radl = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                RADL.append(radl)

            for rec in bf.query(stock='HYPE3'):
                hype = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                HYPE.append(hype)

            for rec in bf.query(stock='VVAR11'):
                vvar = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                VVAR.append(vvar)

            for rec in bf.query(stock='BTOW3'):
                btow = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BTOW.append(btow)

            for rec in bf.query(stock='LCAM3'):
                lcam = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                LCAM.append(lcam)

            for rec in bf.query(stock='TGMA3'):
                tgma = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                TGMA.append(tgma)

            for rec in bf.query(stock='HGTX3'):
                hgtx = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                HGTX.append(hgtx)

            for rec in bf.query(stock='QUAL3'):
                qual = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                QUAL.append(qual)

            for rec in bf.query(stock='ATOM3'):
                atom = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ATOM.append(atom)

            for rec in bf.query(stock='AZUL4'):
                azul = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                AZUL.append(azul)

            for rec in bf.query(stock='GOLL4'):
                goll = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                GOLL.append(goll)

            for rec in bf.query(stock='CAML3'):
                caml = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CAML.append(caml)

            for rec in bf.query(stock='PCAR4'):
                pcar = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                PCAR.append(pcar)

            for rec in bf.query(stock='CRFB3'):
                crfb = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CRFB.append(crfb)

            for rec in bf.query(stock='ALPA4'):
                alpa = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ALPA.append(alpa)

            for rec in bf.query(stock='ECOR3'):
                ecor = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ECOR.append(ecor)

            for rec in bf.query(stock='GFSA3'):
                gfsa = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                GFSA.append(gfsa)

            for rec in bf.query(stock='AMAR3'):
                amar = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                AMAR.append(amar)

            for rec in bf.query(stock='WEGE3'):
                wege = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                WEGE.append(wege)

            for rec in bf.query(stock='LREN3'):
                lren = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                LREN.append(lren)

            for rec in bf.query(stock='GGBR4'):
                ggbr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                GGBR.append(ggbr)

            for rec in bf.query(stock='CSAN3'):
                csan = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CSAN.append(csan)

            for rec in bf.query(stock='IRBR3'):
                irbr = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                IRBR.append(irbr)

            for rec in bf.query(stock='ABEV3'):
                abev = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ABEV.append(abev)

            for rec in bf.query(stock='ITUB4'):
                itub = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ITUB.append(itub)


            for rec in bf.query(stock='KNRI11'):
                knri = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                KNRI.append(knri)

            for rec in bf.query(stock='ENGI11'):
                engi = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                ENGI.append(engi)


            for rec in bf.query(stock='MULT3'):
                mult = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                MULT.append(mult)

            for rec in bf.query(stock='TEND3'):
                tend = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                TEND.append(tend)


            for rec in bf.query(stock='TIMP3'):
                timp = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                TIMP.append(timp)


            for rec in bf.query(stock='VIVT4'):
                vivt = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                VIVT.append(vivt)

            for rec in bf.query(stock='BBDC4'):
                bbdc = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BBDC.append(bbdc)

            for rec in bf.query(stock='TRPL4'):
                trpl = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                TRPL.append(trpl)

            for rec in bf.query(stock='CSMG3'):
                csmg = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CSMG.append(csmg)

            for rec in bf.query(stock='BRML3'):
                brml = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BRML.append(brml)

            for rec in bf.query(stock='MRFG3'):
                mrfg = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                MRFG.append(mrfg)

            for rec in bf.query(stock='B3SA3'):
                b3sa = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                B3SA.append(b3sa)


            for rec in bf.query(stock='PSSA3'):
                pssa = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                PSSA.append(pssa)

            for rec in bf.query(stock='SUZB3'):
                suzb = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                SUZB.append(suzb)

            for rec in bf.query(stock='BRDT3'):
                brdt = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                BRDT.append(brdt)


            for rec in bf.query(stock='CSNA3'):
                csna = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                CSNA.append(csna)


            for rec in bf.query(stock='GOAU4'):
                goau = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                GOAU.append(goau)

            for rec in bf.query(stock='SANB11'):
                sanb = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                SANB.append(sanb)

            for rec in bf.query(stock='SLCE3'):
                slce = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                SLCE.append(slce)

            for rec in bf.query(stock='UNIP6'):
                unip = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                UNIP.append(unip)

            for rec in bf.query(stock='GUAR3'):
                guar = (rec.stock_code,rec.date, rec.price_open, rec.price_high,rec.price_low,rec.price_close,rec.volume)
                GUAR.append(guar)


                df_MYPK = pd.DataFrame(MYPK)
                df_FIBR = pd.DataFrame(FIBR)
                df_EMBR = pd.DataFrame(EMBR)
                df_MOVI = pd.DataFrame(MOVI)
                df_MGLU = pd.DataFrame(MGLU)
                df_CVCB = pd.DataFrame(CVCB)
                df_VLID = pd.DataFrame(VLID)
                df_BBSE = pd.DataFrame(BBSE)
                df_CMIG = pd.DataFrame(CMIG)
                df_ENBR = pd.DataFrame(ENBR)
                df_UGPA = pd.DataFrame(UGPA)
                df_EGIE = pd.DataFrame(EGIE)
                df_DAGB = pd.DataFrame(DAGB)
                df_BBAS = pd.DataFrame(BBAS)
                df_CCRO = pd.DataFrame(CCRO)
                df_NATU = pd.DataFrame(NATU)

                df_VULC = pd.DataFrame(VULC)
                df_ALSC = pd.DataFrame(ALSC)
                df_MDIA = pd.DataFrame(MDIA)
                df_BRSR = pd.DataFrame(BRSR)
                df_BRFS = pd.DataFrame(BRFS)

                df_RENT = pd.DataFrame(RENT)
                df_PETR = pd.DataFrame(PETR)
                df_SMLS = pd.DataFrame(SMLS)
                df_BRKM = pd.DataFrame(BRKM)
                df_FLRY = pd.DataFrame(FLRY)
                df_USIM = pd.DataFrame(USIM)
                df_LAME = pd.DataFrame(LAME)
                df_SHOW = pd.DataFrame(SHOW)
                df_VALE = pd.DataFrame(VALE)

                df_RAPT = pd.DataFrame(RAPT)

                df_CIEL = pd.DataFrame(CIEL)
                df_KROT = pd.DataFrame(KROT)
                df_RAIL = pd.DataFrame(RAIL)

                df_RADL = pd.DataFrame(RADL)
                df_HYPE = pd.DataFrame(HYPE)

                df_VVAR = pd.DataFrame(VVAR)
                df_BTOW = pd.DataFrame(BTOW)

                df_LCAM = pd.DataFrame(LCAM)

                df_TGMA = pd.DataFrame(TGMA)
                df_HGTX = pd.DataFrame(HGTX)
                df_QUAL = pd.DataFrame(QUAL)

                df_ATOM = pd.DataFrame(ATOM)

                df_AZUL = pd.DataFrame(AZUL)
                df_GOLL = pd.DataFrame(GOLL)
                df_CAML = pd.DataFrame(CAML)
                df_PCAR = pd.DataFrame(PCAR)
                df_CRFB = pd.DataFrame(CRFB)

                df_ALPA = pd.DataFrame(ALPA)
                df_ECOR = pd.DataFrame(ECOR)
                df_GFSA = pd.DataFrame(GFSA)

                df_AMAR = pd.DataFrame(AMAR)

                df_WEGE = pd.DataFrame(WEGE)

                df_LREN = pd.DataFrame(LREN)

                df_GGBR = pd.DataFrame(GGBR)

                df_CSAN = pd.DataFrame(CSAN)

                df_IRBR = pd.DataFrame(IRBR)

                df_ABEV = pd.DataFrame(ABEV)

                df_ITUB = pd.DataFrame(ITUB)

                df_KNRI = pd.DataFrame(KNRI)
                df_ENGI = pd.DataFrame(ENGI)
                df_MULT = pd.DataFrame(MULT)
                df_TEND = pd.DataFrame(TEND)

                df_TIMP = pd.DataFrame(TIMP)


                df_VIVT = pd.DataFrame(VIVT)
                df_BBDC = pd.DataFrame(BBDC)
                df_TRPL = pd.DataFrame(TRPL)
                df_CSMG = pd.DataFrame(CSMG)
                df_BRML = pd.DataFrame(BRML)

                df_MRFG = pd.DataFrame(MRFG)

                df_B3SA = pd.DataFrame(B3SA)

                df_PSSA = pd.DataFrame(PSSA)

                df_SUZB = pd.DataFrame(SUZB)

                df_BRDT = pd.DataFrame(BRDT)

                df_CSNA = pd.DataFrame(CSNA)

                df_GOAU = pd.DataFrame(GOAU)

                df_SANB = pd.DataFrame(SANB)

                df_SLCE = pd.DataFrame(SLCE)
                df_UNIP = pd.DataFrame(UNIP)
                df_GUAR = pd.DataFrame(GUAR)

                df_MYPK.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_FIBR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_EMBR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_MOVI.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_MGLU.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_CVCB.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                ##continuacao

                df_VLID.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BBSE.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_CMIG.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_ENBR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_UGPA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_EGIE.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_DAGB.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BBAS.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_CCRO.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_NATU.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_VULC.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_ALSC.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_MDIA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BRSR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BRFS.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_RENT.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_PETR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_SMLS.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BRKM.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_FLRY.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_USIM.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_LAME.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_SHOW.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_VALE.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_RAPT.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_CIEL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_KROT.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_RAIL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_RADL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_HYPE.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_VVAR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BTOW.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_LCAM.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_TGMA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_HGTX.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_QUAL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_ATOM.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_AZUL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_GOLL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_CAML.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_PCAR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_CRFB.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_ALPA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_ECOR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_GFSA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_AMAR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_WEGE.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_LREN.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_GGBR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_CSAN.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_IRBR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_ABEV.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_ITUB.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_KNRI.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_ENGI.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_MULT.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_TEND.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_TIMP.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']


                df_VIVT.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BBDC.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_TRPL.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_CSMG.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_BRML.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_MRFG.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_B3SA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_PSSA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_SUZB.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_BRDT.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_CSNA.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_GOAU.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_SANB.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_SLCE.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']
                df_UNIP.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']

                df_GUAR.columns = ['Ticker','Date', 'Open', 'High','Low','Close','Volume']


                df_MYPK['Date'] = df_MYPK['Date'].astype('datetime64[ns]')
                df_FIBR['Date'] = df_FIBR['Date'].astype('datetime64[ns]')
                df_EMBR['Date'] = df_EMBR['Date'].astype('datetime64[ns]')
                df_MOVI['Date'] = df_MOVI['Date'].astype('datetime64[ns]')
                df_MGLU['Date'] = df_MGLU['Date'].astype('datetime64[ns]')
                df_CVCB['Date'] = df_CVCB['Date'].astype('datetime64[ns]')
                df_VLID['Date'] = df_VLID['Date'].astype('datetime64[ns]')
                df_BBSE['Date'] = df_BBSE['Date'].astype('datetime64[ns]')
                df_CMIG['Date'] = df_CMIG['Date'].astype('datetime64[ns]')
                df_ENBR['Date'] = df_ENBR['Date'].astype('datetime64[ns]')
                df_UGPA['Date'] = df_UGPA['Date'].astype('datetime64[ns]')
                df_EGIE['Date'] = df_EGIE['Date'].astype('datetime64[ns]')
                df_DAGB['Date'] = df_DAGB['Date'].astype('datetime64[ns]')
                df_BBAS['Date'] = df_BBAS['Date'].astype('datetime64[ns]')
                df_CCRO['Date'] = df_CCRO['Date'].astype('datetime64[ns]')
                df_NATU['Date'] = df_NATU['Date'].astype('datetime64[ns]')

                df_VULC['Date'] = df_VULC['Date'].astype('datetime64[ns]')
                df_ALSC['Date'] = df_ALSC['Date'].astype('datetime64[ns]')
                df_MDIA['Date'] = df_MDIA['Date'].astype('datetime64[ns]')
                df_BRSR['Date'] = df_BRSR['Date'].astype('datetime64[ns]')
                df_BRFS['Date'] = df_BRFS['Date'].astype('datetime64[ns]')

                df_RENT['Date'] = df_RENT['Date'].astype('datetime64[ns]')
                df_PETR['Date'] = df_PETR['Date'].astype('datetime64[ns]')
                df_SMLS['Date'] = df_SMLS['Date'].astype('datetime64[ns]')
                df_BRKM['Date'] = df_BRKM['Date'].astype('datetime64[ns]')
                df_FLRY['Date'] = df_FLRY['Date'].astype('datetime64[ns]')
                df_USIM['Date'] = df_USIM['Date'].astype('datetime64[ns]')
                df_LAME['Date'] = df_LAME['Date'].astype('datetime64[ns]')
                df_SHOW['Date'] = df_SHOW['Date'].astype('datetime64[ns]')
                df_VALE['Date'] = df_VALE['Date'].astype('datetime64[ns]')

                df_RAPT['Date'] = df_RAPT['Date'].astype('datetime64[ns]')

                df_CIEL['Date'] = df_CIEL['Date'].astype('datetime64[ns]')
                df_KROT['Date'] = df_KROT['Date'].astype('datetime64[ns]')
                df_RAIL['Date'] = df_RAIL['Date'].astype('datetime64[ns]')

                df_RADL['Date'] = df_RADL['Date'].astype('datetime64[ns]')
                df_HYPE['Date'] = df_HYPE['Date'].astype('datetime64[ns]')

                df_VVAR['Date'] = df_VVAR['Date'].astype('datetime64[ns]')
                df_BTOW['Date'] = df_BTOW['Date'].astype('datetime64[ns]')

                df_LCAM['Date'] = df_LCAM['Date'].astype('datetime64[ns]')

                df_TGMA['Date'] = df_TGMA['Date'].astype('datetime64[ns]')
                df_HGTX['Date'] = df_HGTX['Date'].astype('datetime64[ns]')
                df_QUAL['Date'] = df_QUAL['Date'].astype('datetime64[ns]')

                df_ATOM['Date'] = df_ATOM['Date'].astype('datetime64[ns]')

                df_AZUL['Date'] = df_AZUL['Date'].astype('datetime64[ns]')
                df_GOLL['Date'] = df_GOLL['Date'].astype('datetime64[ns]')
                df_CAML['Date'] = df_CAML['Date'].astype('datetime64[ns]')
                df_PCAR['Date'] = df_PCAR['Date'].astype('datetime64[ns]')
                df_CRFB['Date'] = df_CRFB['Date'].astype('datetime64[ns]')

                df_ALPA['Date'] = df_ALPA['Date'].astype('datetime64[ns]')
                df_ECOR['Date'] = df_ECOR['Date'].astype('datetime64[ns]')
                df_GFSA['Date'] = df_GFSA['Date'].astype('datetime64[ns]')

                df_AMAR['Date'] = df_AMAR['Date'].astype('datetime64[ns]')

                df_WEGE['Date'] = df_WEGE['Date'].astype('datetime64[ns]')

                df_LREN['Date'] = df_LREN['Date'].astype('datetime64[ns]')

                df_GGBR['Date'] = df_GGBR['Date'].astype('datetime64[ns]')

                df_CSAN['Date'] = df_CSAN['Date'].astype('datetime64[ns]')

                df_IRBR['Date'] = df_IRBR['Date'].astype('datetime64[ns]')

                df_ABEV['Date'] = df_ABEV['Date'].astype('datetime64[ns]')

                df_ITUB['Date'] = df_ITUB['Date'].astype('datetime64[ns]')

                df_KNRI['Date'] = df_KNRI['Date'].astype('datetime64[ns]')
                df_ENGI['Date'] = df_ENGI['Date'].astype('datetime64[ns]')
                df_MULT['Date'] = df_MULT['Date'].astype('datetime64[ns]')
                df_TEND['Date'] = df_TEND['Date'].astype('datetime64[ns]')

                df_TIMP['Date'] = df_TIMP['Date'].astype('datetime64[ns]')


                df_VIVT['Date'] = df_VIVT['Date'].astype('datetime64[ns]')
                df_BBDC['Date'] = df_BBDC['Date'].astype('datetime64[ns]')
                df_TRPL['Date'] = df_TRPL['Date'].astype('datetime64[ns]')
                df_CSMG['Date'] = df_CSMG['Date'].astype('datetime64[ns]')
                df_BRML['Date'] = df_BRML['Date'].astype('datetime64[ns]')

                df_MRFG['Date'] = df_MRFG['Date'].astype('datetime64[ns]')

                df_B3SA['Date'] = df_B3SA['Date'].astype('datetime64[ns]')

                df_PSSA['Date'] = df_PSSA['Date'].astype('datetime64[ns]')

                df_SUZB['Date'] = df_SUZB['Date'].astype('datetime64[ns]')

                df_BRDT['Date'] = df_BRDT['Date'].astype('datetime64[ns]')

                df_CSNA['Date'] = df_CSNA['Date'].astype('datetime64[ns]')

                df_GOAU['Date'] = df_GOAU['Date'].astype('datetime64[ns]')
                df_SANB['Date'] = df_SANB['Date'].astype('datetime64[ns]')
                df_SLCE['Date'] = df_SLCE['Date'].astype('datetime64[ns]')

                df_UNIP['Date'] = df_UNIP['Date'].astype('datetime64[ns]')
                df_GUAR['Date'] = df_GUAR['Date'].astype('datetime64[ns]')

                mypk3 = pd.DataFrame(df_MYPK)
                fibr3 = pd.DataFrame(df_FIBR)
                embr3 = pd.DataFrame(df_EMBR)
                movi3 = pd.DataFrame(df_MOVI)
                mglu3 = pd.DataFrame(df_MGLU)
                cvcb3 = pd.DataFrame(df_CVCB)

                ## continuacao

                vlid3 = pd.DataFrame(df_VLID)
                bbse3 = pd.DataFrame(df_BBSE)
                cmig4 = pd.DataFrame(df_CMIG)
                enbr3 = pd.DataFrame(df_ENBR)
                ugpa3 = pd.DataFrame(df_UGPA)
                egie3 = pd.DataFrame(df_EGIE)
                dagb33 = pd.DataFrame(df_DAGB)
                bbas3 = pd.DataFrame(df_BBAS)
                ccro3 = pd.DataFrame(df_CCRO)
                natu3 = pd.DataFrame(df_NATU)

                vulc3 = pd.DataFrame(df_VULC)
                alsc3 = pd.DataFrame(df_ALSC)
                mdia3 = pd.DataFrame(df_MDIA)
                brsr6 = pd.DataFrame(df_BRSR)
                brfs3 = pd.DataFrame(df_BRFS)

                rent3 = pd.DataFrame(df_RENT)
                petr4 = pd.DataFrame(df_PETR)
                smls3 = pd.DataFrame(df_SMLS)
                brkm5 = pd.DataFrame(df_BRKM)
                flry3 = pd.DataFrame(df_FLRY)
                usim5 = pd.DataFrame(df_USIM)
                lame4 = pd.DataFrame(df_LAME)
                show3 = pd.DataFrame(df_SHOW)
                vale3 = pd.DataFrame(df_VALE)

                rapt4 = pd.DataFrame(df_RAPT)

                ciel3 = pd.DataFrame(df_CIEL)
                krot3 = pd.DataFrame(df_KROT)
                rail3 = pd.DataFrame(df_RAIL)

                radl3 = pd.DataFrame(df_RADL)
                hype3 = pd.DataFrame(df_HYPE)

                vvar11 = pd.DataFrame(df_VVAR)
                btow3 = pd.DataFrame(df_BTOW)

                lcam3 = pd.DataFrame(df_LCAM)

                tgma3 = pd.DataFrame(df_TGMA)
                hgtx3 = pd.DataFrame(df_HGTX)
                qual3 = pd.DataFrame(df_QUAL)

                atom3 = pd.DataFrame(df_ATOM)

                azul4 = pd.DataFrame(df_AZUL)
                goll4 = pd.DataFrame(df_GOLL)
                caml3 = pd.DataFrame(df_CAML)
                pcar4 = pd.DataFrame(df_PCAR)
                crfb3 = pd.DataFrame(df_CRFB)

                alpa4 = pd.DataFrame(df_ALPA)
                ecor3 = pd.DataFrame(df_ECOR)
                gfsa3 = pd.DataFrame(df_GFSA)

                amar3 = pd.DataFrame(df_AMAR)

                wege3 = pd.DataFrame(df_WEGE)

                lren3 = pd.DataFrame(df_LREN)

                ggbr4 = pd.DataFrame(df_GGBR)

                csan3 = pd.DataFrame(df_CSAN)

                irbr3 = pd.DataFrame(df_IRBR)

                abev3 = pd.DataFrame(df_ABEV)

                itub4 = pd.DataFrame(df_ITUB)

                knri11 = pd.DataFrame(df_KNRI)
                engi11 = pd.DataFrame(df_ENGI)
                mult3 = pd.DataFrame(df_MULT)
                tend3 = pd.DataFrame(df_TEND)

                timp3 = pd.DataFrame(df_TIMP)



                vivt4 = pd.DataFrame(df_VIVT)
                bbdc4 = pd.DataFrame(df_BBDC)
                trpl4 = pd.DataFrame(df_TRPL)
                csmg3 = pd.DataFrame(df_CSMG)
                brml3 = pd.DataFrame(df_BRML)

                mrfg3 = pd.DataFrame(df_MRFG)

                b3sa3 = pd.DataFrame(df_B3SA)

                pssa3 = pd.DataFrame(df_PSSA)

                suzb3 = pd.DataFrame(df_SUZB)


                brdt3 = pd.DataFrame(df_BRDT)
                csna3 = pd.DataFrame(df_CSNA)

                goau4 = pd.DataFrame(df_GOAU)
                sanb11 = pd.DataFrame(df_SANB)
                slce3 = pd.DataFrame(df_SLCE)
                unip6 = pd.DataFrame(df_UNIP)
                guar3 = pd.DataFrame(df_GUAR)

                barchart = [mypk3,fibr3,embr3,movi3,mglu3,cvcb3,vlid3,bbse3,cmig4,enbr3,ugpa3,
                            egie3,dagb33,bbas3,ccro3,natu3,vulc3,alsc3,mdia3,brsr6,brfs3,rent3,petr4,
                            smls3,brkm5,flry3,usim5,lame4,show3,vale3,rapt4,ciel3,krot3,rail3,radl3,
                            hype3,vvar11,btow3,lcam3,tgma3,hgtx3,qual3,atom3,azul4,goll4,caml3,pcar4,
                            crfb3,alpa4,ecor3,gfsa3,amar3,wege3,lren3,ggbr4,csan3,irbr3,abev3,itub4,
                            knri11,engi11,tend3,timp3,mult3,brml3,bbdc4,trpl4,csmg3,vivt4,b3sa3,mrfg3,
                            pssa3,suzb3,brdt3,csna3,goau4,sanb11,slce3,unip6, guar3]

                for item in barchart:
                    for index,row in item.iterrows():
                        try:
                            if row[0] != 'create_date':
                                bovespa2 = Bovespa()
                                bovespa2.Ticker = row[0]
                                bovespa2.Date = row[1]
                                bovespa2.Open = row[2]
                                bovespa2.High = row[3]
                                bovespa2.Low = row[4]
                                bovespa2.Close = row[5]
                                bovespa2.Volume = row[6]
                                bovespa2.save()
                        except Exception:
                            pass

        except Exception:
            pass

        return render_to_response('bolsa/thankyou.html')

    else:
        return render(request, 'bolsa/import.html')


def stock(request):
    if request.method == 'POST':
        form = bovespaFORM(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            return fibonacci(str(form).upper())

    else:
        form = bovespaFORM()


    return render(request, 'inquiry.html', context = {'df': form})


def fibonacci(symbol):
    df = pd.DataFrame(list(Bovespa.pdobjects.filter(Ticker=symbol).values()))[-21:]


    price = float(df['Close'].iloc[-1])
    price_min= float(df['Close'].min())
    price_max=float(df['Close'].max())
    diff = price_max - price_min
    level1 = price_max - 0.236 * diff
    level2 = price_max - 0.382 * diff
    level3 = price_max - 0.618 * diff
    level4 = price + 0.236 * diff
    level5 = price + 0.382 * diff
    level6 = price + 0.618 * diff
    weight = int(df['Volume'][-1:])
    weight_median=df['Volume'].median()
    stock2 = StockDataFrame.retype(df)
    stock2.reset_index()

    if weight > weight_median:
        w = 'Stock Alert'
    else:
        w = 'Stock traded at normal levels'




    if price > level3 and price < level2:
        action = [(df.ticker[-1],price,level2,level3, 'just buy at 1st level',price_max,"{0:.2%}".format((price_max/level2)-1),0,w,stock2['rsi_21'][-1])]
    elif price> level2 and price < level1:
        action = [(df.ticker[-1],price,level1, level2,'just buy at 1st level',price_max,"{0:.2%}".format((price_max/level1)-1),1,w,stock2['rsi_21'][-1])]
    elif price > level1 :
        action = [(df.ticker[-1],price,level4,price_max,'new highs on going',level6,"{0:.2%}".format((level6/price)-1),2,w,stock2['rsi_21'][-1])]
    else:
        action = [(df.ticker[-1],price,level2,level3,'XP strategy',price_max,"{0:.2%}".format((price_max/level3)-1),3,w,stock2['rsi_21'][-1])]


    barchart = pd.DataFrame(list(action))
    barchart.columns = [['ticker','price','1st level','2nd level','message','target','return','priority','volume_alert','rsi']]




    return render_to_response('bolsa/analise.html',{'action':barchart.to_html(index=False)})




def fibonacci2(form):
    df = pd.DataFrame(list(Bovespa.pdobjects.all().values()))[-21:]
    df = df.reset_index(drop=True)
    price = float(df['Close'][-1:])
    price_min= float(df['Close'].min())
    price_max=float(df['Close'].max())
    diff = price_max - price_min
    level1 = price_max - 0.236 * diff
    level2 = price_max - 0.382 * diff
    level3 = price_max - 0.618 * diff
    level4 = price + 0.236 * diff
    level5 = price + 0.382 * diff
    level6 = price + 0.618 * diff
    weight = int(df['Volume'][-1:])
    weight_median=df['Volume'].median()
    stock2 = StockDataFrame.retype(df)
    stock2.reset_index()
    #rsi = stock2['rsi_21']










    if weight > weight_median:
        w = 'Stock Alert'
    else:
        w = 'Stock traded at normal levels'



    if price > level3 and price < level2:
        action = (df.ticker[-1],price,level2,level3, 'just buy at 1st level',price_max,"{0:.2%}".format((price_max/level2)-1),0,w,stock2['rsi_21'][-1])
    elif price> level2 and price < level1:
        action = (df.ticker[-1],price,level1, level2,'just buy at 1st level',price_max,"{0:.2%}".format((price_max/level1)-1),1,w,stock2['rsi_21'][-1])
    elif price > level1 :
        action = (df.ticker[-1],price,level4,price_max,'new highs on going',level6,"{0:.2%}".format((level6/price)-1),2,w,stock2['rsi_21'][-1])
    else:
        action = (df.ticker[-1],price,level2,level3,'XP strategy',price_max,"{0:.2%}".format((price_max/level3)-1),3,w,stock2['rsi_21'][-1])


    barchart = pd.DataFrame(list(action))
    barchart.columns = [['ticker','price','1st level','2nd level','message','target','return','priority','volume_alert','rsi']]

    #barchart = pd.DataFrame(list(action)).T
    #barchart.columns = ['ticker','price','1st level','2nd level','message']



    return render_to_response('bolsa/analise.html',{'action':barchart.to_html(index=False)})




# def csv(request):
#     df = pd.DataFrame(list(Bovespa.pdobjects.all().values()))
#     csv = df.to_xlsx('bovespa.xlsx', index=False)

def excel_download(request):
    qs = Bovespa.pdobjects.all()
    df2 = qs.to_dataframe()
    df2 =df2.sort_values(by=['Ticker', 'Date'])
    fsock = df2.to_excel('bolsa/documents/bovespa.xlsx',engine='openpyxl', index=False)
    fsock = open('bolsa/documents/bovespa.xlsx', 'rb')
    response = HttpResponse(fsock, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="bovespa.xls"'
    return response




def showthis(request):

    #deletes all objects from Car database table
    Bovespa.objects.all().delete()

    context= {}

    return render(request, 'bolsa/base.html', context)
