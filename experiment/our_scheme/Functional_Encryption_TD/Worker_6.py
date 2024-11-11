import gmpy2 as gy
import System_Params
import time


'''-----------------------------------数据参数部分-----------------------------------'''
U_ID = [1,2,3,4,5]
Mission = [1,2,3,4,5]

N = System_Params.N

#感知数据
Task_data_6 = [6800,127,168,71,1960]

#扰动
alpha_6 = [7132786843348027683509617106225935391508638737748699303820358533878852119799,
          22202262115476576703143786724310994167269882708038512642473923066476527453120,
          9846327241871927141663034382109014318524218773305585705416150605338346338779,
          104865901099009032230511445046932151521771363669490606038609407856879688045376,
          63388054285808307401188397777640847331427019695417334808191053678473067907114]

#用户6的公私钥
public_key = System_Params.public_key[5]
private_key = System_Params.private_key[5]

#用于零知识证明的两个随机数
Ra_1 = gy.mpz(113606409908464303126842517659434766872454131055084704272003192448553931326136213216754831170294604186893109964065289632552054373439174701443716918860895827199268830193077874019333270746779974784756974318127304897915525489272821826878266065980102905543006907196663111479895438758929352555660921674372882136177142102552172888436878543488908119628169585629552608705368371917462628781550147960956514463082763462065334636825488383021291679627891217052921547358862436859250544983576893095483315839104724972401935449992083760296374520790621650265256234182897798671443296227639646229408351535505832578621980213517683600589688598886630431413811925493644977679332097570947491097083845835966644501048757304556525241734787198602382587186438962029953252222997655237336803320752154042402404823501064183682053981706551912994100728510719009313490042671276442593934267608673983306880734613492954950465788513813621359210187543265058752469836093018969324775133658697751982562728071777822891051721468241208273780230575065257685600038598182442315526723060492402359455911932732599368162933465862344072120121876686838538973687784066636894741525740835799814800017687936843640236931536725749023355388877517776371260967448788465152004887121616919490818617018160021605681274590795583827745667561232556294846289150010381304054385642992413349713824682240659490439481050195189846922839603480982152972855875331803636777302881507446567657047265025174493739051941367253387286219943267915286391550081143216626701721762614737016689908907055212407355818879302964499730977534930974044812519290949801556728510699381837642141933192812161144934085671632329675324049335224786777904200992104585493788245119647192269060427703657323884450026308722304522801045324285049086713939357426041557353082112152691524898945787969986468494227464217163249515854908476942082479168853065352045256476436721087891474881385141416819666626390782566418611717343037859729981679714564569341377093574718022488355127592700931205396524455296989827228765767510385431099982502833688783430157856640423763821644000211267335124536419475368012032201513609711451414267732993861715651921456566211784513525542070014892084462559074159735424252886360607437000432022461506241651948140809647192916451267962404602189453717089786596314508611705455942789489154015817837620120230330568055103417149967043580960557629332482405856244755510558593805120413545957959881887632464714831855580307063278125609612347090518139010761126971936421403512289196318829793677353052356909353053618900297693822073808944400517282238516495387771976587036027836178896904808455295272975204453106823660374433215856726001141784921313603643374159913166839588516175043872649900485188593798588979305845944837168468263227984755042531225006787555075565618342739995478262069489120954118137350900891929532605799820809869393012139292543343058507994515327652730555217484359450526190115723480573074600696165862008528235732728158570319271556155780448969676559473011106153678011386283581257894185199393358075017736332406956990320457503019674354959158188618642826681046015228401809697785714126913823843458033210899838509021585393973673372292391070387337121589523006567126931885762831396096475516944587311627051281375332261777934628079697844275854478968332039605968938729261678753168356144724310260833836115141448542256162018458186763405167520259169786430739450106589215568692029055751735891956114915705760255407696047203196011701633886395127881989253683703377564749305418600147761763527385632747706645999186160178242335768477452911380477068095928833777382233551978359232587162312243428799178154301209159515371725037077043747521388020620395475029680086288798458803546196670396612534303700066821867508428247963970234927989494672545603262989542097229269511268376805920661165181747247592703104738761031431855329715143741659292703317981104670724)
Ra_2 = gy.mpz(149001654528200847480883906567296988190273310949576441492024963489056490556651506937973204070493870018794185386670232141155593690203359005697486980379334109536091008023417925080089959234315983824515088380658969449373803742985042219265332969327993191584944705413346668294561148571269947622120817738776982074711137769030082693258538587661046007764661817207725249569722893741366123390028306683197726602816922864909240069044459784401438907360554612551143005924005176202959202426749860025274142548679265342994238661474848844345582387862753475332868671333955956252850931081934867019331520326145812156208570845942876304296172109704986685338629646844680817231971990442718905120747533838716898593724247130332289195934138097184801162926502464809611119261528320564899082573079042803286438833823806183831625704587202321209196705118844007484094506071728183243091412728557913057209597698924670855655798997048059551015432779267587554869224699445326453554539287047489086181052345239834423524082524371658024641505611741858816092248118934263275017633529899237998719855617557515519921880593416385822013503954325681237145644315536726790774867059344568824878264711753555544378346887439048197782052581314128827359711442399737542880341194103935259393234028817821489357907884202059719992178015702603646127569446381854716566307690902107347147768103891554116247118141589936477094860854174389690220225154789307369022412940543470468443373975091637299479468019807552543248706958914007043060590012722067989653793494232162925131042288341778478517494079585351036907157588817313465192101338716658225042244884076366985138082421123340576502829943674569625089775657820993064238881483390882191557682624754417396391853608677900064710824920151421237726563578288946076310968399517735065724671122678945852480649508624179407787188986153722250085498035950828939956768153717210567202751769032173653440966673781894306423287410775743546856505144075810599496518084583826096529481333044299737776549794285204413865112546313849144649329917852101028108017316336150304463537896127529403761018336683906957140857323862013295334283305962081476614084891603564257153196774015304059569762199225737485725935478090696558821162444579058169288992843291216297308160728055546818100869443045247073827907482300627878835496853644242435705739058298231906351934983136210388475697806726506611225518329074874596696029585300361372668641237596315920989079013301756262728960735521490010633254727656600105674126469776147742931052923530638972360096009198105196973159208560520607279861428831479920660988998814274017932209348241624395509272848427787423701374984675721892567216901790883595248915550689439131592758761145547761722396807202475396482220946735972571173535808326059039486678614481817291329806196004777607533064864095407321927908345618264265077742323869121988381705860292153491741783831765935963142649887136390026678553298492575373722259905039559586746005952925260647971128836321265146470005162152788428785736243934162780997940527191347019500771323849270013168660938676551278513008861437249298337071231129267333275016779741044603121661235153631700826861003333920238635148050421247001917604948215683942969273015531968411032907695844860157791788947186139311913260611500507953407510329031948123885527745682562450124945601318563648459562796156250414763395966080113073743471849739056758552795479924498661308126297531430779782913718661344759518366738439234230546423239061948671916278228067705244873648582198172433321808234502708228708516473956649073028362222756604377537507550052660207861011806561913089331812778008699009708773085373277881600898299085615309738079670163224143732170733993926052184375066495385007888566568759916437536337335146657981534737136269650373279211143136932702758529757357264286961412132797544090393824474353888250608003422704932466011804858277346424872979592864102346)














'''-----------------------------------函数部分-----------------------------------'''

#加密感知数据
def FE_Encrypt_data():
    rm = []
    ct_1 = []
    ct_2 = []
    for m in range(len(Mission)):
        r,tmp1,tmp2 = System_Params.FE_Encrypt(Task_data_6[m],public_key)
        rm.append(r)
        ct_1.append(tmp1)
        ct_2.append(tmp2)
    return rm,ct_1,ct_2

#计算零知识证明
def ZKP_generate(rm):
    V_3 = (gy.powmod((1 + N),Ra_1,N**2) * gy.powmod(public_key,Ra_2,N**2)) % N**2
    data_sum = 0
    rm_sum = 0
    for m in range(len(Mission)):
        data_sum += Task_data_6[m]
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
    for m in range(len(Mission)):
        perbed_data.append(Task_data_6[m] - alpha_6[m])
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