import gmpy2 as gy
import System_Params
import time
import sys

'''-----------------------------------数据参数部分-----------------------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

N = System_Params.N

USER_NUM = 5
TASK_NUM = 25

#感知数据
Task_data_1 = [4000,125,174,76,2000,4000,125,174,76,2000,4000,125,174,76,2000,4000,125,174,76,2000,4000,125,174,76,2000]

#扰动
alpha_1 = [22410642974084585442191727643918586647230232556525075962101709016346283694569, 
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
           7132804278995491665647913004073727223071894218922464596426342408363848451982]
size_alpha = 0
for m in range(TASK_NUM):
    size_alpha += sys.getsizeof(alpha_1[m])

#用户1的公私钥
public_key = System_Params.public_key[0]
private_key = System_Params.private_key[0]

#用于零知识证明的两个随机数
Ra_1 = gy.mpz(2565325663170424239797234943705600215449062977821563004104933298764215903403261887977418291625451934781478636794943076197446069193286611028553718782057543999386329845044391170827659913801241136784498961590731216394239215053910917372185296854531232314601256045873994776678329244006212059998496940024907622106614680628074947550717042531547304211205603147710252831680209941827990396413407574516461576743059002780798279724313355795179816614981991063074843184357914017535569940730645068116513324195795520514256658760999426682298666178674866312884433543248441152261847295810076388853938184901628502492330253157557530373025679940362250157665880266568962185953988078610556055204730352215911874223341960144449244666762244139645110642048361436020795581613110447347442500295632077643615496823325471386729806773966581081799328769722213731930596926516436198397634428838209009485994221312900005319582418360014903569546432590333794689618408831457223819527451969597182712629452356594868685519281435372258143403715166544443917025883027129289487683763340401463678309483264078524980575018833967350880556220448550509657209097425845091739775880781273926881562289123215465319547632466229687097415712358481522890931616658295573000516045992455511251121180517980423681648819573516629707781165246332222590398525215604471727620192290862500975963753890974005128182570746958889845231735032583266747104454224632838478897264911361054937486572531009382173238339380634753715346427260673734862271513918612206249903180823520297231106203701247379705823023998649708306289743872778067781478015731854781983886624320635498436110419096010185293167344670759577102056047767322147912123399930705178769861861630823789493510486381589025518720471621953957155937470166965253297567544042929051898725365580420943070811043625267679809688498364206398953070488577784518241342177431697975202970648697366224852508650923492496222167209493597472643117163459765967512459667063063293807422882533294355520261025812076675245569550425674832290029231150946718876558317585335147663265063326874874071883050497844806933038531095059156008606760826313717005701575456869447368085480934691482723648439981564363171120481979144876482040847895888475398473484515761831856010576228031167763045333014906576139343175316890972764596952735758695184181468989465354592573611399680542960714671961774038326873857367501408552620480114038380884436054979497449938581886754051855536362810244801709022565530891002536246264298471489964240482963113521545666907246027583048006069678373246544857833508665138595866289708671704002779710830760787630131964385934594175316975712992036414684319013040354373278863910436895409154705786571612754147335149529346894464577919090618383574926142304149675937951330942376641060050877458171189966194841683452479661642833078439201479851469214948041112858031731787390499456454950977669807590078572947736318486987279348927917321804096622297981937359345247514860829655218814464393289966847608411774389520593071072353797372519478239406115923102965182131973724186032619399840816652264127254965952407490392673212075073475700792075379598877742962507192502047320775045530436761105011826340652000557486218485119409313590328069174793532698322478155806545328369250102552045796690615719702543580214828439799603191175257291141938251140304404026640866742049160558340142320431765129722361803603695080412523153921533763095862333448555696747843450421423480068868107027346995630982589543165152714655673013714256217927287117464691715110640090985379771115705326480715067832606974792659753598165165431249416967150790936557713122569356708149013161038629301315228546203917037839609042105236466404553763472264257321577447138849265399236677703974921968831095191648633642015171082390197482893219821389809538046295401670420299727436546874689382856469345657731581198041194949553964904076869198909222447350)
Ra_2 = gy.mpz(2454071660809688258188344163679671123129743681737251181848553641857386542218850850255742119946395636643460330041955618810714423347130818898535750946813467192487061053560795217899193228050027294711914442454958560018735699347719134953927722327330952113382277972900087915679963873292922606026620779607475073866782736851400808770927875854132696326269251759233476477006302110760259321274533937686127006618310790592631694695265744426251620835549633940970686307817471234415995881735479072458138843252168897184198522787670023367626205056491317019648501803707722923060079780238373300834556354955871475790842112050209927585865502323333337999204620164182266423704695478788971881841312400828021762083736402344257677215857818471659660752745162323346321503701024119011102497740925525790025372119558689994660433833738784718486476209214887245156675477923058293226454131473289263218734949328046883858580688814416604224211835600728656700542906861855136305350440235744239926956566545317695473225266839577342008529308274500445315486573662572504784681641822662687761318930122493241241036269824827660230343294484495758629214255205332701815931731804424730356641385978522315122933059735779922005667780439050601957780208405136267814620502668135652654736399342276720598704179735210575909339752123275695363872572394538112591955941629446759198790658298845363447655989155284103593255231482381910984195516877447277010790028584389055650688005642941041459340398630986282158499193998817918066388227505591861751280115951346354910388819127554958518783394384941207137299633510254482443286070508127705986699762969793168492761223902033609958858732383620698886472871235162416415037810682740824513259113126929166991036716188580216123173588138572428861730645304995755672356707481678343955532538605516162108494694140214286089368160220599493383508378800312077581644174994463834853866185561810900190705415650852382457736261777760905666463144779392997353617677385856202548440719422120061677578392732005033296641842325809971089358788617532869825266278322445021508417415101737992211243468300714513154441118889220755917847175982388705362538925766964606783088802954176430273288134692125388058525974076432399372280695285525828437939282773841082029978635790819762890019058552212550025461259523022864214356876695334675059686396451828778761451778199390365928572651810949920537559168511677927616255932827743033136201597890847941065292958042108793544579987616084308705243624778451913705753558257888216292529344605504749412652839533104201658936008913237455678891213620362045933064820752315851351145105741150034535125812252461829441614955694467747834092124416767767114676995174481813230276802797574921585928676495463004317442177633260523821174449328401366687790976513352113662134927045502327697025314254263738944636301490714202125130981147315696610293905617300370858691483820922142525589903303188185087360683723626575785664044823567164122430099140310313175776736054687646426391805393075252861029016225345947091624119951465656050893002873299353618776122143896879010241086477162327127626315632834362401477842684117046801368053239373393706952425853824861089557154436895037738843012797526699239279469479283450632823272642916751109917026833113527096697761720248521339286784951406580989943030353246318857010296888584747751494420620919788695279353810855916665074003506297126658159347690138154359374527430784731317976414369479919465208740629237534905139151154659938241694730344781663649139119851370432393371877486065520594093574820502494129173001917124426727962211370763893000762082634965804400514661262548962130710569204523552924844006635463547135739597668907667273249817201363782216711283668394826449765021182976353326667419721007549766029961192608036179795835370280551855835807907801468339669742843448695826923440485346716905522663338026079412902928032196160500627514617295382796)














'''-----------------------------------函数部分-----------------------------------'''

#加密感知数据
def FE_Encrypt_data():
    rm = []
    ct_1 = []
    ct_2 = []
    for m in range(TASK_NUM):
        #t = time.perf_counter()
        r,tmp1,tmp2 = System_Params.FE_Encrypt(Task_data_1[m],public_key)
        #print(f'cost: {time.perf_counter() - t:.8f}s')
        rm.append(r)
        ct_1.append(tmp1)
        ct_2.append(tmp2)
    return rm,ct_1,ct_2
#rm,ct_1,ct_2 = FE_Encrypt_data()

#计算零知识证明
def ZKP_generate(rm):
    
    V_3 = (gy.powmod((1 + N),Ra_1,N**2) * gy.powmod(public_key,Ra_2,N**2)) % N**2
    
    data_sum = 0
    rm_sum = 0
    for m in range(TASK_NUM):
        data_sum += Task_data_1[m]
        rm_sum += rm[m]
    h1 = (gy.powmod((1 + N),data_sum,N**2) * gy.powmod(public_key,rm_sum,N**2)) % N**2
    s = str(h1) + str(V_3)
    e = System_Params.hash_to_group(s,N)
    V_1 = e * data_sum + Ra_1
    V_2 = e * rm_sum + Ra_2
    return e,V_1,V_2,V_3
'''
t = time.perf_counter()
ZKP_generate(rm)
print(f'cost: {time.perf_counter() - t:.8f}s')
'''

#扰动数据生成
def perbed_data_generate():
    perbed_data = []
    for m in range(TASK_NUM):
        perbed_data.append(Task_data_1[m] - alpha_1[m])
    return perbed_data

#主函数
def main():
    #t = time.perf_counter()
    rm,ct_1,ct_2 = FE_Encrypt_data()
    e,V_1,V_2,V_3 = ZKP_generate(rm)
    pd = perbed_data_generate()
    #print(f'cost: {time.perf_counter() - t:.8f}s')
    #print(size_alpha+sys.getsizeof(ct_1)+sys.getsizeof(ct_2)+sys.getsizeof(e)+sys.getsizeof(V_1)+sys.getsizeof(V_2)+sys.getsizeof(V_3)+sys.getsizeof(pd))
    return ct_1,ct_2,e,V_1,V_2,V_3
#main()