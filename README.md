# Apraksts

Šis kods ir personīgā finanšu pārvaldnieka lietotne, kas uzrakstīta Python valodā. Tā ļauj lietotājiem pievienot, apskatīt, labot un dzēst finanšu darījumus, kā arī vizualizēt izdevumus un salīdzināt ienākumus ar izdevumiem dažādos mēnešos.

Funkcija **add_transaction** pievieno jaunu darījumu CSV failā. Tai nepieciešami četri parametri: datums, kategorija, darījuma veids un summa. Darījums tiek ierakstīts kā jauna rinda CSV failā.

Funkcija **view_transactions** lasa CSV failu un izdrukā visus darījumus ar to rindu numuriem. Šī funkcija ir noderīga, lai apskatītu visus darījumus un izvēlētos darījumus, kurus labot vai dzēst.

Funkcija **edit_transaction** aizstāj esošo darījumu CSV failā. Tai nepieciešami pieci parametri: rindas numurs, datums, kategorija, darījuma veids un summa. Funkcija vispirms ielasa visus darījumus sarakstā, aizstāj norādīto darījumu, pēc tam ieraksta atjaunināto sarakstu atpakaļ failā.

Funkcija **delete_transaction** noņem esošo darījumu no CSV faila. Tai nepieciešams viens parametrs: darījuma rindas numurs. Tāpat kā funkcija edit_transaction, tā ielasa visus darījumus sarakstā, noņem norādīto darījumu, pēc tam ieraksta atjaunināto sarakstu atpakaļ failā.

Funkcija **plot_expenses** lasa CSV failu un izveido stabiņdiagrammu izdevumiem pa kategorijām, izmantojot matplotlib. Vispirms tā aprēķina kopējo izdevumu summu katrā kategorijā un pēc tam attēlo rezultātus.

Funkcija **validate_input** pārbauda, vai lietotāja ievadītie dati ir derīgi. Tam nepieciešami divi parametri: ievades virkne un ievades veids. Tā pārbauda, vai datums ir pareizā formātā un vai summa ir derīgs skaitlis.

Funkcija **compare_income_expense** salīdzina kopējos ienākumus un izdevumus pašreizējā mēnesī ar iepriekšējo mēnesi. Tā lasa CSV failu un aprēķina kopējos ienākumus un izdevumus katrā mēnesī, pēc tam izdrukā rezultātus.

**Izmantotās Python Bibliotēkas un To Lietošanas Pamatojums:**
1. csv: Šī bibliotēka tiek izmantota darbam ar CSV failiem, kas ir vienkāršs un plaši izplatīts datu glabāšanas formāts. Python csv modulis ļauj efektīvi lasīt un rakstīt datus CSV failos, kas ir svarīgi finanšu darījumu uzglabāšanai un apstrādei.
2. matplotlib.pyplot: Šī ir datu vizualizācijas bibliotēka, kas ļauj izveidot dažādus grafikus un diagrammas. Projekta kontekstā matplotlib.pyplot tiek izmantots, lai izveidotu izdevumu kategoriju stabiņdiagrammas, nodrošinot vizuāli saprotamu attēlojumu par lietotāja tēriņiem.
3. datetime: Šī bibliotēka tiek izmantota datuma un laika apstrādei. Tas ir ļoti svarīgi finanšu lietotnēs, kur precīza datuma un laika reģistrācija ir būtiska. datetime ļauj pareizi formatēt un salīdzināt datumus, kas nepieciešams darījumu pievienošanai, validācijai un datu analīzei.

**Metodes Programmatūras Izmantošanai:**
**Darījumu Pārvaldība:** Lietotne ļauj lietotājiem pievienot jaunus darījumus, skatīt visus darījumus, rediģēt vai dzēst tos. Šī funkcionalitāte ir svarīga, lai nodrošinātu elastīgu finanšu pārvaldību.

**Datuma un Summas Validācija:** Pareiza datuma formāta un summu validācija ir būtiska, lai nodrošinātu datu precizitāti un izvairītos no kļūdām finanšu datu ievadē.

**Izdevumu Vizualizācija:** Izveidojot vizuālus attēlojumus par izdevumiem, lietotne palīdz lietotājiem labāk saprast un analizēt savus finanšu paradumus.

**Ienākumu un Izdevumu Salīdzinājums:** Šī funkcija ļauj lietotājiem salīdzināt ienākumus un izdevumus pa mēnešiem, kas palīdz izprast finanšu plūsmas tendences un plānot budžetu.

Kopumā šī lietotne ir izstrādāta, lai nodrošinātu lietotājiem vienkāršu un efektīvu rīku finanšu pārvaldībai, izmantojot Python valodas bibliotēkas un metodes, kas optimizē datu apstrādi, validāciju un vizualizāciju.
