import gmpy2 as gy
import System_Params
import time


'''-----------------------------------数据参数部分-----------------------------------'''
N = System_Params.N

U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

USER_NUM = 5
TASK_NUM = 25

Task_data_2 = [4871,123,180,80,1738,4871,123,180,80,1738,4871,123,180,80,1738,4871,123,180,80,1738,4871,123,180,80,1738]

alpha_2 = [101695400669583813810746445139700392985776378025001584089118250770932796907834, 
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
           62755672704738825954244685788727478461029435805923521444111995765377310087073]
#用户2的公私钥
public_key = System_Params.public_key[1]
private_key = System_Params.private_key[1]

#用于零知识证明的两个随机数
Ra_1 = gy.mpz(1674347217459774537823931070202881905361873032721745930089435219468405485656575916099413080496166777228057150353701545986540004776757237291919604671271446527509931437489901861933868294643371069826450287637599318599173402766684884947003227986317579152481468582592574868986112377118222458340207570531556599699300201984920684060979253697329035284590378731157927451487392582774794092242847985840359085189134597670413597071825141825749263740091586177249877696691496367296331020188410346975100987522796691876120388104153067178819844039915314497779698550685995618620397984575339148914739472192413735344587316282718862688283929005453586071080683100146536907035839290994414260635587281978533863931500533440175537615745941298311506931714962605648798079498763596544643989106623039893457005101779105673027054581572514435500319977324636094574611725763865827914464793959088882226625385035853595643103405714622879457102586460194439243886283668834545628699871249242363301565383934355648070793339689829493030304082705490805020782740542135394254289550221749093346469949853113446858822559594046924355913048892946860998076587652092065533838024348430328533045220298604283238363164179236004477612689044619319362090526526855162085637030677252083743825476693785724811846979154970768851720904483738718282736821901803654059683565798418375095653631195650750722879743891901321838222300118083243018422762288759909200923122024037656031110121283095240078627150983946592174754085598607751182854715976795834416259479507212104720932211055490412049643956354435774619915825795279856467495285902296635993247497831991142098248730896766790469080535192137969044037638341292322276370444069705948194508003102396150627090147690253789649391028250680502060688554745679058839502507724614003441479454331398224246615219842821433026337871877460910253785105103991848080461849922912027283126039232968102359217184882259330084135453826590686725397362963622633307908797167904463519368016986232821956120514813448778213711674628952493545637102523968368434761815483456012472962221907091365598928309689712527603078057814581637199909191798965974196116842136087515640791303188015214336976215387881919481013533967435146796419533143951368529098949800781453397804709273379668901669973643064023023142181243357881131986461783981684462549063817635822126329177882010051893215547555710028957073163257409377997446727426479946804945520129402592884422396417421021434460005742085675321653703238254373832941863333040051927444859258473761777064666311710504006091965848618722654885446448931762552133471123322425518361684220186048775463734969096180209975250542162375394998633539163532251627782258961450661772347130229395748353284656397306819958183852175558844510150638074802197772289292569909939475587671232229088670288618382745276110283147699367122269586963750237370421374563435183094133883837288230886464086980786657511764835335907404822306065851418875202888759242446389991411234556180534999547511635442771002497941258857784429499617074279253366172523837992182324891695267716012342369658358677647376412268606415725585991034743139103026406193482017689483744620609664531119470020825270728701392658694909430117603584984187769387912122520611037543290040261158362933976575631500766119498545019491078734213714262697099607359729948235896092435624185880057838510091138281646448481118549715251316084850233750549159495397988463862800320951440350252006608084646541041741746014673684299927517801385045907044343638394342627581926891440529157694590996479243646084257839654113620862035526950176250949053276754061514150898755018385286812417030379521277425986358493102561692319139596066161299928027016211060450468864567149755248598230357402148751792729094335991853599612431993911883704858316383247032505421807376769874262977944603633700668721719257298957485423404804811918988066395800336416483001345491864425)
Ra_2 = gy.mpz(3588353993607753202494220033920136713845120956865975366391410397748585899870949540038961068418906720340408248083760862745700020128269044903283479427483879546318079347890670994026764492115750603603796449230009641932037357525685519733558502201339172846497245514093156891525466155878449877680188812976819148053138981459082857728771146183996507213483363148520454630080405098220584956597041506074472281701670074792682708542348481853557564039801870731283694616779024576279065196870651164040924249026414429353133685961648815966241513305088829417039259796794419308137732988903074289530033576504332021695928030312458305646729861363829799896832306635343420106996357799175760612110511220395570520298785599439589559959811869396320684814476694251391807664183871247902914484623455312961320242734220170574231517495489597181124895990251862566882545283715615922765213222538730964529239187468755754022156181293493919385150648190602229336868623741166933769878559686804303361997855896685086155143084702079788862576719182505484314815804304838177119103655598244164530000441139101906450068488708208165332749557501899507123127000577058373077532008714010637661034099805076629405312953577598653555653540062144039427665320858289670104316543737628363228834205094404257030891037521035970596229381860263304347471573443836271779616040906020058576790251367407144311008879853227798567643018804200582946984131094425773869371848518829661503805826586771323265338657413362580266071223058646582906093209856085144046614543539394489609178082978005635618292591079359032552480763222009821841552121904185498991316320297970231182531054951166504549444138728556424696583283548453248365969638303425601844942482383951534161314587291507324355462569561791375475714275333799821450521200363142975037885755698929993523462916626479942019810503695299465327298356260512725700869451315378314397883246676398781183546666384448962078998098549938919213101488250423308445511886683781154203701461131791820409083453673723010089546007376081368807347270994243823975117734787091218165215573855484707524977786743414786991263565044334087886622804221322256401531676436562651923973199584656602772492305148697184442202210503697311815972583747505077078634869191767920291854919554418764955703608070296509552921572201614918206570631710979906426742261756790245589896988787371513247033641269578453642846385180244710693428184036901393578602348461953625138716441768185623854862762549292680072492481356470250805962016326441684851669618876591005661502187366706540905322697272109394855770894610395857565663272640078952230156490878053169641942474694568588376841155191697297875126081051729358084806286568064034926101076447310736587564602215513730751992430684521575163372853980760737427978050725416139016502998538458984244220306543277087815865388655152337763909892019049255218167583679562511745583570386934041489756956766933758217355921487058524768113642247383355306418461660842300973059315796506135726073035132593476328492259757069097722672189232627343575557361593498519442029542734241660077752748904537628067749370212194448159555002198854368577700712733593144703688668769321118193387245299205281113099197769152668441925035788659650070074045573839134845805891621410267456502776513074376132286783292901148802062502188239386016565815462379029127731494062185217599761655485664607106157524523506473204056435079575726190811472221396515689160362919263806381790055923103826855198771156022326950894111828244013194304711412746426732995034439146807921881061108462569846591956947458478787259150948767054395666704221911064324442149029245219486206017567644955221952575040860709058484158108966835407405691847481493025071028564969197378970285569081177423753535346547143643947086769980905345384658674657261023312418944091847326650701130234638949316632009966580200829618236150081022570932333003579629719623593169074964)














'''-----------------------------------函数部分-----------------------------------'''

#加密感知数据
def FE_Encrypt_data():
    rm = []
    ct_1 = []
    ct_2 = []
    for m in range(TASK_NUM):
        r,tmp1,tmp2 = System_Params.FE_Encrypt(Task_data_2[m],public_key)
        rm.append(r)
        ct_1.append(tmp1)
        ct_2.append(tmp2)
    return rm,ct_1,ct_2

#计算零知识证明
def ZKP_generate(rm):
    V_3 = (gy.powmod((1 + N),Ra_1,N**2) * gy.powmod(public_key,Ra_2,N**2)) % N**2
    data_sum = 0
    rm_sum = 0
    for m in range(TASK_NUM):
        data_sum += Task_data_2[m]
        rm_sum += rm[m]
    h1 = (gy.powmod((1 + N),data_sum,N**2) * gy.powmod(public_key,rm_sum,N**2)) % N**2
    s = str(h1) + str(V_3)
    e = System_Params.hash_to_group(s,N)
    V_1 = e * data_sum + Ra_1
    V_2 = e * rm_sum + Ra_2
    return e,V_1,V_2,V_3

#扰动数据生成
def perbed_data_generate():
    perbed_data = []
    for m in range(TASK_NUM):
        perbed_data.append(Task_data_2[m] - alpha_2[m])
    return perbed_data

#主函数
def main():
    #t = time.perf_counter()
    rm,ct_1,ct_2 = FE_Encrypt_data()
    e,V_1,V_2,V_3 = ZKP_generate(rm)
    perbed_data_generate()
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    return ct_1,ct_2,e,V_1,V_2,V_3
#main()