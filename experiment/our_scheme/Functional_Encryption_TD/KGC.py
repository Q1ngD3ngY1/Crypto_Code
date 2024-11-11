import gmpy2 as gy
import math
import pickle
import System_Params
import time
import sys









'''-----------------------------------数据参数部分-----------------------------------'''
N = System_Params.N

U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 25

#用户的公私钥
public_key = System_Params.public_key
private_key = System_Params.private_key

#用户权值
weight = [1,2,3,4,5]
weight_sum = 15

#扰动
alpha = [[22410642974084585442191727643918586647230232556525075962101709016346283694569, 
           68574235962049804543682472313140990616965871425187131346222779247232111250905, 
           43139019699327115711617780202783040092862808628341895782744823069479854552953, 
           107077420960787047367844643446953157544199051322244644306625049394723563232185, 
           16523082419060126492750584071126670442347370916635012443244906593568651899054,
           
           110438586017209887450179280829459401688087231643490099920795265644044261932511, 
           37105307030537039988022678537085291452325031359526329807537776969528831686425, 
           92938117346403131611721061906191193208723286610021864092519917726021443176727, 
           69096111760705943573314622999192185604939082041890480984362075605583421228132, 
           88282543211063824032235398553655229577400976826817027034777851470278982529952,
           
           100341745270499415663311873233218231670242647660264075745506770088471842508802, 
           89488274603804225389171841939230219448895365434485275894237396301495518554715, 
           76569347923444256958023287141542497510825013650419953885226359615086761829344, 
           81563584870525250942043937695609098622088217936406627218564791286200545169634, 
           5172851674036880809927411127200479633491103025233884330385647373127239362761,
           
           27028946396447814017188389527013970519524088371669835359929995423985710176660, 
           91425191432345758752664578760387393279775536730989321983648985485050233077173, 
           37106632025601916820095524384718640277484166308753206283110705565223659865125, 
           95633630757091468057553366794189296457777722005165038765088393126665176601628, 
           21700321939992927803622029800518580659321319021907177209646572761251239207312,
           
           80585351183873771092133446128001575555019360163939149939501448705632125870581, 
           32150157806281034227017859035132326258872818815410174001041145461220116763069, 
           100722857505322115198146208499220022084625070052526878791255362854105394503769, 
           106469741797494909039100335847700627678282797337420882550664990385374013346714, 
           7132804278995491665647913004073727223071894218922464596426342408363848451982],

           [101695400669583813810746445139700392985776378025001584089118250770932796907834, 
           73764177157514071151095645437026121983640638485837445471844106164793206724575, 
           47612803961517067692539903164155489886296618497839475581217124605877787757442, 
           109689469928430497140731974242430685833999201365656390582176427565993107439132, 
           92925713401400710623839810079810339180963862369432977099052206202543808421338,
           
           94752408506926225570773195019809612845214636045571337885576118785662754995191, 
           11687759206386098973763929965057896084026776161639951755404541571829414014711, 
           98101203433084520088882495036948260163306830748215934614306663021376543883475, 
           38102405711692653302023266297565313745133299659810858812425357382507365916015, 
           31351092313530085678216533906886348462184720764998204665947362730103914949859,
           
           108256217076716964109438974786351886511253564069794761574328767752766679462127, 
           15304140838687734950794851206661960290863334014419538915774100706533318132795, 
           82709072283389713644412475662681448886797588096875278710224629168018261066720, 
           49200972638354163255526323479406776255588449968070470863452160171711604144269, 
           53974289389691794263604396858473687710078884961553653095054485268083791771845,
           
           64169344959044255051216342262515258231712726509616860542953998077159862372026, 
           28848551368724471150105066536199026936530435177406936086517386084231870534736, 
           104291015502183623363523952253866990437044158889510055157230242566028625067489, 
           74472569422699238850867629393141696075870640202705343764051579995959485140231, 
           87929536507094745589093662126427758521580752170605256266333061522368949810462,
           
           20104728617112084322057533231445223761718071244927479043679395685789025302176, 
           27432095162820795694090765961559759463694798565217005397503632817791681430075, 
           81391314733886202614293787929560138195007878203908655329116964820273868519922, 
           28130529658036641371124331944806630207247126504233319689450121382996670420227, 
           62755672704738825954244685788727478461029435805923521444111995765377310087073],
           
           [63522566125187066556456764927373909912726211284218421011246448508692892883960, 
           2409208470116330926832310305110493054977239499386296942801684715449791849710, 
           113517673626352500141239206018899500102813717310384125436766574738317857361980, 
           37375605603684302646951325006261092494073445795806255322644516033219539977589, 
           114880691687877779925881942767867221717253840071213558427380246744809174197327,
           
           84878454492724156890692473022429866562587303151891578646443325256602367495224, 
           67024982683209163298112781081260983328866515074189854734106041088856750535141, 
           67289251102924369279640193706011109182492780977246632604738600725897862219398, 
           74196539734949063251218316599835010573375781780263598725419279417497802534054, 
           103035491321492063319453715640408659864141100610171689748449197739872601794110,
           
           90468123390936450218751360341074407346719736675459673081694357179611083294349, 
           12645883548661052429366963825503463912100475287103875168310940608683743678985, 
           17298584378449003517657383131516981400781260800849789598882870708642262049827, 
           43382465159345818425240719488884371862837229205349249451686248003358123837456, 
           17184333231159541990979421720429162150860787751672433060683713089622164361599,
           
           85905751912688945868853775351961027511796643417968681044297406470778836072369, 
           19619616534082545084214763288212327890201965937902651745172989752864033122098, 
           114305034837722378806922303182706642796704007694086261734007555841314998870105, 
           8422065751024866048555214560733396657858664308813983159970831314881993019989, 
           8836390970673200634276966705240403261784075441204861842087577814133831791933,
           
           103507277130645535632340892873715688492558113369849538491885677887520815187350, 
           105903851261146464135007034839760600071766339923319447722063319628668732286486, 
           3531388289266480766159286474225379969772569353527015040202934539198940814091, 
           109244683812902017961152300713558847361321765683346399206490596089519054694994, 
           80646533880311748120991725407185450632278907506741867369289780744460131677697],
           
           [62312548736497453480832483456650982941473578796180777137784969230386548643384, 
           64054305960678500929777904083234938546857537972919801355215258591653013196486, 
           19835137876183337719973403408040362000981861846821393735688467352621159088332, 
           18746778741407973218597871561523148403714854963385195740040441598826397863894, 
           20201604210824322513505661740215815043165403993207115450011218751649201516349,
           
           64319489048851532324315809274443245173568580931292578187609709518888738187870, 
           620267293515310378993121861842067004658214255791393188911110141928357728612, 
           57023193989683568739739210752361669886131873467621867845039573332943843441603, 
           61027345843942352680394957511608347626515939164221885864145658716321325519482, 
           83631467916978131746624347080935479606668223724092145157878977175481292579488,
           
           22037356287626745871116693210555756919633900699463377968475849850058340857595, 
           18334091981503713155729934834883289317573282149971450923858818979598056599322, 
           49269437468813983047081226226091137550704036343955284499107912240345111631819, 
           54376632048783410629814523980574571839627098984960515857200193816661241742237, 
           49861947272056015851262483357533431094963170070307377274120593412604982589944,
           
           59570315619285524355161408054244783400615402874492318919035157314876545030340, 
           108602451419317669571952729883991649762906668358612057736500138982476378807881, 
           15717803621597238813882976860792998177866559512791183131364307211176761506277, 
           14806996796080182058714852933734629420562453438498102625470459212135803145007, 
           21680531120567186364718496668574544777053950241190992174088527362220115859853, 
           
           53029544691914849058124010578912914260743308079462334553285570880688045937245, 
           86764537489341688819291702176868549487763773098877307030064773880241424768908, 
           23782076011164775602175793990786267142160872976126844175826609624016503012585, 
           99785974651708646840724572210778256755713177707187843043600802208027713095646, 
           92568377035646159171159644180226485180861997917454332207899427138690918537658],
           
           [29570929772973349417968750706070689975526920770033625399115048062619150992298, 
           96784599580189734353569887609390758722769477223581924642005694087560629449912, 
           21077299056370535147157222341468262036561137739159405038991391911128092007265, 
           69473945125418599488020607054720093749407458904586736888715945536961994897683, 
           18773976058461958245909423671154077797152685511502714027189255601719507001640,

           112265350327667086632380828459338610940626952394519975816205523170426940301221, 
           77803259844244377303300044348458411991845686083987620490483659183817018640871, 
           24645123421264148108663584292455374553896187467281258803011903031732951539800, 
           96249396594326154538609843166223288674525681265613042993829035820462274065873, 
           13641164048590688726734553679618933956098673128725974689572890788785899026227, 

           109231735584107987188923530943702254175415289578618550755335291484270100963368, 
           20588343665560642564581195412616014031907293933355100758715414611883462641969, 
           20521122663434957567991681147800704187752729568132117053456637904460773645002, 
           62468329757496509111280450036672510906602718638486390633937536932438197979523, 
           51448316374913558982100130149747296397559570961442790387524689919729616543045, 

           624647904842078174810106640583240736192976270186107800573619575203344751567, 
           58897475872112413428993391419928368160022660146520082240028140408498044117068, 
           115555873792869539907133670369201900730144823147009335351833001238284493146459, 
           19273794077020196281413933299689680098970565704088413774174798948095092028838, 
           31360016255940157391110058219506108276482320611913146486151374127144610945403, 

           31328036475983122519042329271147709268087343980682625161263317021837605825370, 
           28797444336888695224762439752444085477976508596765916191942265006134104652672, 
           16038810261442278228267248924704644020737335911978411501106645664337795646872, 
           94438980322764661753211195484091035135097567014217765514687464369022793039177, 
           19688935691509082282226516854812935938009654244821277242053025024618421003712]]
'''
         [7132786843348027683509617106225935391508638737748699303820358533878852119799,
          22202262115476576703143786724310994167269882708038512642473923066476527453120,
          9846327241871927141663034382109014318524218773305585705416150605338346338779,
          104865901099009032230511445046932151521771363669490606038609407856879688045376,
          63388054285808307401188397777640847331427019695417334808191053678473067907114],
         [65409304011354047237186567709588712533172325026467698363593724213142926988343,
          112842395804061866533073652196090434308350830110184467533442888048301276525193,
          22167638407458087456909011333524897573126473603610239756816857648794079344169,
          44328431963488937666383030730779073358015421103939273396866799542612616315874,
          104562966334847411476092532616950370438425171227329215456075892387002477874973],
         [82311233059362826292536458877051790059863656700534136836280522182928647995503,
          85570166055603503963241492763829970922073310076502773750400818987063390197163,
          50581398802476747285065499181964945506412184399799615686276017128518175627321,
          40134484064243320410604578954571590973131345465333677911899673185710823132668,
          104545717417648121169975128314758727909304342625913470898014862589977113121163],
         [48623361593403789316428535969317064530714456201628671361639035403693876576704,
          80784874429251842388832045434779236362764810205959439166878424611570650297881,
          58352991835940127247214466748328378337271782853490820375504749954439872709319,
          10827998448947705453740509451623197092332146734030359153145444172475834481420,
          42206922366291643865051189848072143512302276533955325280189998516140809922759],
         [55938223678457320586225977217529546577844133102439334408923560983580220520083,
          2848921631326935200510353395593829839243358619998526618662089992347765320249,
          59698045928224943307611385018635183240445175697043564943040187109900517325414,
          101453691664314943360165983077445994137973893060623835039764909777617875232048,
          58318025073374684892780175626710443450628931464012007176340940024729693377047]
'''
size_alpha = 0
for k in range(USER_NUM):
    for m in range(TASK_NUM):
        size_alpha += sys.getsizeof(alpha[k][m])

#加密数据
with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\ct1.txt","rb") as file:
    Serialized_ct1 = file.read()
ct1 = pickle.loads(Serialized_ct1)


with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\ct2.txt","rb") as file:
    Serialized_ct2 = file.read()
ct2 = pickle.loads(Serialized_ct2)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\e.txt","rb") as file:
    Serialized_e = file.read()
e = pickle.loads(Serialized_e)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\V1.txt","rb") as file:
    Serialized_V1 = file.read()
V1 = pickle.loads(Serialized_V1)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\V2.txt","rb") as file:
    Serialized_V2 = file.read()
V2 = pickle.loads(Serialized_V2)

with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\V3.txt","rb") as file:
    Serialized_V3 = file.read()
V3 = pickle.loads(Serialized_V3)









'''-----------------------------------函数部分-----------------------------------'''
#生成函数解密密钥
def FE_DecryptKey_generate():
    #生成y
    y = []
    for k in range(USER_NUM):
        y.append(int(1000 * weight[k] / weight_sum))
    
    #计算skm
    sk = []
    for m in range(TASK_NUM):
        sk_m = 1
        for k in range(USER_NUM):
            inverse = gy.invert(ct1[k][m],N**2)
            #t = time.perf_counter()
            sk_m = (sk_m * gy.powmod(inverse,y[k] * private_key[k],N**2)) % N**2
            #print(f'cost: {time.perf_counter() - t:.8f}s')
        sk.append(sk_m)
    print('Function decryption key generated successfully!\n')
    print(y)
    '''
    Serialized_sk = pickle.dumps(sk)
    with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\skm.txt","wb") as file:
        file.write(Serialized_sk)
    '''
    return y,sk
FE_DecryptKey_generate()


with open("F:\研究生论文资料\Code-用户任务扩充版本\experiment\our_scheme\Functional_Encryption_TD\dist_auxi.txt","rb") as file:
    Serilized_dist_auxi = file.read()
dist_auxi = pickle.loads(Serilized_dist_auxi)
#权值更新
def weight_update():

    #计算每个用户的感知数据与真值的差
    data_sub_truth = []
    for k in range(USER_NUM):
        tmp_dst = []
        for m in range(TASK_NUM):
            tmp_dst.append(dist_auxi[k][m] + alpha[k][m])
        data_sub_truth.append(tmp_dst)
    
    #计算每个用户的距离平方和
    dist = []
    for k in range(USER_NUM):
        tmp_dist = 0
        for m in range(TASK_NUM):
            tmp_dist += data_sub_truth[k][m] ** 2
        dist.append(tmp_dist)
    sum_dist = 0
    for k in range(USER_NUM):
        sum_dist += dist[k]
    
    #更新每个用户的权值
    updated_weight = []
    for k in range(USER_NUM):
        w = math.log2(sum_dist // dist[k])
        updated_weight.append(w)
    print('Updated Weight:\n')
    print(updated_weight)

#主函数
def main():
    #t = time.perf_counter()
    y,sk = FE_DecryptKey_generate()
    weight_update()
    print(size_alpha+sys.getsizeof(y)+sys.getsizeof(sk)+sys.getsizeof(dist_auxi))
    #print(f'total cost: {time.perf_counter() - t:.8f}s')

main()



