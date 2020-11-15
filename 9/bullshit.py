#!/usr/bin/env python3

import random 

li1 = ["Erõforrás-alapú megközelítéssel kell",
"Egy absztrakciós létra mentén kell",
"Alapvetõ fontosságú",
"Kiemelt projektünk",
"A menedzsment célja",
"Teljes összhangban kell",
"Belsõ kommunikáció révén kell",
"Csapatmunkában szükséges",
"Még ma szükséges",
"Nem tûr halasztást",
"Fontos lenne", 
"Szükséges lenne", 
"Szükséges", 
"Vállalatunk célja", 
"Kiemelt fontosságú feladat",
"Ennek szellemében kell",
"Formállogikai alapon kellene",
"Alkotó folyamat keretében kell",
"Felelõsséggel kell",
"A következõt kell tennünk:",
"Egyetlen megoldásunk van:",
"Az egyetlen kiút:",
"Tanácsadóink szerint célunk:",
"A menedzsment szeretné",
"Az üzletág szeretné",
"Most kell",
"Nincs más hátra, mint",
"Ne felejtsük el",
"Ne szalasszuk el",
"Szeretném",
"Célom",
"Az eddigiek szerint kell",
"A lényeg:",
"Feladatunk:",
"Küldetésünk:",
"A mai legfontosabb prioritás:",
"Megpróbáljuk",
"Megpróbálom",
"Megkíséreljük",
"Megkísérlem",
"Próbáljátok meg",
"Meg kell próbálnunk",
"Küldetésem",
"Új koncepció szerint kell",
"Azonnal szükséges",
"Egy megoldás van:",
"Kreatív módon kell",
"Sürgõsen szükséges",
"Személyes célom",
"Nincs más dolgunk, mint",
"Nincs más feladatom, mint",
"Legfontosabb feladatom",
"Legfontosabb küldetésem",
"Elsõdleges fontosságú lenne",
"Elengedhetetlen lenne",
"Létfontosságú dolog",
"Elengedhetetlenül fontos lenne",
"Itt az idõ",
"Nem halaszthatjuk el",
"Kreatív módon kell",
"Elemzések segítségével kell",
"Kreatív módon kéne",
"Látványosan kell",
"Minél feltûnõbben kell",
"Professzionális módon kell",
"Megfelelõ idõzítéssel kell"]

li2 = ["implementálni",
"átültetni",
"aggregálni", 
"aktívan menedzselni",
"aktiválni",
"allokálni", 
"analizálni", 
"áramvonalasítani", 
"arányosítani", 
"áthangszerelni", 
"átváltoztatni", 
"átvariálni", 
"átvezetni", 
"bátorítani",
"betanítani",
"befolyásolni", 
"benchmarkolni", 
"bevetni", 
"birtokba venni", 
"bõvíteni", 
"szûkíteni", 
"ellenõrizni", 
"elõmozdítani", 
"életre kelteni",
"facilitálni", 
"fejleszteni", 
"felnevelni", 
"felruházni", 
"felszabadítani", 
"forradalmasítani", 
"generálni", 
"hasznosítani", 
"hatékonyabbá tenni", 
"innovatívan fejleszteni", 
"integrálni", 
"iterálni", 
"kihangsúlyozni",
"kiválasztani",
"leválogatni", 
"leválasztani", 
"kihasználni",
"kiterjeszteni", 
"kultiválni", 
"lefoglalni", 
"lehetõvé tenni", 
"márkázni", 
"maximalizálni", 
"meghatározni", 
"megragadni", 
"megváltoztatni", 
"menedzselni", 
"monetizálni", 
"motiválni",
"növelni", 
"nyilvánvalóvá tenni", 
"optimalizálni", 
"ösztönözni", 
"kiépíteni", 
"rávilágítani",
"racionálisan végiggondolni",
"racionalizálni", 
"ritkítani",
"sûríteni",
"strategizálni", 
"struktúrálni", 
"szakmailag felügyelni", 
"szétszabdalni", 
"szimulálni",
"szindikálni", 
"szinergizálni", 
"szinkronba hozni", 
"sztenderdizálni",
"szintetizálni", 
"támogatni",
"targetálni", 
"termékesíteni", 
"testreszabni",
"toborozni",
"tipizálni",
"tiszta lappal kezdeni", 
"transzformálni", 
"túlteljesíteni", 
"új kontextusba helyezni", 
"újra feltalálni", 
"újra meghatározni", 
"újradefiniálni", 
"újrapozícionálni", 
"újratermelni", 
"vizionálni", 
"vizualizálni"]


li3 = ["a közösségi normáknak megfelelõ",
"a decentralizált", 
"a dinamikusan növekvõ", 
"a dinamikusan növekvõ", 
"a divergens",
"a fontos",
"a felvállalható", 
"a forradalmian új", 
"a funkció-specifikus", 
"a globális preferenciák szerinti", 
"a hatásos", 
"a hatékony", 
"a hibátlan", 
"a holisztikus", 
"a kihívást jelentõ", 
"a konvergens",
"a konzisztens", 
"a korrigálható",
"a korreláló", 
"a költséghatékony", 
"a közszolgáltatási", 
"a kultúraidegen",
"a kritikus", 
"a kvázi-projekt-szerû",
"a marketing-szemléletû", 
"a megfelelõen elõkészített",
"a meghatározandó",
"a megtérülõ",
"a metakommunkiációs", 
"a one-stop-shop-szerû",
"az összehangolt",
"a piacvezetõ", 
"a proaktív", 
"a prudens",
"a reakcióképes",
"a robosztus", 
"a racionális",
"a rendszeres", 
"a rugalmas", 
"a sajátos", 
"a stagnáló", 
"a stratégiai céloknak megfelelõ", 
"a stratégiáknak megfelelõ", 
"a súrlódásmentes", 
"a szárnyaló", 
"a széles körben használt", 
"a személyre szabott", 
"a szinergizált", 
"a tudatos", 
"a vállalati szintû", 
"a vállalati szintû", 
"a vállalatspecifikus", 
"a vállalható", 
"a valós idejû", 
"a vertikális", 
"a világszínvonalú", 
"a virtuális", 
"a vizionált", 
"a vonzáskörzeten belüli", 
"a XXI. századi színvonalú", 
"az autonóm",
"a heteronóm",
"az apatikus",
"a közömbös",
"a személyközi",
"a szûkös",
"a rutinos",
"az atipikus", 
"az átlátható", 
"az attraktív", 
"az egységsugarú", 
"az együttmûködõ", 
"az elosztott", 
"az elõvárosi",
"az elõnyös", 
"az értéklánc menti", 
"az értéknövelt", 
"az európai színvonalú", 
"az európai uniós", 
"az extenzív", 
"az idõzített",
"az igazgató úr által is említett", 
"az innovatív", 
"az integrált", 
"az interaktív", 
"az intuitív", 
"az irányvonalnak megfelelõ", 
"az ügyfélbarát", 
"az ügyfélközpontú", 
"az ügyféloldali", 
"az ütemes", 
"a távolsági"]

li4 = ["szinergiákat",
"adatbázist", 
"ágazatközi munkamegosztást", 
"akció-rádiuszt", 
"akcióterveket",
"belsõ hatékonyságot",
"beruházási megtérülést", 
"beszállító-menedzsmentet", 
"csatlakozási pontokat", 
"csapatot",
"csatornákat", 
"derogációt", 
"desztinációszenzitív portfoliót", 
"együttmûködéseket",
"egységköltséget",
"egység-díjtételt", 
"ellátási láncokat", 
"emberi erõforrást", 
"eredményjavító hatást", 
"erõforrás-menedzsmentet", 
"erõforrásokat", 
"értékláncot",
"értékesítési rendszert", 
"fejlesztéseket", 
"feladatmegosztást", 
"flotta-menedzsmentet", 
"fogyasztói bázist",
"frontvonalat",
"front-office-t",
"front-office on-stage vonalat", 
"front-office backstage vonalat", 
"hálózatokat", 
"háttérszolgáltatásokat", 
"hatalmi centrumot",
"imázs-alakítást", 
"infrastruktúrákat", 
"intermodalitást", 
"interoperabilitást", 
"irányelveket",
"irányítási filozófiát", 
"jogharmonizációt", 
"kapacitás-kihasználtságot", 
"kapcsolatokat", 
"kezdeményezéseket", 
"koncepciót", 
"kontextust",
"kontrollingot", 
"konvergenciákat",
"költségérzékeny szegmenst",
"környezet-elemzést",
"kritériumokat",
"látványtechnológiát",
"leválasztási stratégiát",
"marketing-kutatást", 
"marketing-miómát",
"marketing-szemléletet",
"megoldásokat", 
"méretgazdaságosságot",
"mérföldköveket", 
"metodológiákat", 
"minõségi szolgáltatásokat", 
"minpõségi indikátorokat",
"minõség-monitoringot",
"munkacsoportot",
"mûködési költségeket",
"optimalizálási koncepciót", 
"outsourcingot", 
"paradigmákat", 
"piaci megjelenést", 
"piaci potenciált", 
"piaci pozíciót", 
"piaci réseket",
"piaci trendeket",
"piacokat", 
"pilot projektet", 
"platformokat", 
"portálokat", 
"projekteket", 
"reklámanyagot", 
"rendszereket", 
"rendszertervezési technológiát",
"sémákat", 
"stratégiai célokat", 
"szabályozásokat", 
"szegmentumokat", 
"személyszállítást",
"szervezeti kultúrát",
"szolgáltatási folyamatrendszert",
"szolgáltatás-felügyeletet", 
"szolgáltatást", 
"sztenderdizációt",
"támogató tevékenységet",
"termékpalettát",
"termékportfolió-átalakítást",
"technológiákat",
"tevékenység-menedzsmentet",
"tudásközpontot",
"tranzakciós költséget", 
"újraelosztó-rendszert", 
"ügyfeleket",
"ügyfélreferenst",
"ügyfél-kiszolgálást", 
"ügyfélorientált trendeket",
"üzletmenetet", 
"vállalati imázst",
"VIP-ügyfeleket",
"versenyhelyzetet",
"versenyelõny-forrást"]
  
def get_bullshit():
     max1=65
     max2=89
     max3=91
     max4=107
     
     index1=random.randint(0, max1)
     index2=random.randint(0, max2)
     index3=random.randint(0, max3)
     index4=random.randint(0, max4)
     
     return li1[index1] + " " + li2[index2] + " " + li3[index3] + " " + li4[index4] + "."
